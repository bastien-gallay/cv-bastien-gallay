# Backlog d'Idées

Ce fichier collecte les idées d'améliorations futures issues des tâches terminées. Ces idées peuvent être transformées en tâches concrètes via `/task-from-idea`.

---

## Contenu (CNT)

- [ ] Améliorer la traçabilité des clarifications historiques dans le système de tâches (source: CNT-004, 2025-11-16)

---

## Template (TPL)

*Aucune idée pour l'instant*

---

## Qualité (QUA)

*Aucune idée pour l'instant*

---

## Pipeline (PIP)

- [ ] Dans les commandes de gestion des tâches, privilégier des questionnaires posant plusieurs questions numérotées à la suite plutôt que des questions uniques successives
- [ ] `/task-next` pourrait bénéficier d'un cache pour accélérer la recherche de la prochaine tâche à faire (Spike, expérimentation nécessaire)

---

## Layout (LAY)

*Aucune idée pour l'instant*

---

## Documentation (DOC)

- [ ] Suggérer des réponses automatiques aux questions de collecte d'informations lors de la complétion des tâches (basées sur le contenu de la tâche et l'historique Git) (source: DOC-001, 2025-10-28)

---

## Infrastructure (INF)

- [ ] Pérenniser le script Python de calcul des priorités (scripts/priority_weight.py) utilisé dans /task-next et l'améliorer pour le futur (source: CNT-002, 2025-11-16)

---

## Utilisation

### Ajouter une idée

Les idées sont ajoutées automatiquement depuis `/task-complete` lorsque la section "Améliorations futures" est remplie.

### Créer une tâche depuis une idée

Utilisez `/task-from-idea` pour transformer une idée en tâche concrète. L'idée sera supprimée du backlog une fois transformée.

### Format

Chaque idée suit le format :

```markdown
- [ ] {Description de l'idée} (source: {ID-TACHE}, {DATE})
```
