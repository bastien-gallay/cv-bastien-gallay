# Recommandations de l'Audit LinkedIn

**Analyse:** CNT-001
**Date:** 2025-10-29
**Total:** 19 recommandations

Ce fichier liste toutes les recommandations issues de l'audit comparatif LinkedIn vs CV. Ces recommandations peuvent être transformées en tâches via la commande `/task-from-analysis`.

Le suivi de l'implémentation se fait dans le fichier [recommendations-status.md](./recommendations-status.md).

---

## Priorité TRÈS HAUTE (1 recommandation)

### R01 - Corriger l'écart critique sur Upwiser

**Problème:** Date de fin très différente

- LinkedIn: oct. 2013 - **nov. 2024** (11 ans 2 mois)
- CV: 09/2013 - **01/2021** (7 ans 4 mois)
- **Écart: +3 ans 10 mois**

**Questions à clarifier:**

- Upwiser a-t-il continué parallèlement à PALO IT (2021-2024)?
- S'agit-il d'une activité à temps partiel/maintien de structure?
- Quelle est la date réelle de fin?

**Action:** Vérifier les documents officiels (KBIS, contrats) pour confirmer la date exacte

**Référence CV:** [src/cv.typ:122](../../../src/cv.typ#L122)

---

## Priorité HAUTE (10 recommandations)

### R02 - Corriger la date de fin CTO chez PALO IT

**Problème:**

- LinkedIn: nov. 2024 - **oct. 2025**
- CV: 10/2024 - **08/2025**
- **Écart: -2 mois**

**Action:** Mettre à jour le CV avec la date exacte (oct. 2025)

**Référence CV:** [src/cv.typ:107](../../../src/cv.typ#L107)

---

### R03 - Corriger les dates de Boonty

**Problème:**

- LinkedIn: **juin 2005** - juil. 2006 (1 an 2 mois)
- CV: **07/2004** - 07/2006 (2 ans)
- **Écart: -13 mois de début, -10 mois de durée**

**Impact:** Cet écart affecte également les dates de Qualia Services (non présent dans CV)

**Action:** Vérifier contrats de travail pour dates exactes

**Référence CV:** [src/cv.typ:162](../../../src/cv.typ#L162)

---

### R04 - Corriger les dates de début Freelance

**Problème:**

- LinkedIn: **juin 2002** - juin 2004 (2 ans)
- CV: **06/1999** - 06/2004 (5 ans)
- **Écart: -3 ans**

**Action:** Clarifier l'activité 1999-2002 (études? freelance? autre?)

**Référence CV:** [src/cv.typ:169](../../../src/cv.typ#L169)

---

### R05 - Ajouter les certifications manquantes

**Certifications à ajouter:**

1. **Professional Scrum Developer (PSD-I)** - Scrum.org (May 2018)
2. **Scaled Professional Scrum (SPS)** - Scrum.org (Jan 2016)

**Emplacement:** Après ligne 232, avant "Professional Scrum with Kanban"

**Référence CV:** [src/cv.typ:220-250](../../../src/cv.typ#L220-L250)

---

### R06 - Corriger la date SAFe

**Problème:**

- LinkedIn: Jun 2020 (SAFe 5)
- CV: 2018 (SPC4 et SPC5)

**Action:** Clarifier si certification obtenue en 2018 et mise à jour en 2020, ou obtenue en 2020

**Référence CV:** [src/cv.typ:248](../../../src/cv.typ#L248)

---

### R07 - Ajouter l'expérience i-BP

**Détails LinkedIn:**

- **Poste:** Coach Agile (Freelance)
- **Dates:** avr. 2015 - sept. 2015 (6 mois)
- **Lieu:** Nantes Area, France
- **Description:**
  - Accompagnement de projets Agiles: Décisionnel, Livraison (DevOps)
  - Coaching de la communauté de pratique des équipiers Agiles
  - Participation à des travaux transverses d'organisation
  - Mise en place de Coach Dating
  - Méthodes: Scrum, Kanban, Lean Startup

**Emplacement:** Insérer entre Upwiser et Cdiscount (chronologique: 2015)

**Note:** Cette mission s'inscrit dans la période Upwiser, préciser que c'est une mission freelance

**Référence CV:** Insertion recommandée après ligne 135

---

### R08 - Ajouter l'expérience DEKRA

**Détails LinkedIn:**

- **Poste:** Coach Agile (Freelance)
- **Dates:** oct. 2013 - janv. 2015 (1 an 4 mois)
- **Lieu:** Bordeaux Area, France
- **Description:**
  - Scrum Mastering pour le projet de refonte logiciel interne
  - Mise en place des feature teams, coordination multi-équipes
  - Coaching et formation des nouveaux Scrum Masters
  - Accompagnement à l'adoption de bonnes pratiques

**Emplacement:** Insérer entre Upwiser et Cdiscount (chronologique: 2013-2015)

**Note:** Cette mission démarre juste après le début d'Upwiser (oct. 2013), clarifier le lien

**Référence CV:** Insertion recommandée après ligne 135

---

### R09 - Ajouter section Bénévolat

**Organisations à inclure (par priorité):**

1. **Agile Tour Bordeaux** - 2011-aujourd'hui (fusionner les 2 entrées LinkedIn)
2. **Lean Startup Bordeaux** - 2012-2018 (déjà mentionné dans Upwiser, créer section dédiée)
3. **Collectif Quinconces** - 2016-2018

**Emplacement:** Nouvelle section après Certifications, avant "Expérience détaillée"

**Référence CV:** Insertion recommandée après ligne 250

---

### R10 - Corriger écarts mineurs de dates (Cdiscount)

**Problème:**

- **Cdiscount fin:** oct. 2013 vs 09/2013 (-1 mois)

**Impact:** Négligeable, mais corrigeable pour cohérence absolue

**Référence CV:** [src/cv.typ:139](../../../src/cv.typ#L139)

---

### R11 - Corriger écarts mineurs de dates (Cast)

**Problème:**

- **Cast début:** août 2006 vs 07/2006 (-1 mois)

**Impact:** Négligeable, mais corrigeable pour cohérence absolue

**Référence CV:** [src/cv.typ:150](../../../src/cv.typ#L150)

---

## Priorité MOYENNE (5 recommandations)

### R12 - Ajouter la langue Espagnol

**Action:** Décommenter la ligne 66 et ajuster le niveau si nécessaire

**Actuel (commenté):**

```typst
// #item-with-level("Espagnol", 2, subtitle: "Notions")
```

**LinkedIn indique:** Elementary proficiency

**Référence CV:** [src/cv.typ:66](../../../src/cv.typ#L66)

---

### R13 - Enrichir la description de Boonty

**Description LinkedIn disponible:**

- Travail architectural sur front office et back office
- Intégration DRM serveur pour jeux vidéo (Macrovision, Starforce, Sony/SecuROM)
- Développement du système d'abonnement pour jeux vidéo

**Actuel:** Description vide

**Référence CV:** [src/cv.typ:160-165](../../../src/cv.typ#L160-L165)

---

### R14 - Ajouter le site web personnel

**Action:** Décommenter et mettre à jour la ligne website

**URL LinkedIn:** <http://bastien.gallay.org/>

**Référence CV:** [src/cv.typ:15](../../../src/cv.typ#L15)

---

### R15 - Clarifier l'institution du DEA

**Problème:** LinkedIn indique UVSQ, CV indique INSTN Sacclay

**Action:** Vérifier le diplôme original, potentiellement indiquer les deux institutions si partenariat

**Référence CV:** [src/cv.typ:176-194](../../../src/cv.typ#L176-L194)

---

### R16 - Ajouter ITS Group

**Détails LinkedIn:**

- **Poste:** Project manager
- **Dates:** oct. 2010 - juin 2011 (9 mois)
- **Lieu:** Bordeaux
- **Description:** En mission pour CDiscount

**Note:** Clarifiante car explique le chevauchement avec Cdiscount (ESN)

**Référence CV:** Insertion optionnelle après Cdiscount ou en note

---

## Priorité BASSE (3 recommandations)

### R17 - Ajouter Ruby Bordeaux au bénévolat

**Détails:** Organisateur, janv. 2011 - janv. 2013 (2 ans)

**Référence CV:** Nouvelle section bénévolat

---

### R18 - Ajouter Startup Weekend Bordeaux

**Détails:** Coach Agile, oct. 2012 (1 mois)

**Référence CV:** Nouvelle section bénévolat

---

### R19 - Ajouter site "Le monde des parents"

**URL:** <http://lemondedesparents.fr>

**Référence CV:** [src/cv.typ:15](../../../src/cv.typ#L15) (ligne website)

---

## Statistiques des Recommandations

| Priorité | Nombre | Temps estimé |
|----------|--------|-------------|
| 🔴🔴 Très Haute | 1 | 30 min |
| 🔴 Haute | 10 | 2-3h |
| 🟡 Moyenne | 5 | 1-2h |
| 🟢 Basse | 3 | 1h |
| **TOTAL** | **19** | **4-6.5h** |

## Répartition par Catégorie

| Catégorie | Nombre |
|-----------|--------|
| Dates incohérentes | 7 |
| Expériences manquantes | 4 |
| Certifications manquantes | 2 |
| Langue manquante | 1 |
| Bénévolat absent | 3 |
| Sites web absents | 2 |

---

**Prochaine étape:** Utiliser `/task-from-analysis` pour transformer ces recommandations en tâches concrètes.
