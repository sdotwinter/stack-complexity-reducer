def simplification_plan(scan, score):
    steps = []
    if score['build_tool_count'] > 1:
        steps.append('Consolidate build tooling to one primary bundler to reduce maintenance overhead.')
    if score['framework_count'] > 1:
        steps.append('Standardize on one primary framework for new features to reduce cognitive load.')
    if score['runtime_count'] > 1:
        steps.append('Reduce cross-runtime coupling; isolate services or migrate one utility layer.')
    if not steps:
        steps.append('Current stack is relatively lean. Focus on keeping dependencies trimmed.')

    steps.append('Audit and remove unused dependencies monthly.')
    return steps
