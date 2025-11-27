# Weekly Reports System

Système de génération de rapports hebdomadaires avec Cumulative Flow Diagram (CFD) pour le suivi des tâches du projet.

## Vue d'ensemble

Le système permet de :

- Générer des CFD (Cumulative Flow Diagrams) pour visualiser le flux de travail
- Créer des rapports hebdomadaires markdown avec statistiques
- Suivre les métriques Lean/Kanban (throughput, WIP, lead time)

## Structure des fichiers

```text
.tasks/reports/                     # Rapports générés
├── YYYY-WNN-recap.md               # Rapport markdown
├── YYYY-WNN-cfd.png                # Image CFD
└── YYYY-WNN-data.json              # Données brutes

scripts/reports/                    # Module Python
├── __init__.py
├── cfd.py                          # Génération CFD
├── weekly_report.py                # Génération rapports
├── generate_cfd.py                 # CLI
└── tests/                          # Tests (34)

.claude/skills/weekly-reports/      # Skill Claude
├── SKILL.md
└── workflows/
    ├── report-create.md
    └── report-update.md
```

## Cumulative Flow Diagram (CFD)

Le CFD est un graphique d'aires empilées montrant l'évolution des tâches par état.

### Lecture du CFD

| Zone | Couleur | Métrique | Interprétation |
|------|---------|----------|----------------|
| Terminé | Vert | Throughput | Pente = vitesse de livraison |
| En cours | Orange | WIP | Épaisseur = travail en cours |
| À faire | Bleu | Backlog | Hauteur = tâches restantes |

### Métriques clés

- **Throughput** : Nombre de tâches terminées par unité de temps (pente verte)
- **WIP (Work In Progress)** : Tâches en cours simultanément (épaisseur orange)
- **Lead Time** : Temps moyen entre début et fin d'une tâche (distance horizontale)
- **Little's Law** : Lead Time = WIP / Throughput

## Utilisation

### Génération CLI

```bash
# Générer un CFD depuis un fichier JSON
uv run --with matplotlib --with numpy scripts/reports/generate_cfd.py \
  --data .tasks/reports/2025-W48-data.json \
  --output .tasks/reports/

# Afficher les métriques
uv run --with matplotlib --with numpy scripts/reports/generate_cfd.py \
  --data .tasks/reports/2025-W48-data.json \
  --metrics

# Mode interactif (afficher le graphique)
uv run --with matplotlib --with numpy scripts/reports/generate_cfd.py \
  --data .tasks/reports/2025-W48-data.json \
  --show
```

### Via le skill Claude

```text
# Créer un rapport
User: Crée un rapport pour cette semaine
Claude: [Exécute workflow report-create]

# Mettre à jour un rapport
User: Ajoute les données de jeudi au rapport
Claude: [Exécute workflow report-update]
```

## Format des données JSON

```json
{
  "week": "2025-W48",
  "title": "Cumulative Flow Diagram - Semaine 48 (25-27 nov 2025)",
  "data": [
    {
      "date": "2025-11-24",
      "backlog": 29,
      "in_progress": 0,
      "done": 12,
      "comment": "État initial (dimanche soir)"
    },
    {
      "date": "2025-11-25",
      "backlog": 22,
      "in_progress": 0,
      "done": 32,
      "comment": "Lundi soir - 20 tâches terminées"
    }
  ],
  "summary": {
    "tasks_completed": 28,
    "tasks_created": 19,
    "avg_wip": 0.5,
    "throughput": 9.3
  }
}
```

### Champs obligatoires

| Champ | Type | Description |
|-------|------|-------------|
| `date` | string | Date ISO (YYYY-MM-DD) |
| `backlog` | int | Tâches à faire |
| `in_progress` | int | Tâches en cours |
| `done` | int | Tâches terminées (cumulatif) |

### Champs optionnels

| Champ | Type | Description |
|-------|------|-------------|
| `comment` | string | Note pour ce point de données |

## API Python

### Classes principales

```python
from scripts.reports.cfd import DayData, CFDConfig, generate_cfd, calculate_metrics

# Créer des données
data = [
    DayData(date=datetime(2025, 11, 25), backlog=10, in_progress=2, done=5),
    DayData(date=datetime(2025, 11, 26), backlog=8, in_progress=1, done=8),
]

# Générer le CFD
config = CFDConfig(title="Mon CFD", dpi=150)
generate_cfd(data, config=config, output_path=Path("cfd.png"))

# Calculer les métriques
metrics = calculate_metrics(data)
print(f"Throughput: {metrics['throughput']} tâches/jour")
```

### Génération de rapports markdown

```python
from scripts.reports.weekly_report import WeeklyReport, TaskSummary, generate_weekly_report

report = WeeklyReport(
    week="2025-W48",
    start_date=datetime(2025, 11, 25),
    end_date=datetime(2025, 11, 27),
    tasks_completed=[
        TaskSummary("CNT-001", "Ma tâche", "CNT", "haute", "terminé")
    ],
    backlog_count=17,
)

generate_weekly_report(report, Path(".tasks/reports/2025-W48-recap.md"))
```

## Tests

```bash
# Lancer les tests du module reports
uv run --with pytest --with matplotlib --with numpy pytest scripts/reports/tests/ -v

# Tous les tests du projet
uv run --with pytest pytest
```

**Couverture :** 34 tests (19 CFD + 15 weekly_report)

## Dépendances

| Package | Version | Usage |
|---------|---------|-------|
| matplotlib | >=3.8.0 | Génération graphiques |
| numpy | >=1.26.0 | Calculs numériques |
| pytest | >=8.0.0 | Tests (dev) |

Installation :

```bash
uv pip install -e ".[reports]"
```

## Bonnes pratiques

1. **Fréquence des points de données** : Un point par jour travaillé minimum
2. **Moment de capture** : Fin de journée pour cohérence
3. **Commentaires** : Ajouter contexte pour les variations importantes
4. **Archivage** : Conserver les rapports pour analyse rétrospective

## Références

- [Little's Law](https://en.wikipedia.org/wiki/Little%27s_law)
- [Cumulative Flow Diagram](https://www.atlassian.com/agile/kanban/cumulative-flow-diagram)
- [Kanban Metrics](https://kanbanize.com/kanban-resources/kanban-analytics)
