from dataclasses import dataclass
from typing import Dict, List

@dataclass
class Component:
    name: str
    category: str  # frontend, backend, database, infra, tooling
    weight: int = 1

COMPLEXITY_WEIGHTS = {
    'frontend': {'react': 3, 'vue': 2, 'angular': 4, 'svelte': 1, 'vanilla': 0},
    'backend': {'node': 2, 'python': 1, 'go': 1, 'rust': 3, 'java': 4, 'rails': 3, 'django': 2},
    'database': {'postgresql': 1, 'mysql': 1, 'mongodb': 2, 'redis': 1, 'dynamodb': 2, 'graphql': 2},
    'infra': {'aws': 3, 'gcp': 3, 'azure': 3, 'kubernetes': 4, 'docker': 2, 'serverless': 1},
    'tooling': {'webpack': 2, 'vite': 1, 'terraform': 3, 'cicd': 2}
}

def analyze_stack(components: List[Dict]) -> Dict:
    total = 0
    by_cat = {}
    for c in components:
        cat = c.get('category', 'frontend')
        tech = c.get('technology', '').lower()
        weight = COMPLEXITY_WEIGHTS.get(cat, {}).get(tech, 1)
        total += weight
        by_cat[cat] = by_cat.get(cat, 0) + weight
    return {
        'total_score': total,
        'by_category': by_cat,
        'complexity_level': 'low' if total < 5 else 'medium' if total < 10 else 'high'
    }
