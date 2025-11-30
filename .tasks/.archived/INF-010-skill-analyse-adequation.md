# INF-010: Skill analyse adéquation profil-poste

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | INF-010 |
| **Titre** | Skill d'analyse de l'adéquation profil-poste |
| **Statut** | ⏳ À faire |
| **Priorité** | 🔴 Haute |
| **Trigramme** | INF (Infrastructure) |
| **Section CV** | N/A |
| **Créé le** | 2025-11-25 |
| **Cible** | - |
| **Terminé le** | - |
| **Temps estimé** | 3-4 heures |
| **Temps réel** | - |
| **Branche nécessaire** | Auto |

---

## Description

Créer un Claude skill qui analyse la correspondance entre le profil du candidat (CV) et les exigences d'une offre d'emploi.

### Contexte

L'analyse d'adéquation permet de :

- Évaluer objectivement la correspondance profil/poste
- Identifier les points forts à mettre en avant
- Repérer les lacunes à adresser ou compenser
- Préparer les arguments pour la candidature
- Décider si la candidature vaut la peine d'être soumise

### Objectif

Créer un skill qui :

- Compare le CV aux exigences de l'offre analysée
- Calcule un score d'adéquation global
- Identifie les forces et faiblesses
- Suggère des points de discussion/argumentation
- Propose des recommandations pour la candidature

### Position dans le workflow

```text
    INF-009 (Analyse offre)
         │
         ▼
┌─────────────────┐
│ ★ INF-010 ★     │
│ Analyse fit     │
│ Score + Points  │
└────────┬────────┘
         │
    ┌────┴────┐
    ▼         ▼
INF-011   INF-012
Lettre    CV adapté
```

---

## Sous-tâches

- [ ] Définir la méthodologie de scoring
- [ ] Créer le template de rapport d'adéquation
- [ ] Implémenter la comparaison compétences requises vs possédées
- [ ] Ajouter l'analyse des expériences pertinentes
- [ ] Générer les recommandations et talking points
- [ ] Créer le workflow `/job-fit`
- [ ] Tester avec différents profils de postes

---

## Notes pour Claude

> Instructions spécifiques pour l'assistance IA

**Structure du rapport d'adéquation :**

```markdown
# Adéquation : {Titre du poste} @ {Entreprise}

## Score global : XX/100 ⭐⭐⭐⭐☆

## Correspondance des exigences

### ✅ Exigences satisfaites (X/Y)
| Exigence | Preuve dans le profil |
|----------|----------------------|
| Python 5+ ans | 8 ans d'expérience Python |
| Leadership | CTO, management 15 personnes |

### ⚠️ Exigences partiellement satisfaites (X/Y)
| Exigence | Situation actuelle | Recommandation |
|----------|-------------------|----------------|
| Kubernetes | Expérience Docker | Mentionner apprentissage en cours |

### ❌ Exigences non satisfaites (X/Y)
| Exigence | Impact | Stratégie |
|----------|--------|-----------|
| Certification AWS | Faible | Mettre en avant expérience cloud |

## Points forts à valoriser
1. **Leadership technique** : 5 ans en tant que CTO
2. **Expertise IA** : Publications, certifications

## Lacunes à adresser
1. **Certification manquante** : Compenser par expérience
2. **Secteur différent** : Transférer les compétences

## Talking points pour l'entretien
- "Mon expérience en X démontre que..."
- "J'ai géré des projets similaires quand..."

## Recommandation finale
🟢 Candidature recommandée / 🟡 À considérer / 🔴 Profil peu adapté

**Justification** : ...
```

**Méthodologie de scoring :**

```python
score = (
    must_have_match * 0.6 +      # 60% poids exigences obligatoires
    nice_to_have_match * 0.2 +   # 20% poids exigences souhaitées
    experience_relevance * 0.15 + # 15% pertinence expériences
    culture_fit * 0.05            # 5% adéquation culturelle
) * 100
```

**Workflow `/job-fit` :**

```markdown
## Input
- Analyse d'offre (INF-009) - automatique si disponible
- CV source (src/cv.typ)

## Étapes
1. Charger l'analyse de l'offre
2. Parser le CV pour extraire compétences et expériences
3. Comparer point par point
4. Calculer le score d'adéquation
5. Générer les recommandations
6. Produire le rapport

## Output
- Rapport d'adéquation avec score
- Liste des talking points
- Recommandation go/no-go
```

---

## Notes pour l'utilisateur

> Rappels, références, notes personnelles

**Utilisation prévue :**

```bash
# Après avoir analysé une offre
/job-fit

# Spécifier une offre particulière
/job-fit --application=google-2025-01-15
```

**Interprétation des scores :**

- 80-100 : Excellent fit, candidature prioritaire
- 60-79 : Bon fit, candidature recommandée
- 40-59 : Fit moyen, à évaluer selon motivation
- 0-39 : Fit faible, candidature risquée

---

## Références externes

### Fichiers du projet

- [src/cv.typ](../../src/cv.typ) - CV source pour l'analyse

### Tâches liées

- [INF-008](./INF-008-architecture-skills-candidature.md) - Architecture globale
- [INF-009](./INF-009-skill-analyse-offre-emploi.md) - Fournit l'analyse d'offre
- [INF-011](./INF-011-skill-lettre-motivation.md) - Utilise cette analyse
- [INF-012](./INF-012-skill-cv-adapte.md) - Utilise cette analyse

---

## Commits Git associés

### Commit final

```bash
git commit -m "feat(skills): ✨ add profile-job fit analysis skill

- Compare CV against job requirements
- Calculate fit score with weighted criteria
- Generate talking points and recommendations
- Provide go/no-go recommendation

Closes INF-010"
```

---

## Tests / Vérifications

- [ ] Le skill charge correctement le CV
- [ ] La comparaison des compétences fonctionne
- [ ] Le score est calculé correctement
- [ ] Les recommandations sont pertinentes
- [ ] Le rapport est clair et actionnable

---

## Historique des modifications

| Date | Action | Détails |
|------|--------|---------|
| 2025-11-25 | Création | Skill d'analyse adéquation profil-poste |

---

## Résultat final

[À remplir une fois la tâche terminée]
