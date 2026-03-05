def score_complexity(scan):
    framework_count = len(scan.get('frameworks', []))
    build_tool_count = len(scan.get('build_tools', []))
    runtime_count = len(scan.get('runtimes', []))

    score = framework_count * 20 + build_tool_count * 18 + runtime_count * 15
    score = min(100, score)

    level = 'low'
    if score >= 70:
        level = 'high'
    elif score >= 40:
        level = 'medium'

    return {
        'score': score,
        'level': level,
        'framework_count': framework_count,
        'build_tool_count': build_tool_count,
        'runtime_count': runtime_count,
    }
