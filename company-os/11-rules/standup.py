"""Daily standup support for skill `standup` (work-log-rules.md WL-6).

	python company-os/11-rules/standup.py --context [--member Matt]   reminders before a member submits (default: CAREKIND_MEMBER)
	python company-os/11-rules/standup.py --summary [--date 2026-10-12]   who submitted, and every blocker, for one day

Standup reports live in company-os/02-operating-rhythm/standups/YYYY-MM-DD_<Member>.md and are written
by the skill; this script only reads them. Reports are self-reported work status — no counts, streaks or rankings (WL-5).
"""
import argparse
import datetime
import os
import pathlib
import re
import sys

from work_items import (
	MEMBER_ENV, ROOT, STANDUP_DIR, assigned_prd_paths, open_work, resolve_member, roster_names, standup_file,
)

PRD_SECTION = '负责的 PRD（自动）'
PLAN_SECTION = '今天计划'
BLOCKER_SECTION = 'Blockers'
NO_BLOCKER = re.compile(r'^\s*(?:无|none|n/?a|-)?\s*$', re.I)


def section_items(text: str, title: str) -> list[str]:
	match = re.search(rf'^## {re.escape(title)}\s*\n(.*?)(?=^## |\Z)', text, re.M | re.S)
	if not match:
		return []
	return [line.strip()[2:].strip() for line in match.group(1).splitlines() if line.strip().startswith('- ')]


def real_blockers(text: str) -> list[str]:
	return [item for item in section_items(text, BLOCKER_SECTION) if not NO_BLOCKER.match(item)]


def previous_standup(member: str, today: datetime.date) -> pathlib.Path | None:
	# File names start with the ISO date, so name order is date order.
	earlier = [p for p in STANDUP_DIR.glob(f'*_{member}.md') if p.name[:10] < today.isoformat()]
	return max(earlier, key=lambda p: p.name) if earlier else None


def print_items(title: str, items: list[str], empty: str = '无') -> None:
	print(title)
	for item in items or [empty]:
		print(f'  - {item}')


def print_context(member: str) -> None:
	today = datetime.date.today()
	today_file = standup_file(member, today)
	print(f'站会 · {today} · {member}')
	if today_file.exists():
		print(f'今天已提交：{today_file.relative_to(ROOT).as_posix()}（再次提交 = 更新这份报告）')
	print_items('未完成的 PRD 与任务：', open_work(member))
	previous = previous_standup(member, today)
	current_prds = assigned_prd_paths(member)
	if previous is None:
		print_items('新分配的 PRD（首次站会，全部列出）：', current_prds)
		return
	text = previous.read_text(encoding='utf-8')
	print(f'上次站会：{previous.name[:10]}')
	known_prds = set(section_items(text, PRD_SECTION))
	print_items('上次站会后新分配的 PRD：', [p for p in current_prds if p not in known_prds])
	print_items('上次站会后不再由你负责的 PRD：', [p for p in known_prds if p not in current_prds])
	print_items('上次的"今天计划"（确认是否完成）：', section_items(text, PLAN_SECTION))
	print_items('上次的 Blockers（确认是否解决）：', real_blockers(text))


def print_summary(day: datetime.date, members: set[str]) -> None:
	print(f'站会汇总 · {day}')
	for member in sorted(members):
		path = standup_file(member, day)
		if not path.exists():
			print(f'  ⬜ {member}：未提交')
			continue
		blockers = real_blockers(path.read_text(encoding='utf-8'))
		print(f'  ✅ {member}：' + ('；'.join(f'Blocker: {b}' for b in blockers) if blockers else '无 Blocker'))


def main() -> int:
	sys.stdout.reconfigure(encoding='utf-8')
	parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
	parser.add_argument('--context', action='store_true', help='reminders before submitting a standup')
	parser.add_argument('--summary', action='store_true', help='team summary for one day')
	parser.add_argument('--member', help=f'team-roster name (default: {MEMBER_ENV})')
	parser.add_argument('--date', type=datetime.date.fromisoformat, default=datetime.date.today(), help='summary date, YYYY-MM-DD')
	args = parser.parse_args()
	members = roster_names()
	if args.summary:
		print_summary(args.date, members)
		return 0
	if not args.context:
		parser.print_help()
		return 1
	name = args.member or os.environ.get(MEMBER_ENV, '')
	member = resolve_member(name, members) if name else None
	if member is None:
		print(f'成员 "{name}" 不在团队名册中；请设置 {MEMBER_ENV}（work-log-rules.md WL-1）或传 --member', file=sys.stderr)
		return 1
	print_context(member)
	return 0


if __name__ == '__main__':
	sys.exit(main())
