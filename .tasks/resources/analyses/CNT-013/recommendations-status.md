# CNT-013: Suivi des Recommandations - CV 2019 vs CV 2025

**Analyse:** CNT-013 - Analyse ancien CV > 5 ans (2019)
**Date:** 2025-11-14
**Source:** Comparaison CV 2019 (Mars 2019) vs CV Actuel (2025)

---

## 📊 Statistiques

| Statut | Très Haute | Haute | Moyenne | Basse | **Total** |
|--------|------------|-------|---------|-------|-----------|
| ⏳ **En attente** | 2 | 4 | 6 | 2 | **14** |
| 🔨 **Tâche créée** | 0 | 0 | 0 | 0 | **0** |
| ✅ **Terminé** | 0 | 0 | 0 | 0 | **0** |
| 🚫 **Rejeté** | 0 | 0 | 0 | 0 | **0** |
| **Total** | **2** | **4** | **6** | **2** | **14** |

**Progression:** 0% (0/14 recommandations traitées)

---

## 🔴🔴 Très Haute Priorité (Critique)

### R01 - Corriger erreur dates Indépendant

- ☐ **Statut:** ⏳ En attente
- **Tâche associée:** -
- **Catégorie:** Incohérence de dates (critique)
- **Source:** [audit-report.md § 4.7](./audit-report.md#47-indépendant-2002-2004---erreur-critique--description-vide)
- **Référence CV:** src/cv.typ:169
- **Trigramme suggéré:** CNT
- **Date ajout:** 2025-11-14
- **Description:** CV actuel indique "06/1999 - 06/2004" pour Indépendant, ce qui est chronologiquement impossible (études DUT 1999, Licence/Maîtrise 2001, DEA 2002). Dates correctes: 09/2002 - 06/2004 (ou 07/2002 selon documents).
- **Impact:** 🔴🔴 Crédibilité du CV compromise, erreur chronologique évidente détectable par recruteurs/ATS
- **Effort:** Très faible (correction 1 ligne)

### R02 - Clarifier et corriger dates Boonty/Qualia Service

- ☐ **Statut:** ⏳ En attente
- **Tâche associée:** -
- **Catégorie:** Incohérence de dates
- **Source:** [audit-report.md § 4.6](./audit-report.md#46-boonty-2004-2006---expérience-vidée)
- **Référence CV:** src/cv.typ:162
- **Trigramme suggéré:** CNT
- **Date ajout:** 2025-11-14
- **Description:** Écarts entre CV 2019 (06/2004-08/2006), CV 2025 (07/2004-07/2006) et clarification utilisateur (06/2004-07/2006 avec Qualia Service 06/2004-07/2005 + Boonty direct 07/2005-07/2006). Nécessite vérification documents officiels (KBIS, contrats, bulletins paie) pour dates exactes.
- **Impact:** 🔴🔴 Cohérence des dates critique, traçabilité Qualia Service nécessaire
- **Effort:** Moyen (recherche documents + correction)

---

## 🔴 Haute Priorité (Important)

### R03 - Ajouter 3 missions détaillées Upwiser

- ☐ **Statut:** ⏳ En attente
- **Tâche associée:** -
- **Catégorie:** Enrichissement contenu
- **Source:** [audit-report.md § 4.3](./audit-report.md#43-upwiser-2013-2021---régression-massive)
- **Référence CV:** src/cv.typ:253 (section "Expérience détaillée" vide)
- **Trigramme suggéré:** CNT
- **Date ajout:** 2025-11-14
- **Description:** Perte de 12 missions détaillées Upwiser (6 majeures + 6 autres interventions). Ajouter au minimum: (1) Dekra Programme Next (10/2013-02/2015) - 30 personnes, 10k j/h, Feature Teams, TDD/BDD; (2) iBP Agile par Nature (04/2015-09/2015) - Banque, LeSS, multi-site; (3) Robin Finance (10/2017+) - Fintech, coaching PO/CTO.
- **Impact:** 🔴 Preuves concrètes pour 7 ans d'expérience, crédibilité, mots-clés ATS (clients, technologies)
- **Effort:** Élevé (rédaction 3 missions détaillées)

### R04 - Restaurer description Boonty

- ☐ **Statut:** ⏳ En attente
- **Tâche associée:** -
- **Catégorie:** Enrichissement contenu
- **Source:** [audit-report.md § 4.6](./audit-report.md#46-boonty-2004-2006---expérience-vidée)
- **Référence CV:** src/cv.typ:161-165
- **Trigramme suggéré:** CNT
- **Date ajout:** 2025-11-14
- **Description:** Description vide dans CV actuel. Restaurer: Gestion 2 projets pilotes 400k€/mois chacun, création Framework interne, R&D DRM et magasins en ligne, équipes internationales (Singapour, Corée, Japon, New York), technologies PHP 4 & 5, MySQL, SOAP, XML.
- **Impact:** 🔴 Preuve gestion projets fort CA, compétence architecture, international
- **Effort:** Faible (ajout 5 bullets)

### R05 - Enrichir description CDiscount

- ☐ **Statut:** ⏳ En attente
- **Tâche associée:** -
- **Catégorie:** Enrichissement contenu
- **Source:** [audit-report.md § 4.4](./audit-report.md#44-cdiscount-2010-2013---perte-modérée)
- **Référence CV:** src/cv.typ:137-146
- **Trigramme suggéré:** CNT
- **Date ajout:** 2025-11-14
- **Description:** Condensation de 9 bullets → 3 bullets. Ajouter: Certification PCI DSS, refonte SaaS, Scrum/Scrumban 200 j/mois, anonymisation données (RGPD), Coding Dojos internes, coaching développeurs/chefs de projets.
- **Impact:** 🔴 PCI DSS (ATS paiement/sécurité), SaaS, RGPD, 200 j/mois (volume), leadership (Dojos)
- **Effort:** Faible (ajout 4 bullets)

### R06 - Restaurer centres d'intérêt concrets

- ☐ **Statut:** ⏳ En attente
- **Tâche associée:** -
- **Catégorie:** Enrichissement contenu
- **Source:** [audit-report.md § 7](./audit-report.md#7-centres-dintérêt-et-engagement-communautaire)
- **Référence CV:** src/cv.typ:43-46
- **Trigramme suggéré:** CNT
- **Date ajout:** 2025-11-14
- **Description:** Perte de 5 activités concrètes (Leader Lean Startup Bordeaux, Orateur conférences, Organisateur Agile Tour, Coach Startup Weekend, Co-fondateur Ruby Bordeaux) remplacées par 3 thématiques génériques. Restaurer avec preuves: IA (Gen-e2), Entrepreneuriat (Leader Lean Startup, coaching 100+ startups, Agile Tour), Communauté (orateur, co-fondateur Ruby Bordeaux), Management (mentorat).
- **Impact:** 🔴 Preuves leadership, visibilité communauté, différenciation vs générique
- **Effort:** Faible (réécriture 4 bullets)

---

## 🟡 Moyenne Priorité (Souhaitable)

### R07 - Ajouter certifications manquantes

- ☐ **Statut:** ⏳ En attente
- **Tâche associée:** -
- **Catégorie:** Certification
- **Source:** [audit-report.md § 6](./audit-report.md#6-certifications)
- **Référence CV:** src/cv.typ:220-250
- **Trigramme suggéré:** CNT
- **Date ajout:** 2025-11-14
- **Description:** 4 certifications manquantes: (1) Professional Scrum Developer (PSD) - 2015, Scrum.org; (2) Facilitation Graphique - 2014, Ayeba/R. Couturier; (3) Improve Your User Stories - 2014, Neuri Consulting/G. Adzic; (4) Gestion de projet - 2008, Merlane. Priorité: PSD, Facilitation Graphique, Improve Your User Stories.
- **Impact:** 🟡 PSD (technique Scrum), Facilitation (différenciation), User Stories (Gojko Adzic référence)
- **Effort:** Faible (ajout 3 entrées)

### R08 - Enrichir description Cast SA

- ☐ **Statut:** ⏳ En attente
- **Tâche associée:** -
- **Catégorie:** Enrichissement contenu
- **Source:** [audit-report.md § 4.5](./audit-report.md#45-cast-sa-2006-2010---perte-missions-détaillées)
- **Référence CV:** src/cv.typ:148-157 ou 253+
- **Trigramme suggéré:** CNT
- **Date ajout:** 2025-11-14
- **Description:** Perte de 6 missions détaillées. Option 1 (minimale): Enrichir avec JOA Online (PO équipe 10 FR/PT, Scrum distribué, 10 sous-traitants Europe), Pixmania TheLink.com (management 7 dev, coordination Londres), CEA, Nespresso, La Poste. Option 2 (complète): Ajouter missions dans section "Expérience détaillée".
- **Impact:** 🟡 Clients nommés, contextes variés, management international
- **Effort:** Moyen (enrichissement description ou ajout missions)

### R09 - Restaurer Espagnol (Notions)

- ☐ **Statut:** ⏳ En attente
- **Tâche associée:** -
- **Catégorie:** Langue
- **Source:** [audit-report.md § 2](./audit-report.md#2-langues)
- **Référence CV:** src/cv.typ:66
- **Trigramme suggéré:** CNT
- **Date ajout:** 2025-11-14
- **Description:** Espagnol présent dans le code mais commenté. Décommenter: `#item-with-level("Espagnol", 2, subtitle: "Notions")`
- **Impact:** 🟡 Faible, mais différenciateur pour postes internationaux
- **Effort:** Très faible (décommenter 1 ligne)

### R10 - Ajouter compétences manquantes aux pills

- ☐ **Statut:** ⏳ En attente
- **Tâche associée:** -
- **Catégorie:** Compétences
- **Source:** [audit-report.md § 3](./audit-report.md#3-compétences-et-expertises)
- **Référence CV:** src/cv.typ:69-88
- **Trigramme suggéré:** CNT
- **Date ajout:** 2025-11-14
- **Description:** ~15 compétences présentes en 2019 absentes en 2025. Ajouter aux pills: DevOps, BDD (Behaviour Driven Development), Impact Mapping, Story Mapping. Cohérence avec missions Upwiser et recherche ATS.
- **Impact:** 🟡 Mots-clés ATS, cohérence avec missions 2019
- **Effort:** Faible (ajout 4 items pills)

### R11 - Vérifier date certification CSM

- ☐ **Statut:** ⏳ En attente
- **Tâche associée:** -
- **Catégorie:** Certification
- **Source:** [audit-report.md § 6.2](./audit-report.md#62-analyse)
- **Référence CV:** src/cv.typ:223-226
- **Trigramme suggéré:** CNT
- **Date ajout:** 2025-11-14
- **Description:** Écart de date CSM: 2009 (CV 2019) vs 2008 (CV 2025). Vérifier certificat original pour date exacte.
- **Impact:** 🟡 Faible (écart 1 an seulement)
- **Effort:** Faible (vérification certificat)

### R12 - Clarifier dates mineures (Upwiser, CDiscount, Cast)

- ☐ **Statut:** ⏳ En attente
- **Tâche associée:** -
- **Catégorie:** Incohérence de dates
- **Source:** [audit-report.md § 9](./audit-report.md#9-synthèse-des-écarts-de-dates)
- **Référence CV:** Multiple (src/cv.typ:122, 139, 150)
- **Trigramme suggéré:** CNT
- **Date ajout:** 2025-11-14
- **Description:** Écarts mineurs de dates (-1 mois): Upwiser début (09/2013 vs 10/2013), CDiscount fin (09/2013 vs 10/2013), Cast début (07/2006 vs 08/2006). Vérifier documents officiels si possible.
- **Impact:** 🟡 Faible (écarts 1 mois)
- **Effort:** Faible (vérification documents)

---

## 🟢 Basse Priorité (Optionnel)

### R13 - Enrichir description Indépendant

- ☐ **Statut:** ⏳ En attente
- **Tâche associée:** -
- **Catégorie:** Enrichissement contenu
- **Source:** [audit-report.md § 4.7](./audit-report.md#47-indépendant-2002-2004---erreur-critique--description-vide)
- **Référence CV:** src/cv.typ:167-172
- **Trigramme suggéré:** CNT
- **Date ajout:** 2025-11-14
- **Description:** Description vide (après correction dates critiques R01). Ajouter: Création sites internet PME et associations, pilotage projets (recueil besoins → production), conseil et expertise technique (PHP, MySQL, HTML, JS).
- **Impact:** 🟢 Faible (expérience ancienne), mais complétude
- **Effort:** Faible (ajout 3 bullets)

### R14 - Considérer tableau récapitulatif compétences

- ☐ **Statut:** ⏳ En attente
- **Tâche associée:** -
- **Catégorie:** Structure/Layout
- **Source:** [audit-report.md § 8.2](./audit-report.md#82-organisation-du-contenu)
- **Référence CV:** Nouveau (ajout potentiel)
- **Trigramme suggéré:** LAY
- **Date ajout:** 2025-11-14
- **Description:** Ajouter tableau structuré style CV 2019 (5 catégories: Certifications, Méthodes, Gestion Produit, Craftmanship, Facilitation) en complément des pills pour améliorer scannabilité et structure pédagogique.
- **Impact:** 🟢 Faible (format actuel efficace), mais structure pédagogique intéressante
- **Effort:** Moyen (création tableau, contrainte espace 2 pages A4)

---

## 📋 Instructions d'Utilisation

### Pour Créer des Tâches depuis les Recommandations

```bash
/task-from-analysis --analysis-id=CNT-013 [--filter=high|medium|low|all]
```

**Exemples:**

```bash
# Créer tâches pour recommandations haute priorité uniquement
/task-from-analysis --analysis-id=CNT-013 --filter=high

# Créer tâches pour recommandations très haute et haute priorité
/task-from-analysis --analysis-id=CNT-013 --filter=high

# Créer tâches pour toutes les recommandations
/task-from-analysis --analysis-id=CNT-013 --filter=all
```

### Pour Mettre à Jour ce Fichier

**Lorsqu'une tâche est créée depuis une recommandation:**

1. Remplacer `☐` par `☑`
2. Changer le statut de `⏳ En attente` à `🔨 Tâche créée`
3. Ajouter l'ID de la tâche dans "Tâche associée"

**Exemple:**

```markdown
### R01 - Corriger erreur dates Indépendant
- ☑ **Statut:** 🔨 Tâche créée
- **Tâche associée:** CNT-016
```

**Lorsqu'une tâche est terminée:**

1. Changer le statut de `🔨 Tâche créée` à `✅ Terminé`
2. Ajouter la date de complétion

**Exemple:**

```markdown
### R01 - Corriger erreur dates Indépendant
- ☑ **Statut:** ✅ Terminé (2025-11-15)
- **Tâche associée:** CNT-016
```

**Lorsqu'une recommandation est rejetée:**

1. Remplacer `☐` par `☒`
2. Changer le statut de `⏳ En attente` à `🚫 Rejeté`
3. Ajouter la raison du rejet

**Exemple:**

```markdown
### RXX - Titre de la recommandation
- ☒ **Statut:** 🚫 Rejeté
- **Raison:** Clarification utilisateur - information déjà correcte dans le CV actuel
```

### Mise à Jour des Statistiques

Après chaque modification, mettre à jour manuellement le tableau des statistiques en haut du fichier.

---

## 🔗 Fichiers Liés

- [audit-report.md](./audit-report.md) - Analyse comparative complète
- [recommendations.md](./recommendations.md) - Détails de chaque recommandation (version étendue)
- [cv-2019.md](../../audits/CNT-013/cv-2019.md) - Extraction CV 2019
- [cv-snapshot.md](../../audits/CNT-013/cv-snapshot.md) - Snapshot CV actuel 2025

---

**Dernière mise à jour:** 2025-11-14
**Analyse:** CNT-013
**Fichier:** recommendations-status.md
