# Plan d'Action Séquentiel - Audit CNT-001

**Analyse:** CNT-001
**Date:** 2025-10-29
**Total phases:** 6

Ce plan d'action structure l'implémentation des recommandations issues de l'audit LinkedIn en phases séquentielles, du plus critique au moins urgent.

---

## Phase 1: Corrections Critiques de Dates (🔴 Immédiat)

**Objectif:** Résoudre les incohérences majeures qui affectent la crédibilité

**Temps estimé:** 30 minutes (après clarification)

**Actions:**

1. ✅ Clarifier avec l'utilisateur les dates exactes:
   - Upwiser: fin en nov. 2024 ou jan. 2021?
   - PALO IT CTO: fin en oct. 2025 ou août 2025?
   - Boonty: début en juin 2005 ou juil. 2004?
   - Freelance: début en juin 2002 ou juin 1999?

2. ✅ Mettre à jour le CV avec les dates validées

**Fichiers affectés:**

- [src/cv.typ:107](../../../src/cv.typ#L107) - PALO IT CTO
- [src/cv.typ:122](../../../src/cv.typ#L122) - Upwiser
- [src/cv.typ:162](../../../src/cv.typ#L162) - Boonty
- [src/cv.typ:169](../../../src/cv.typ#L169) - Freelance

**Recommandations concernées:** R01, R02, R03, R04

---

## Phase 2: Ajout des Certifications (🔴 Haute priorité)

**Objectif:** Compléter les qualifications importantes

**Temps estimé:** 30 minutes

**Actions:**

1. ✅ Ajouter Professional Scrum Developer (PSD-I) - 2018
2. ✅ Ajouter Scaled Professional Scrum (SPS) - 2016
3. ✅ Corriger date SAFe (2020 vs 2018)

**Fichier affecté:**

- [src/cv.typ:220-250](../../../src/cv.typ#L220-L250)

**Recommandations concernées:** R05, R06

---

## Phase 3: Ajout des Expériences Manquantes (🔴 Haute priorité)

**Objectif:** Compléter l'historique professionnel

**Temps estimé:** 1-1.5 heures

**Actions:**

1. ✅ Ajouter i-BP (avr. 2015 - sept. 2015)
2. ✅ Ajouter DEKRA (oct. 2013 - janv. 2015)
3. 🤔 Décider si ajouter ITS Group (clarification ESN)

**Fichier affecté:**

- [src/cv.typ:103-173](../../../src/cv.typ#L103-L173)

**Recommandations concernées:** R07, R08, R16

**Note:** Ces missions freelance s'inscrivent dans la période Upwiser. Décider si:

- Les lister séparément (meilleure visibilité)
- Les mentionner dans la description Upwiser
- Créer une sous-section "Missions notables"

---

## Phase 4: Création Section Bénévolat (🔴 Haute priorité)

**Objectif:** Valoriser l'engagement communautaire

**Temps estimé:** 1 heure

**Actions:**

1. ✅ Créer nouvelle section "Expérience Bénévole" après Certifications
2. ✅ Ajouter Agile Tour Bordeaux (2011-aujourd'hui)
3. ✅ Ajouter Lean Startup Bordeaux (2012-2018) - redondance avec Upwiser à gérer
4. ✅ Ajouter Collectif Quinconces (2016-2018)

**Fichier affecté:**

- [src/cv.typ](../../../src/cv.typ) - Nouvelle section après ligne 250

**Recommandations concernées:** R09, R17, R18

**Point d'attention:** Lean Startup Bordeaux est déjà mentionné dans Upwiser (ligne 132). Options:

- Créer une section bénévolat séparée avec détails
- Laisser seulement la mention dans Upwiser
- Mentionner dans les deux avec renvoi

---

## Phase 5: Enrichissements (🟡 Moyenne priorité)

**Objectif:** Améliorer la complétude du CV

**Temps estimé:** 1 heure

**Actions:**

1. ✅ Décommenter et activer Espagnol (ligne 66)
2. ✅ Ajouter description à Boonty
3. ✅ Ajouter site web personnel
4. ✅ Clarifier institution DEA

**Fichiers affectés:**

- [src/cv.typ:66](../../../src/cv.typ#L66) - Espagnol
- [src/cv.typ:160-165](../../../src/cv.typ#L160-L165) - Boonty
- [src/cv.typ:15](../../../src/cv.typ#L15) - Website
- [src/cv.typ:179](../../../src/cv.typ#L179) - DEA

**Recommandations concernées:** R12, R13, R14, R15

---

## Phase 6: Finalisation (🟢 Basse priorité)

**Objectif:** Peaufiner les détails

**Temps estimé:** 30 minutes

**Actions:**

1. ✅ Corriger écarts mineurs (Cdiscount, Cast)
2. 🤔 Décider ajout Ruby Bordeaux, Startup Weekend (si espace disponible)
3. 🤔 Décider ajout lemondedesparents.fr
4. ✅ Vérifier équilibre 2 pages

**Recommandations concernées:** R10, R11, R19

**Point critique:** Vérifier que le CV reste sur 2 pages après tous les ajouts. Si débordement:

- Réduire certaines descriptions existantes
- Déplacer le `#colbreak()` (actuellement ligne 184)
- Ajuster la taille de police ou les marges (actuellement 10pt)
- Fusionner certaines entrées

---

## Temps Total Estimé

| Phase | Temps | Cumul |
|-------|-------|-------|
| Phase 1 | 30 min | 30 min |
| Phase 2 | 30 min | 1h |
| Phase 3 | 1-1.5h | 2-2.5h |
| Phase 4 | 1h | 3-3.5h |
| Phase 5 | 1h | 4-4.5h |
| Phase 6 | 30 min | 4.5-5h |

**Total:** 4.5-5 heures (dans la fourchette estimée de 4-6.5h)

---

## Workflow Recommandé

### Après chaque phase

1. **Compiler le CV:** `just build`
2. **Vérifier visuellement:** Ouvrir `dist/cv.pdf`
3. **Vérifier la pagination:** Doit rester sur 2 pages
4. **Commit Git:** Avec référence à la phase et recommandations (ex: `Refs CNT-001 R02,R03,R04`)

### Validation finale

1. Compiler le CV final
2. Vérifier toutes les dates
3. Vérifier l'orthographe
4. Valider que toutes les recommandations sont traitées
5. Mettre à jour `recommendations-status.md`
6. Commit final avec `Closes CNT-001`

---

## Dépendances et Blocages

### Avant Phase 1

**Blocage:** Besoin de clarifier 4 dates critiques avec l'utilisateur

**Questions:**

- [ ] Upwiser: date de fin et statut parallèle avec PALO IT?
- [ ] PALO IT CTO: date de fin exacte?
- [ ] Boonty: date de début exacte et lien avec Qualia Services?
- [ ] Freelance 1999-2002: activité réelle ou études?

### Avant Phase 4

**Décision:** Format de la section bénévolat

**Options:**

- Section dédiée après certifications
- Sous-section dans "Expérience détaillée"
- Sidebar dans le CV (nécessite modification template)

### Avant Phase 6

**Validation:** Équilibre des 2 pages

**Si débordement:**

- Identifier les descriptions les plus longues à réduire
- Prioriser les informations les plus récentes/pertinentes
- Envisager version longue 3 pages (future tâche TPL-001)

---

## Références

- [Recommandations complètes](./recommendations.md)
- [Suivi des recommandations](./recommendations-status.md)
- [Rapport d'audit](./audit-report.md)
- [Métriques](./metrics.md)
