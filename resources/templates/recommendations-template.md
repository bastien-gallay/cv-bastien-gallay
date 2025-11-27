# Suivi des Recommandations - [TASK-ID]

**Analyse:** [TASK-ID] - [Nom de l'analyse]
**Date création:** [YYYY-MM-DD]
**Total recommandations:** [N]
**Statut:** ⏳ En attente de traitement

Ce fichier permet de suivre l'évolution de chaque recommandation issue de l'audit. Lorsqu'une recommandation est transformée en tâche via `/task-from-analysis`, elle est marquée comme "task created" avec l'ID de la tâche créée.

---

## Statistiques

| Statut | Nombre | Pourcentage |
|--------|--------|-------------|
| ⏳ Pending | [N] | 100% |
| 🔄 Task created | 0 | 0% |
| ✅ Completed | 0 | 0% |

---

## 🔴🔴 Priorité TRÈS HAUTE ([N/N] items pending)

- [ ] **R01 - [Titre de la recommandation]**
  - Catégorie: [Type: Date incohérence, Expérience manquante, etc.]
  - Source: [recommendations.md](./recommendations.md#r01-[slug])
  - Référence CV: [src/cv.typ:XXX](../../../src/cv.typ#LXXX)
  - Trigramme suggéré: [CNT/TPL/LAY/etc.]
  - Date ajout: [YYYY-MM-DD]
  - Tâche créée: -
  - Statut: ⏳ Pending

---

## 🔴 Priorité HAUTE ([N/N] items pending)

- [ ] **R02 - [Titre de la recommandation]**
  - Catégorie: [Type]
  - Source: [recommendations.md](./recommendations.md#r02-[slug])
  - Référence CV: [src/cv.typ:XXX](../../../src/cv.typ#LXXX)
  - Trigramme suggéré: [Trigramme]
  - Date ajout: [YYYY-MM-DD]
  - Tâche créée: -
  - Statut: ⏳ Pending

[Répéter pour chaque recommandation haute priorité]

---

## 🟡 Priorité MOYENNE ([N/N] items pending)

- [ ] **R[N] - [Titre de la recommandation]**
  - Catégorie: [Type]
  - Source: [recommendations.md](./recommendations.md#r[n]-[slug])
  - Référence CV: [src/cv.typ:XXX](../../../src/cv.typ#LXXX)
  - Trigramme suggéré: [Trigramme]
  - Date ajout: [YYYY-MM-DD]
  - Tâche créée: -
  - Statut: ⏳ Pending

[Répéter pour chaque recommandation moyenne priorité]

---

## 🟢 Priorité BASSE ([N/N] items pending)

- [ ] **R[N] - [Titre de la recommandation]**
  - Catégorie: [Type]
  - Source: [recommendations.md](./recommendations.md#r[n]-[slug])
  - Référence CV: [src/cv.typ:XXX](../../../src/cv.typ#LXXX)
  - Trigramme suggéré: [Trigramme]
  - Date ajout: [YYYY-MM-DD]
  - Tâche créée: -
  - Statut: ⏳ Pending

[Répéter pour chaque recommandation basse priorité]

---

## Workflow de Traitement

### Comment marquer une recommandation comme traitée

Lorsqu'une recommandation est transformée en tâche:

1. Cocher la checkbox [ ] → [x]
2. Remplacer "Tâche créée: -" par "Tâche créée: [TASK-ID]"
3. Remplacer "Statut: ⏳ Pending" par "Statut: 🔄 Task created"
4. Mettre à jour les statistiques en haut du fichier

**Exemple:**

```markdown
- [x] **R05 - Ajouter les certifications manquantes**
  - Catégorie: Certification manquante
  - Source: [recommendations.md](./recommendations.md#r05-ajouter-les-certifications-manquantes)
  - Référence CV: [src/cv.typ:220-250](../../../src/cv.typ#L220-L250)
  - Trigramme suggéré: CNT
  - Date ajout: 2025-10-29
  - Tâche créée: CNT-002
  - Statut: 🔄 Task created
```

### Quand marquer une recommandation comme complétée

Lorsque la tâche associée est terminée et le CV mis à jour:

1. Remplacer "Statut: 🔄 Task created" par "Statut: ✅ Completed"
2. Ajouter "Date complétion: [YYYY-MM-DD]"
3. Mettre à jour les statistiques

---

## Commandes Utiles

```bash
# Transformer des recommandations en tâches
/task-from-analysis

# Voir le statut de l'analyse
cat .tasks/ANALYSES.md

# Voir toutes les recommandations
cat .tasks/resources/analyses/[TASK-ID]/recommendations.md
```

---

## Guide d'Utilisation de ce Template

### Création d'un Fichier de Suivi

1. **Copier ce template** dans `analyses/[TASK-ID]/recommendations-status.md`
2. **Remplacer les placeholders:**
   - `[TASK-ID]` → ID de l'analyse (ex: CNT-001)
   - `[Nom de l'analyse]` → Nom descriptif (ex: Audit LinkedIn)
   - `[N]` → Nombre total de recommandations
   - `[YYYY-MM-DD]` → Date de création

3. **Créer une entrée par recommandation:**
   - Copier le bloc de recommandation template
   - Remplir tous les champs
   - Organiser par priorité (Très Haute → Basse)
   - Numéroter séquentiellement (R01, R02, etc.)

### Catégories Standards

- Date incohérence
- Expérience manquante
- Certification manquante / incohérence
- Langue manquante
- Section manquante
- Description à enrichir
- Information à clarifier
- Site web absent

### Trigrammes Standards

- **CNT** - Content (contenu du CV)
- **TPL** - Template (structure, format)
- **LAY** - Layout (mise en page, design)
- **QUA** - Quality (vérification, validation)

### Mise à Jour des Statistiques

Après chaque modification, recalculer:

```markdown
Pending = Total - (Task created + Completed)
Task created = Nombre avec statut 🔄
Completed = Nombre avec statut ✅

Pourcentage = (Nombre / Total) * 100
```
