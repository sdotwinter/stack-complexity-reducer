import argparse
from pathlib import Path
from scanner import scan_project
from scorer import score_complexity
from planner import simplification_plan
from reporter import print_scan

def run(argv=None):
    p=argparse.ArgumentParser(prog='stack-complexity-reducer', description='Scan stack complexity and suggest simplifications.')
    sub=p.add_subparsers(dest='cmd', required=True)

    for name in ['scan', 'score', 'simplify-plan']:
        c=sub.add_parser(name)
        c.add_argument('path', nargs='?', default='.')
        c.add_argument('--json', action='store_true')

    args=p.parse_args(argv)
    root=Path(args.path).resolve()
    scan=scan_project(root)
    score=score_complexity(scan)
    plan=simplification_plan(scan, score)

    if args.cmd == 'scan':
        print_scan(scan, {'score': 0, 'level': 'n/a', 'framework_count': len(scan['frameworks']), 'build_tool_count': len(scan['build_tools']), 'runtime_count': len(scan['runtimes'])}, [], as_json=args.json)
    elif args.cmd == 'score':
        print_scan(scan, score, [], as_json=args.json)
    else:
        print_scan(scan, score, plan, as_json=args.json)
    return 0
