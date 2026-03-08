# Stack Complexity Reducer

[![Sponsor](https://img.shields.io/badge/Sponsor-GitHub%20Sponsors-ea4aaa?logo=githubsponsors)](https://github.com/sponsors/sdotwinter)

A planner tool that maps web app architecture complexity and recommends a simpler, maintainable stack for small teams.

## Usage
```bash
python3 main.py analyze --stack samples/stack.json
python3 main.py recommend --analysis samples/analysis.json --team-size 3
python3 main.py export --analysis samples/analysis.json --recommendations samples/recs.json --output out.json
```

## Sample Stack
```json
{"components": [{"category": "frontend", "technology": "react"}, {"category": "backend", "technology": "node"}, {"category": "database", "technology": "postgresql"}]}
```

## Sponsorware
Personal use is free. Team templates and advanced recommendation packs require sponsorship.
Suggested tiers: **$7 / $14 / $50**.
