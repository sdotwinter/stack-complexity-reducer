import argparse, json
from pathlib import Path
from analyzer import analyze_stack
from recommender import suggest_simplifications

def run(argv=None):
    p = argparse.ArgumentParser(prog='stack-complexity-reducer')
    sub = p.add_subparsers(dest='cmd', required=True)

    a = sub.add_parser('analyze')
    a.add_argument('--stack', required=True, help='JSON file with stack components')

    r = sub.add_parser('recommend')
    r.add_argument('--analysis', required=True, help='Analysis JSON from analyze')
    r.add_argument('--team-size', type=int, default=5)
    r.add_argument('--traffic', default='low', choices=['low', 'medium', 'high'])

    e = sub.add_parser('export')
    e.add_argument('--analysis', required=True)
    e.add_argument('--recommendations', required=True)
    e.add_argument('--output', required=True)

    args = p.parse_args(argv)

    if args.cmd == 'analyze':
        data = json.loads(Path(args.stack).read_text(encoding='utf-8'))
        result = analyze_stack(data.get('components', []))
        print(json.dumps(result, indent=2))
        return 0

    if args.cmd == 'recommend':
        analysis = json.loads(Path(args.analysis).read_text(encoding='utf-8'))
        recs = suggest_simplifications(analysis, args.team_size, args.traffic)
        print(json.dumps({'recommendations': recs}, indent=2))
        return 0

    if args.cmd == 'export':
        analysis = json.loads(Path(args.analysis).read_text(encoding='utf-8'))
        recs = json.loads(Path(args.recommendations).read_text(encoding='utf-8'))
        out = {'analysis': analysis, **recs}
        Path(args.output).write_text(json.dumps(out, indent=2), encoding='utf-8')
        print(f"Exported to {args.output}")
        return 0

    return 0
