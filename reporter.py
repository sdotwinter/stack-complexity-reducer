import json

def print_scan(scan, score, plan, as_json=False):
    payload = {'scan': scan, 'score': score, 'plan': plan}
    if as_json:
        print(json.dumps(payload, indent=2)); return
    print(f"Complexity score: {score['score']} ({score['level']})")
    print(f"Frameworks: {', '.join(scan['frameworks']) or '(none)'}")
    print(f"Build tools: {', '.join(scan['build_tools']) or '(none)'}")
    print(f"Runtimes: {', '.join(scan['runtimes']) or '(none)'}")
    print('\nSimplification plan:')
    for i, s in enumerate(plan, start=1):
        print(f"{i}. {s}")
