from typing import Dict, List

RECOMMENDATIONS = {
    'frontend': {
        'react': 'Consider Svelte or Preact for simpler bundles',
        'angular': 'Migration to React or Vue reduces learning curve',
        'vanilla': 'Good baseline - only add framework if needed'
    },
    'backend': {
        'rails': 'Django or Express offers similar productivity with less weight',
        'java': 'Consider Spring Boot or drop to Go/Python for simpler deploys',
        'node': 'Good choice - keep streamlined'
    },
    'database': {
        'mongodb': 'PostgreSQL JSONB often sufficient with less operational overhead',
        'dynamodb': 'Consider SQLite for small apps, PostgreSQL for scale'
    },
    'infra': {
        'kubernetes': 'Use managed containers (ECS, Cloud Run) for smaller teams',
        'aws': 'Consolidate to Vercel/Netlify + single DB for MVPs'
    }
}

def suggest_simplifications(analysis: Dict, team_size: int = 5, traffic: str = 'low') -> List[str]:
    recs = []
    by_cat = analysis.get('by_category', {})
    total = analysis.get('total_score', 0)

    if total > 10:
        recs.append('Current stack is complex - consider consolidating services')
    if team_size < 5 and by_cat.get('infra', 0) > 2:
        recs.append('Small team: migrate infra to serverless or managed services')
    if by_cat.get('frontend', 0) > 3:
        recs.append('Reduce frontend complexity: stick to one framework, remove state mgmt overhead')

    for cat, techs in RECOMMENDATIONS.items():
        if cat in by_cat:
            for tech, msg in techs.items():
                if tech in str(by_cat).lower():
                    recs.append(msg)
    return recs[:5]
