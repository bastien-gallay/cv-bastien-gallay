# INF-009: Skill analyse d'offre d'emploi

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | INF-009 |
| **Titre** | Skill d'analyse d'offre d'emploi |
| **Statut** | ⏳ À faire |
| **Priorité** | 🟡 Moyenne |
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

Créer un Claude skill capable d'analyser une offre d'emploi et d'en extraire les informations structurées pertinentes.

### Contexte

L'analyse d'une offre d'emploi est la première étape du processus de candidature. Elle permet de :

- Identifier les compétences requises vs souhaitées
- Comprendre les responsabilités du poste
- Détecter les mots-clés importants (ATS)
- Évaluer le niveau d'expérience attendu
- Repérer les éventuels red flags

### Objectif

Créer un skill qui :

- Accepte une URL ou le texte d'une offre d'emploi
- Extrait et structure les informations clés
- Identifie les exigences obligatoires vs optionnelles
- Détecte les mots-clés pour l'optimisation ATS
- Recherche des informations sur l'entreprise (optionnel)
- Génère un rapport d'analyse formaté

---

## Sous-tâches

- [ ] Définir le format d'entrée (URL, texte, fichier)
- [ ] Créer le template de rapport d'analyse
- [ ] Implémenter l'extraction des informations structurées
- [ ] Ajouter la détection des mots-clés ATS
- [ ] Intégrer la recherche entreprise (WebSearch)
- [ ] Créer le workflow `/job-analyze`
- [ ] Tester avec différents types d'offres
- [ ] Documenter l'utilisation

---

## Notes pour Claude

> Instructions spécifiques pour l'assistance IA

**Structure du rapport d'analyse :**

```markdown
# Analyse : {Titre du poste} @ {Entreprise}

## Informations générales
- **Poste**: ...
- **Entreprise**: ...
- **Localisation**: ...
- **Type de contrat**: ...
- **Salaire**: ... (si mentionné)

## Exigences

### Obligatoires (must-have)
- [ ] Compétence 1
- [ ] Compétence 2

### Souhaitées (nice-to-have)
- [ ] Compétence 3

## Responsabilités principales
1. ...
2. ...

## Mots-clés ATS
`keyword1`, `keyword2`, `keyword3`

## Contexte entreprise
- Secteur: ...
- Taille: ...
- Actualités récentes: ...

## Points d'attention
- ⚠️ Red flag potentiel: ...
- ✅ Point positif: ...

## Recommandations pour la candidature
- Mettre en avant: ...
- Préparer: ...
```

**Workflow `/job-analyze` :**

```markdown
# Workflow: Analyse d'offre d'emploi

## Input
- URL de l'offre OU texte copié-collé

## Étapes
1. Récupérer le contenu (WebFetch si URL)
2. Parser et structurer l'information
3. Identifier les exigences (must-have vs nice-to-have)
4. Extraire les mots-clés ATS
5. (Optionnel) Rechercher infos entreprise
6. Générer le rapport formaté
7. Sauvegarder dans data/applications/{id}/

## Output
- Rapport d'analyse structuré
- Fichier sauvegardé pour réutilisation
```

---

## Notes pour l'utilisateur

> Rappels, références, notes personnelles

**Utilisation prévue :**

```bash
# Analyser depuis une URL
/job-analyze https://www.linkedin.com/jobs/view/...

# Analyser depuis le presse-papier
/job-analyze
# (puis coller le texte de l'offre)
```

**Types d'offres à supporter :**

- LinkedIn
- Welcome to the Jungle
- Indeed
- Sites carrières d'entreprises
- Texte brut copié-collé

---

## Références externes

### Tâches liées

- [INF-008](./INF-008-architecture-skills-candidature.md) - Architecture globale (parent)
- [INF-010](./INF-010-skill-analyse-adequation.md) - Utilise les résultats de cette analyse

---

## Commits Git associés

### Commit final

```bash
git commit -m "feat(skills): ✨ add job posting analysis skill

- Parse job postings from URL or text
- Extract structured requirements and keywords
- Generate analysis report with ATS keywords
- Include company research integration

Closes INF-009"
```

---

## Tests / Vérifications

- [ ] Le skill parse correctement une offre LinkedIn
- [ ] Le skill parse correctement une offre texte brut
- [ ] Les exigences sont correctement catégorisées
- [ ] Les mots-clés ATS sont extraits
- [ ] Le rapport est bien formaté et lisible
- [ ] Les données sont sauvegardées correctement

---

## Historique des modifications

| Date | Action | Détails |
|------|--------|---------|
| 2025-11-25 | Création | Skill d'analyse d'offre d'emploi |

---

## Résultat final

[À remplir une fois la tâche terminée]
