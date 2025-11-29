# CNT-037: Optimisation version courte (1 page)

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | CNT-037 |
| **Titre** | Optimisation version courte (1 page) |
| **Statut** | 🔄 En cours |
| **Priorité** | 🟡 Moyenne |
| **Trigramme** | CNT (Content) |
| **Section CV** | General |
| **Créé le** | 2025-11-27 |
| **Cible** | - |
| **Terminé le** | - |
| **Temps estimé** | 1 heure |
| **Temps réel** | - |
| **Branche nécessaire** | Non |

---

## Description

Densifier et optimiser la version 1 page du CV pour les ATS (robots de tri) et la prospection rapide.

### Contexte

Retours d'un expert recrutement tech (novembre 2025) :

- La version courte est visuellement propre mais peut être densifiée en mots-clés pour les ATS
- Les recruteurs scannent souvent "Python, Azure, AI" en premier
- La section "Rayonnement" (Mentor Google, Speaker) est excellente et prouve l'autorité dans le domaine
- Pour Cdiscount, préciser le volume (ex: "High traffic", "Millions de visiteurs") est un marqueur fort de crédibilité technique à Bordeaux

### Objectif

- Remonter/visibiliser la stack technique
- Ajouter contexte volume pour Cdiscount
- Préserver et optimiser la section "Rayonnement"
- Propager les améliorations du CV long (titre, résumé, chiffres en gras)

---

## Sous-tâches

- [x] Améliorer visibilité stack technique
- [x] Ajouter contexte volume Cdiscount (déjà présent : 1 milliard € CA)
- [x] Vérifier section Rayonnement (conservée)
- [x] Propager titre amélioré du CV long (déjà synchronisé via shared/config.typ)
- [x] Propager résumé vendeur condensé (déjà synchronisé via shared/sidebar.typ)
- [x] Mettre chiffres business en gras (déjà présent)
- [x] Vérifier compilation et rendu final

---

## Notes pour Claude

> Instructions spécifiques pour l'assistance IA

### Mode interactif

> **IMPORTANT** : Cette tâche nécessite une validation utilisateur avant exécution.

#### Questions au démarrage

Avant de commencer les modifications, poser les questions suivantes :

1. **Stack technique prioritaire** : Quels éléments techniques sont les plus importants pour la prospection rapide ?
   - Options : GenAI, Python, TypeScript, Azure, AWS, React, Node.js
   - Combien d'éléments maximum dans la sidebar ?

2. **Position stack** : Préférez-vous la stack technique :
   - En haut de la sidebar (plus visible)
   - Dans une section dédiée "Tech" bien identifiée
   - Répartie dans les pôles (si LAY-003 appliqué)

3. **Contexte Cdiscount** : Quel volume/contexte ajouter ?
   - "High traffic e-commerce platform"
   - "Millions de visiteurs/mois"
   - "Top 5 e-commerce français"
   - Autre formulation ?

4. **Section Rayonnement** : Faut-il modifier cette section ?
   - Conserver telle quelle (recommandé)
   - Ajouter/retirer des éléments
   - Changer l'ordre des items

5. **Éléments à ajouter/retirer** : Y a-t-il d'autres éléments à ajouter ou retirer de la version courte ?

#### Processus

1. Poser les questions ci-dessus
2. Attendre les réponses de l'utilisateur
3. Proposer les modifications
4. Demander validation avant d'appliquer
5. Itérer si nécessaire

---

### Transformations spécifiques

#### Visibilité stack technique

Options de positionnement :

```typst
// Option A: En haut de sidebar
== Stack Technique
#item-pills(
  "GenAI",
  "Python",
  "TypeScript",
  "Azure/AWS",
)

// Option B: Section Expertises réorganisée (si LAY-003 appliqué)
== Expertises
=== Tech & IA
#item-pills("GenAI", "Python", "TypeScript", "Azure/AWS", "DDD")
```

#### Contexte Cdiscount

**Avant** :

```typst
#entry(
  title: "Lead Développeur",
  date: "2010 - 2013",
  institution: "Cdiscount",
  // ...
)
```

**Après** :

```typst
#entry(
  title: "Lead Développeur",
  date: "2010 - 2013",
  institution: "Cdiscount (Top 5 e-commerce FR, millions de visiteurs/mois)",
  // ...
)
```

#### Propagation améliorations CV long

Après CNT-036, propager :

- Nouveau titre (si différent)
- Résumé vendeur condensé (adapter à 1 page)
- Chiffres business en gras

---

**Fichiers à modifier:**

- [src/cv-short.typ](../../src/cv-short.typ) - CV court (1 page)

**Points d'attention:**

- La version courte doit rester sur 1 page
- Vérifier que les modifications ne cassent pas la mise en page
- Compiler après chaque modification (`just build-short`)
- S'assurer de la cohérence avec le CV long

**Prérequis recommandés:**

- CNT-036 (Condensation et impact business) devrait être terminé avant pour propager les améliorations
- TPL-005 / LAY-004 (Factorisation page 1) - après factorisation, les modifications de cv-short.typ devront :
  - Modifier `src/shared/` pour les éléments communs (config, sidebar)
  - Modifier uniquement `cv-short.typ` pour le contenu spécifique à la version courte

---

## Notes pour l'utilisateur

> Rappels, références, notes personnelles

**Usage de la version courte :**

- Prospection rapide
- Candidatures spontanées
- Réseaux professionnels (LinkedIn, etc.)
- Screening initial par ATS

**Points forts à préserver :**

- Section "Rayonnement" (Mentor Google, Speaker) → autorité
- Lisibilité immédiate
- Mots-clés ATS visibles

---

## Références externes

### Fichiers du projet

- [src/cv-short.typ](../../src/cv-short.typ) - CV court à modifier

### Tâches liées

- [CNT-036](./CNT-036-condensation-impact-business.md) - Condensation CV long (prérequis recommandé)
- [LAY-003](./LAY-003-reorganiser-competences-3-poles.md) - Réorganiser compétences (si applicable)

### Ressources

- Retours expert recrutement tech (novembre 2025)

---

## Commits Git associés

### Commit final

```bash
git commit -m "content(cv-short): ✨ optimize one-page CV for ATS

- Improved tech stack visibility
- Added Cdiscount volume context (Top 5 e-commerce FR)
- Preserved Rayonnement section (Google Mentor, Speaker)
- Propagated improvements from full CV (title, profile, bold metrics)

Closes CNT-037"
```

---

## Tests / Vérifications

- [x] Le CV compile sans erreur (`just build-short`)
- [x] Le CV reste sur 1 page
- [x] La stack technique est visible rapidement
- [x] Le contexte Cdiscount est ajouté
- [x] La section Rayonnement est préservée
- [x] Les améliorations du CV long sont propagées
- [x] La cohérence avec cv.typ est maintenue

---

## Historique des modifications

| Date | Action | Détails |
|------|--------|---------|
| 2025-11-29 | En cours | Début du travail |
| 2025-11-27 | Création | Tâche créée suite aux retours expert recrutement |

---

## Résultat final

[À remplir une fois la tâche terminée]
