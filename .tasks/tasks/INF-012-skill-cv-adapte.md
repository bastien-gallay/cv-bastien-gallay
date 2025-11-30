# INF-012: Skill CV adapté à l'offre

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | INF-012 |
| **Titre** | Skill de génération de CV adapté à l'offre |
| **Statut** | 🔄 En cours |
| **Priorité** | 🔴 Haute |
| **Trigramme** | INF (Infrastructure) |
| **Section CV** | N/A |
| **Créé le** | 2025-11-25 |
| **Cible** | - |
| **Terminé le** | - |
| **Temps estimé** | 4-5 heures |
| **Temps réel** | - |
| **Branche nécessaire** | Auto |

---

## Description

Créer un Claude skill capable de générer une version du CV optimisée et adaptée pour une offre d'emploi spécifique.

### Contexte

Un CV adapté à l'offre permet de :

- Mettre en avant les expériences les plus pertinentes
- Utiliser les mots-clés de l'offre (optimisation ATS)
- Réorganiser les sections selon les priorités du poste
- Ajuster le niveau de détail des expériences
- Potentiellement changer le format (1 page vs 2 pages)

### Objectif

Créer un skill qui :

- Prend le CV source et l'analyse d'offre comme inputs
- Génère une version Typst adaptée
- Réorganise/priorise les expériences pertinentes
- Intègre les mots-clés ATS identifiés
- Ajuste le format si nécessaire
- Compile le PDF final

### Position dans le workflow

```text
INF-009 → INF-010
              │
              ▼
     ┌────────┴────────┐
     │                 │
     ▼                 ▼
┌─────────────┐  ┌─────────────┐
│   INF-011   │  │ ★ INF-012 ★ │
│   Lettre    │  │  CV adapté  │
└─────────────┘  └──────┬──────┘
                        │
                        ▼
                   [Output]
                   cv-adapted.typ
                   cv-adapted.pdf
```

---

## Sous-tâches

- [ ] Définir les règles d'adaptation (ordre, détail, keywords)
- [ ] Créer le mécanisme de modification du CV Typst
- [ ] Implémenter l'injection des mots-clés ATS
- [ ] Ajouter la réorganisation des sections
- [ ] Créer le workflow `/job-cv`
- [ ] Intégrer la compilation PDF automatique
- [ ] Tester avec différents types de postes

---

## Notes pour Claude

> Instructions spécifiques pour l'assistance IA

**Stratégies d'adaptation :**

1. **Réorganisation des expériences**
   - Mettre en premier les expériences les plus pertinentes
   - Développer les expériences liées au poste
   - Condenser les expériences moins pertinentes

2. **Optimisation ATS**
   - Intégrer les mots-clés de l'offre naturellement
   - Utiliser la terminologie exacte de l'offre
   - S'assurer que les compétences requises apparaissent

3. **Ajustement du format**
   - Version courte (1 page) pour certains contextes
   - Version détaillée si le poste le justifie
   - Ajuster les sections sidebar si nécessaire

4. **Mise en avant des compétences**
   - Réordonner les skills selon la pertinence
   - Ajouter des compétences mentionnées dans l'offre si possédées
   - Retirer les compétences non pertinentes

**Workflow `/job-cv` :**

```markdown
## Input
- CV source (src/cv.typ)
- Analyse d'offre (INF-009)
- Analyse d'adéquation (INF-010)
- Format souhaité (optionnel: short/long)

## Étapes
1. Charger le CV source et les analyses
2. Identifier les modifications à apporter
3. Générer le fichier Typst adapté
4. Compiler en PDF
5. Sauvegarder dans data/applications/{id}/

## Output
- Fichier cv-adapted.typ
- Fichier cv-adapted.pdf
- Rapport des modifications effectuées
```

**Structure du fichier généré :**

```typst
// cv-adapted-{company}-{date}.typ
// Généré automatiquement pour: {Titre du poste} @ {Entreprise}
// Date: {date}
// Modifications: {liste des changements}

#import "@preview/neat-cv:0.4.0": ...

// CV adapté avec les modifications suivantes:
// - Expériences réordonnées: [liste]
// - Mots-clés ajoutés: [liste]
// - Sections ajustées: [liste]

...
```

**Rapport de modifications :**

```markdown
## CV adapté pour : {Poste} @ {Entreprise}

### Modifications apportées

**Expériences réorganisées :**
1. {Expérience A} → Position 1 (était position 3)
2. {Expérience B} → Développée (+2 bullet points)

**Mots-clés intégrés :**
- "Cloud Architecture" ajouté dans expérience X
- "Team Leadership" mis en avant

**Compétences ajustées :**
- {Skill} déplacé en premier
- {Skill} retiré (non pertinent)

**Format :**
- Version 2 pages conservée
```

---

## Notes pour l'utilisateur

> Rappels, références, notes personnelles

**Utilisation prévue :**

```bash
# Générer le CV adapté
/job-cv

# Spécifier le format
/job-cv --format=short

# Voir les modifications sans générer
/job-cv --dry-run
```

**Points d'attention :**

- Toujours vérifier le CV généré avant envoi
- S'assurer que les informations restent véridiques
- Ne pas sur-optimiser au détriment de la cohérence
- Garder une trace des versions envoyées

**Intégration avec le build existant :**

```bash
# Le CV adapté peut être compilé avec just
just build experiments/cv-adapted.typ
```

---

## Références externes

### Fichiers du projet

- [src/cv.typ](../../src/cv.typ) - CV source
- [justfile](../../justfile) - Commandes de build

### Tâches liées

- [INF-008](./INF-008-architecture-skills-candidature.md) - Architecture globale
- [INF-009](./INF-009-skill-analyse-offre-emploi.md) - Fournit les mots-clés ATS
- [INF-010](./INF-010-skill-analyse-adequation.md) - Fournit la priorisation
- [TPL-001](./TPL-001-cv-versions.md) - Versions courte/longue (réutilisable)

---

## Commits Git associés

### Commit final

```bash
git commit -m "feat(skills): ✨ add adapted CV generator skill

- Generate job-specific CV versions
- Integrate ATS keywords automatically
- Reorder experiences by relevance
- Compile PDF with modifications report

Closes INF-012"
```

---

## Tests / Vérifications

- [ ] Le CV adapté compile sans erreur
- [ ] Les mots-clés sont correctement intégrés
- [ ] L'ordre des expériences est pertinent
- [ ] Le format PDF est correct
- [ ] Le rapport de modifications est clair
- [ ] Les informations restent véridiques

---

## Historique des modifications

| Date | Action | Détails |
|------|--------|---------|
| 2025-11-25 | Création | Skill de génération de CV adapté |
| 2025-11-30 | En cours | Début du travail |

---

## Résultat final

[À remplir une fois la tâche terminée]
