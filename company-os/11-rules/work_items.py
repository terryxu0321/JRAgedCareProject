"""Show each team member's open work and personal work record (work-log-rules.md).

	python company-os/11-rules/work_items.py                     open work of every member
	python company-os/11-rules/work_items.py --member Matt       open work of one member
	python company-os/11-rules/work_items.py --me                open work of CAREKIND_MEMBER (SessionStart hook)
	python company-os/11-rules/work_items.py --member Matt --log [--days 14]   work record of one member

Sources (read-only, never a second copy — DRY):
	PRD Assignee lines (docs/PRD.md, specs/*.md)              — DR-006 / skill assign-prd
	ADLC task files adlc/tasks/T-*.md, when they exist          — ADLC spec §6
	changelog/CHANGELOG.md entries whose 请求人 is the member   — changelog-rules
	changelog/ai-edits.jsonl lines whose member is the member   — hook_log_change.py
	02-operating-rhythm/standups/ (today's report exists?)      — skill standup, standup.py

Lists work items only: no counts, durations or rankings (WL-5, NSW Workplace Surveillance Act).
"""
import argparse
import datetime
import json
import os
import pathlib
import re
import sys

from check_rules import ASSIGNEE_LINE, ROOT, documents_requiring_legal_references, roster_names

MEMBER_ENV = 'CAREKIND_MEMBER'
TASKS_DIR = ROOT / 'company-os' / '06-app-development' / 'adlc' / 'tasks'
CHANGELOG = ROOT / 'changelog' / 'CHANGELOG.md'
EDITS_LOG = ROOT / 'changelog' / 'ai-edits.jsonl'
STANDUP_DIR = ROOT / 'company-os' / '02-operating-rhythm' / 'standups'
CLOSED_TASK_STATUSES = frozenset({'done', 'cancelled'})

FRONT_MATTER = re.compile(r'^---\n(.*?)\n---', re.S)
TASK_FIELD = re.compile(r'^\s*(id|title|status|owner|executor|reviewer|due):\s*(.*?)\s*(?:#.*)?$', re.M)
CHANGELOG_ENTRY = re.compile(r'^## (\d{4}-\d{2}-\d{2}) · [^·\n]+ · ([^\n]+)\n+- \*\*请求人\*\*[:：]\s*([^\n]+)', re.M)


def same_name(left: str, right: str) -> bool:
	# ADLC task files use lower-case ids ("matt"); the roster uses "Matt".
	return left.strip().casefold() == right.strip().casefold()


def resolve_member(name: str, members: set[str]) -> str | None:
	return next((m for m in members if same_name(m, name)), None)


def assigned_prd_paths(member: str) -> list[str]:
	paths = []
	for doc in documents_requiring_legal_references():
		for match in ASSIGNEE_LINE.finditer(doc.read_text(encoding='utf-8')):
			name = (match.group('cell') or match.group('item') or '').strip().strip('*').strip()
			if same_name(name, member):
				paths.append(doc.relative_to(ROOT).as_posix())
	return paths


def standup_file(member: str, day: datetime.date) -> pathlib.Path:
	return STANDUP_DIR / f'{day.isoformat()}_{member}.md'


def read_task(path: pathlib.Path) -> dict[str, str]:
	match = FRONT_MATTER.match(path.read_text(encoding='utf-8'))
	if not match:
		return {}
	return {key: value.strip('\'"') for key, value in TASK_FIELD.findall(match.group(1))}


def open_tasks(member: str) -> list[str]:
	items = []
	for path in sorted(TASKS_DIR.glob('T-*.md')) if TASKS_DIR.is_dir() else []:
		task = read_task(path)
		status = task.get('status', '')
		if status in CLOSED_TASK_STATUSES:
			continue
		label = f"{task.get('id', path.stem)} {task.get('title', '')} [{status}] due {task.get('due') or '-'}"
		if same_name(task.get('executor', ''), member):
			items.append(f'任务（执行）: {label}')
		elif same_name(task.get('owner', ''), member):
			items.append(f'任务（负责）: {label}')
		if status == 'in-review' and same_name(task.get('reviewer', ''), member):
			items.append(f'待你评审: {label}')
	return items


def open_work(member: str) -> list[str]:
	return [f'PRD Assignee: {path}' for path in assigned_prd_paths(member)] + open_tasks(member)


def changelog_entries(member: str, since: datetime.date) -> list[str]:
	text = CHANGELOG.read_text(encoding='utf-8') if CHANGELOG.exists() else ''
	return [
		f'{date} {title.strip()}'
		for date, title, requester in CHANGELOG_ENTRY.findall(text)
		if same_name(requester, member) and datetime.date.fromisoformat(date) >= since
	]


def edited_files(member: str, since: datetime.date) -> list[str]:
	files: dict[str, str] = {}
	lines = EDITS_LOG.read_text(encoding='utf-8').splitlines() if EDITS_LOG.exists() else []
	for line in lines:
		try:
			entry = json.loads(line)
		except json.JSONDecodeError:
			# A malformed line must not hide the rest of the record.
			print(f'work_items: skipped unreadable line in {EDITS_LOG.name}', file=sys.stderr)
			continue
		day = str(entry.get('timestamp', ''))[:10]
		if same_name(str(entry.get('member') or ''), member) and day and datetime.date.fromisoformat(day) >= since:
			files[str(entry.get('file'))] = day
	return [f'{day} {path}' for path, day in sorted(files.items(), key=lambda item: item[1])]


def print_section(title: str, items: list[str], empty: str) -> None:
	print(title)
	for item in items or [empty]:
		print(f'  - {item}')


def print_open_work(member: str) -> None:
	print_section(f'{member} 的未完成工作：', open_work(member), '无')


def print_log(member: str, days: int) -> None:
	since = datetime.date.today() - datetime.timedelta(days=days)
	print(f'{member} 的工作记录（{since} 起）')
	print_section('CHANGELOG 任务：', changelog_entries(member, since), '无')
	print_section('AI 改动过的文件：', edited_files(member, since), '无（只记录设置了 CAREKIND_MEMBER 之后的 Claude Code 编辑）')


def run_session_start(members: set[str]) -> int:
	# SessionStart hook: must never block a session, so problems are reported and exit 0.
	name = os.environ.get(MEMBER_ENV, '')
	member = resolve_member(name, members) if name else None
	if member is None:
		print(f'[work-log] {MEMBER_ENV} 未设置或不在团队名册中（当前值："{name}"），本次 AI 改动无法归属到成员。设置方法见 company-os/11-rules/work-log-rules.md WL-1。')
		return 0
	print(f'[work-log] 当前成员：{member}（work-log-rules.md）')
	print_open_work(member)
	if not standup_file(member, datetime.date.today()).exists():
		print(f'[standup] {member} 今天的站会尚未提交 —— 说"提交站会"或运行 skill standup。')
	return 0


def main() -> int:
	sys.stdout.reconfigure(encoding='utf-8')
	parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
	parser.add_argument('--member', help='team-roster name')
	parser.add_argument('--me', action='store_true', help=f'use {MEMBER_ENV}; for the SessionStart hook')
	parser.add_argument('--log', action='store_true', help='show the work record instead of open work')
	parser.add_argument('--days', type=int, default=14, help='work-record window in days (default 14)')
	args = parser.parse_args()
	members = roster_names()
	if args.me:
		return run_session_start(members)
	if args.member:
		member = resolve_member(args.member, members)
		if member is None:
			print(f'"{args.member}" 不在团队名册中：{", ".join(sorted(members))}', file=sys.stderr)
			return 1
		print_log(member, args.days) if args.log else print_open_work(member)
		return 0
	if args.log:
		print('--log 需要 --member：工作记录只按单人查看（WL-5）', file=sys.stderr)
		return 1
	for member in sorted(members):
		print_open_work(member)
	if not TASKS_DIR.is_dir():
		print(f'（ADLC 任务目录尚未建立：{TASKS_DIR.relative_to(ROOT).as_posix()}，目前只列出 PRD Assignee）')
	return 0


if __name__ == '__main__':
	sys.exit(main())
