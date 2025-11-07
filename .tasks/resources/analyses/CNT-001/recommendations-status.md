# Suivi des Recommandations - CNT-001

**Analyse:** CNT-001 - Audit LinkedIn
**Date création:** 2025-10-29
**Date clarifications:** 2025-11-05
**Total recommandations:** 19
**Statut:** 🔄 En cours de traitement

Ce fichier permet de suivre l'évolution de chaque recommandation issue de l'audit. Lorsqu'une recommandation est transformée en tâche via `/task-from-analysis`, elle est marquée comme "task created" avec l'ID de la tâche créée.

**Mise à jour 2025-11-05:** 3 recommandations rejetées suite aux clarifications utilisateur.

---

## Statistiques

| Statut | Nombre | Pourcentage |
|--------|--------|-------------|
| ⏳ Pending | 8 | 42% |
| 🔄 Task created | 8 | 42% |
| ❌ Rejetée | 3 | 16% |
| ✅ Completed | 0 | 0% |
| **TOTAL** | **19** | **100%** |

---

## 🔴🔴 Priorité TRÈS HAUTE (0/0 items - Toutes clarifiées)

**Note:** Les 3 "incohérences critiques" ont été clarifiées avec l'utilisateur le 2025-11-05. Voir section "Clarifications utilisateur" dans audit-report.md.

- [x] **~~R01 - Ajouter position @Home~~** → **REJETÉE (2025-11-05)**
  - Catégorie: Position manquante
  - Source: [recommendations.md](./recommendations.md#r01---corriger-lécart-critique-sur-upwiser)
  - Référence CV: N/A
  - **Raison rejet:** @Home = période de chômage actuelle. Il est normal et approprié de ne pas inclure une période de chômage dans le CV.
  - Date ajout: 2025-11-05
  - Date rejet: 2025-11-05
  - Statut: ❌ Rejetée

- [x] **~~R02 - Corriger dates Upwiser~~** → **REJETÉE (2025-11-05)**
  - Catégorie: Date incohérence
  - Source: Audit comparatif
  - Référence CV: [src/cv.typ:122](../../../src/cv.typ#L122)
  - **Raison rejet:** Pas d'incohérence. CV affiche fin activité plein temps (01/2021), LinkedIn affiche fermeture administrative (11/2024). Les deux sont corrects selon le contexte.
  - Date ajout: 2025-11-05
  - Date rejet: 2025-11-05
  - Statut: ❌ Rejetée

- [x] **~~R03 - Harmoniser dates PALO IT CTO~~** → **REJETÉE (2025-11-05)**
  - Catégorie: Date incohérence
  - Source: Audit comparatif
  - Référence CV: [src/cv.typ:107](../../../src/cv.typ#L107)
  - **Raison rejet:** CV a la bonne date (08/2025), LinkedIn est erroné (10/2025). Pas de correction nécessaire.
  - Date ajout: 2025-11-05
  - Date rejet: 2025-11-05
  - Statut: ❌ Rejetée

---

## 🔴 Priorité HAUTE (0/8 items pending - 2 rejetées)

**Note:** Les anciennes tâches CNT-002 (Upwiser) et CNT-003 (PALO IT CTO) créées avant les clarifications peuvent être fermées/rejetées.

- [x] **R04 - Corriger les dates de Boonty**
  - Catégorie: Date incohérence
  - Source: [recommendations.md](./recommendations.md#r03---corriger-les-dates-de-boonty)
  - Référence CV: [src/cv.typ:162](../../../src/cv.typ#L162)
  - Trigramme suggéré: CNT
  - Date ajout: 2025-10-29
  - Tâche créée: [CNT-004](../../tasks/CNT-004-corriger-dates-boonty.md)
  - Date création tâche: 2025-10-29
  - Statut: 🔄 Task created

- [x] **R04 - Corriger les dates de début Freelance**
  - Catégorie: Date incohérence
  - Source: [recommendations.md](./recommendations.md#r04---corriger-les-dates-de-début-freelance)
  - Référence CV: [src/cv.typ:169](../../../src/cv.typ#L169)
  - Trigramme suggéré: CNT
  - Date ajout: 2025-10-29
  - Tâche créée: [CNT-005](../../tasks/CNT-005-corriger-dates-debut-freelance.md)
  - Date création tâche: 2025-10-29
  - Statut: 🔄 Task created

- [x] **R05 - Ajouter les certifications manquantes**
  - Catégorie: Certification manquante
  - Source: [recommendations.md](./recommendations.md#r05---ajouter-les-certifications-manquantes)
  - Référence CV: [src/cv.typ:220-250](../../../src/cv.typ#L220-L250)
  - Trigramme suggéré: CNT
  - Date ajout: 2025-10-29
  - Tâche créée: [CNT-006](../../tasks/CNT-006-ajouter-certifications-manquantes.md)
  - Date création tâche: 2025-10-29
  - Statut: 🔄 Task created

- [x] **R06 - Corriger la date SAFe**
  - Catégorie: Certification incohérence
  - Source: [recommendations.md](./recommendations.md#r06---corriger-la-date-safe)
  - Référence CV: [src/cv.typ:248](../../../src/cv.typ#L248)
  - Trigramme suggéré: CNT
  - Date ajout: 2025-10-29
  - Tâche créée: [CNT-007](../../tasks/CNT-007-corriger-date-safe.md)
  - Date création tâche: 2025-10-29
  - Statut: 🔄 Task created

- [x] **R07 - Ajouter l'expérience i-BP**
  - Catégorie: Expérience manquante
  - Source: [recommendations.md](./recommendations.md#r07---ajouter-lexpérience-i-bp)
  - Référence CV: Insertion après ligne 135
  - Trigramme suggéré: CNT
  - Date ajout: 2025-10-29
  - Tâche créée: [CNT-008](../../tasks/CNT-008-ajouter-experience-ibp.md)
  - Date création tâche: 2025-10-29
  - Statut: 🔄 Task created

- [x] **R08 - Ajouter l'expérience DEKRA**
  - Catégorie: Expérience manquante
  - Source: [recommendations.md](./recommendations.md#r08---ajouter-lexpérience-dekra)
  - Référence CV: Insertion après ligne 135
  - Trigramme suggéré: CNT
  - Date ajout: 2025-10-29
  - Tâche créée: [CNT-009](../../tasks/CNT-009-ajouter-experience-dekra.md)
  - Date création tâche: 2025-10-29
  - Statut: 🔄 Task created

- [x] **R09 - Ajouter section Bénévolat**
  - Catégorie: Section manquante
  - Source: [recommendations.md](./recommendations.md#r09---ajouter-section-bénévolat)
  - Référence CV: Insertion après ligne 250
  - Trigramme suggéré: CNT
  - Date ajout: 2025-10-29
  - Tâche créée: [CNT-010](../../tasks/CNT-010-ajouter-section-benevolat.md)
  - Date création tâche: 2025-10-29
  - Statut: 🔄 Task created

- [x] **R10 - Corriger écarts mineurs de dates (Cdiscount)**
  - Catégorie: Date incohérence
  - Source: [recommendations.md](./recommendations.md#r10---corriger-écarts-mineurs-de-dates-cdiscount)
  - Référence CV: [src/cv.typ:139](../../../src/cv.typ#L139)
  - Trigramme suggéré: CNT
  - Date ajout: 2025-10-29
  - Tâche créée: [CNT-011](../../tasks/CNT-011-corriger-ecarts-mineurs-cdiscount.md)
  - Date création tâche: 2025-10-29
  - Statut: 🔄 Task created

- [x] **R11 - Corriger écarts mineurs de dates (Cast)**
  - Catégorie: Date incohérence
  - Source: [recommendations.md](./recommendations.md#r11---corriger-écarts-mineurs-de-dates-cast)
  - Référence CV: [src/cv.typ:150](../../../src/cv.typ#L150)
  - Trigramme suggéré: CNT
  - Date ajout: 2025-10-29
  - Tâche créée: [CNT-012](../../tasks/CNT-012-corriger-ecarts-mineurs-cast.md)
  - Date création tâche: 2025-10-29
  - Statut: 🔄 Task created

---

## 🟡 Priorité MOYENNE (5/5 items pending)

- [ ] **R12 - Ajouter la langue Espagnol**
  - Catégorie: Langue manquante
  - Source: [recommendations.md](./recommendations.md#r12---ajouter-la-langue-espagnol)
  - Référence CV: [src/cv.typ:66](../../../src/cv.typ#L66)
  - Trigramme suggéré: CNT
  - Date ajout: 2025-10-29
  - Tâche créée: -
  - Statut: ⏳ Pending

- [ ] **R13 - Enrichir la description de Boonty**
  - Catégorie: Description à enrichir
  - Source: [recommendations.md](./recommendations.md#r13---enrichir-la-description-de-boonty)
  - Référence CV: [src/cv.typ:160-165](../../../src/cv.typ#L160-L165)
  - Trigramme suggéré: CNT
  - Date ajout: 2025-10-29
  - Tâche créée: -
  - Statut: ⏳ Pending

- [ ] **R14 - Ajouter le site web personnel**
  - Catégorie: Site web absent
  - Source: [recommendations.md](./recommendations.md#r14---ajouter-le-site-web-personnel)
  - Référence CV: [src/cv.typ:15](../../../src/cv.typ#L15)
  - Trigramme suggéré: CNT
  - Date ajout: 2025-10-29
  - Tâche créée: -
  - Statut: ⏳ Pending

- [ ] **R15 - Clarifier l'institution du DEA**
  - Catégorie: Éducation à clarifier
  - Source: [recommendations.md](./recommendations.md#r15---clarifier-linstitution-du-dea)
  - Référence CV: [src/cv.typ:176-194](../../../src/cv.typ#L176-L194)
  - Trigramme suggéré: CNT
  - Date ajout: 2025-10-29
  - Tâche créée: -
  - Statut: ⏳ Pending

- [ ] **R16 - Ajouter ITS Group**
  - Catégorie: Expérience manquante
  - Source: [recommendations.md](./recommendations.md#r16---ajouter-its-group)
  - Référence CV: Insertion optionnelle après Cdiscount
  - Trigramme suggéré: CNT
  - Date ajout: 2025-10-29
  - Tâche créée: -
  - Statut: ⏳ Pending

---

## 🟢 Priorité BASSE (3/3 items pending)

- [ ] **R17 - Ajouter Ruby Bordeaux au bénévolat**
  - Catégorie: Bénévolat absent
  - Source: [recommendations.md](./recommendations.md#r17---ajouter-ruby-bordeaux-au-bénévolat)
  - Référence CV: Nouvelle section bénévolat
  - Trigramme suggéré: CNT
  - Date ajout: 2025-10-29
  - Tâche créée: -
  - Statut: ⏳ Pending

- [ ] **R18 - Ajouter Startup Weekend Bordeaux**
  - Catégorie: Bénévolat absent
  - Source: [recommendations.md](./recommendations.md#r18---ajouter-startup-weekend-bordeaux)
  - Référence CV: Nouvelle section bénévolat
  - Trigramme suggéré: CNT
  - Date ajout: 2025-10-29
  - Tâche créée: -
  - Statut: ⏳ Pending

- [ ] **R19 - Ajouter site "Le monde des parents"**
  - Catégorie: Site web absent
  - Source: [recommendations.md](./recommendations.md#r19---ajouter-site-le-monde-des-parents)
  - Référence CV: [src/cv.typ:15](../../../src/cv.typ#L15)
  - Trigramme suggéré: CNT
  - Date ajout: 2025-10-29
  - Tâche créée: -
  - Statut: ⏳ Pending

---

## Workflow de Traitement

### Comment marquer une recommandation comme traitée

Lorsqu'une recommandation est transformée en tâche:

1. Cocher la checkbox [ ] → [x]
2. Remplacer "Tâche créée: -" par "Tâche créée: CNT-XXX"
3. Remplacer "Statut: ⏳ Pending" par "Statut: 🔄 Task created"
4. Mettre à jour les statistiques en haut du fichier

**Exemple:**

```markdown
- [x] **R05 - Ajouter les certifications manquantes**
  - Catégorie: Certification manquante
  - Source: [recommendations.md](./recommendations.md#r05---ajouter-les-certifications-manquantes)
  - Référence CV: [src/cv.typ:220-250](../../../src/cv.typ#L220-L250)
  - Trigramme suggéré: CNT
  - Date ajout: 2025-10-29
  - Tâche créée: CNT-002
  - Statut: 🔄 Task created
```

### Quand marquer une recommandation comme complétée

Lorsque la tâche associée est terminée et le CV mis à jour:

1. Remplacer "Statut: 🔄 Task created" par "Statut: ✅ Completed"
2. Ajouter "Date complétion: YYYY-MM-DD"
3. Mettre à jour les statistiques

---

## Commandes Utiles

```bash
# Transformer des recommandations en tâches
/task-from-analysis

# Voir le statut de l'analyse
cat .tasks/ANALYSES.md

# Voir toutes les recommandations
cat .tasks/resources/analyses/CNT-001/recommendations.md
```
