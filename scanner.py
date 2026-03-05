import json
from pathlib import Path

def scan_project(root: Path):
    findings = {"frameworks": [], "build_tools": [], "runtimes": [], "signals": []}
    pkg = root / 'package.json'
    req = root / 'requirements.txt'

    if pkg.exists():
        data = json.loads(pkg.read_text(encoding='utf-8'))
        deps = {**data.get('dependencies', {}), **data.get('devDependencies', {})}
        keys = set(deps.keys())
        if 'react' in keys: findings['frameworks'].append('react')
        if 'next' in keys or 'next.js' in keys: findings['frameworks'].append('next')
        if 'vue' in keys: findings['frameworks'].append('vue')
        for t in ['webpack', 'vite', 'rollup', 'parcel', 'esbuild']:
            if t in keys: findings['build_tools'].append(t)
        findings['runtimes'].append('node')
        findings['signals'].append(f"js_dep_count={len(keys)}")

    if req.exists():
        pkgs = [l.strip().split('==')[0] for l in req.read_text(encoding='utf-8').splitlines() if l.strip() and not l.strip().startswith('#')]
        pset = set(pkgs)
        for f in ['django', 'flask', 'fastapi']:
            if f in pset: findings['frameworks'].append(f)
        findings['runtimes'].append('python')
        findings['signals'].append(f"py_dep_count={len(pset)}")

    findings['frameworks'] = sorted(set(findings['frameworks']))
    findings['build_tools'] = sorted(set(findings['build_tools']))
    findings['runtimes'] = sorted(set(findings['runtimes']))
    return findings
