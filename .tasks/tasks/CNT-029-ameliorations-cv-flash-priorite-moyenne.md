# CNT-029: Améliorations CV Flash (priorité moyenne)

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | CNT-029 |
| **Titre** | Améliorations CV Flash (priorité moyenne) |
| **Statut** | ⏳ À faire |
| **Priorité** | 🟡 Moyenne |
| **Trigramme** | CNT |
| **Section CV** | Multiple |
| **Créé le** | 2025-11-25 |
| **Cible** | 2025-12-05 |
| **Terminé le** | - |
| **Temps estimé** | 1h |
| **Temps réel** | - |
| **Branche nécessaire** | Non |

---

## Description

Implémenter les améliorations de priorité moyenne identifiées dans l'analyse CNT-015 du CV Flash.

### Contexte

Ces améliorations sont souhaitables mais non critiques. Elles permettent d'enrichir le CV avec des détails supplémentaires et d'améliorer la cohérence.

### Objectif

Traiter les 4 recommandations de priorité moyenne:

1. **R05 - Enseignement supérieur:** Ajouter le rôle d'intervenant enseignant
2. **R06 - Quantifier formation:** Ajouter métriques (~15 sessions/an depuis 2015)
3. **R07 - Design Thinking:** Ajouter aux compétences (pills)
4. **R08 - i-BP national:** Enrichir avec dimension nationale

---

## Sous-tâches

- [ ] Ajouter mention enseignement supérieur (si établissements connus)
- [ ] Quantifier l'activité de formation dans Upwiser (~15 sessions/an)
- [ ] Ajouter "Design Thinking" dans les pills de compétences
- [ ] Enrichir description i-BP avec "Communautés de Pratiques nationales"
- [ ] Vérifier la compilation du CV
- [ ] Valider le rendu PDF

---

## Notes pour Claude

> Instructions spécifiques pour l'assistance IA

**R05 - Enseignement supérieur:**
```typst
# Option: dans Upwiser ou nouvelle mention
- Intervenant en écoles d'ingénieurs et universités
```

**R06 - Quantifier formation:**
```typst
# Dans la description Upwiser, modifier:
- Animation de formations et d'ateliers sur l'agilité et le développement logiciel.
# En:
- Animation de formations (Agile, Lean, Design Thinking) : ~15 sessions/an depuis 2015.
```

**R07 - Design Thinking:**
```typst
# Ajouter dans item-pills (ligne ~69-88):
"Design Thinking",
```

**R08 - i-BP dimension nationale:**
```typst
# Enrichir la mission i-BP existante:
- Animation de Communautés de Pratiques nationales
- Mise en place des modèles agiles de collaboration avec les centres de services
```

**Fichiers à modifier:**

- [cv.typ](../../src/cv.typ) - Sidebar pills (ligne ~69-88)
- [cv.typ](../../src/cv.typ) - Section Upwiser (lignes 120-135)
- [cv.typ](../../src/cv.typ) - Mission i-BP (lignes 287-294)

---

## Notes pour l'utilisateur

> Rappels, références, notes personnelles

**Points d'attention:**

- Pour l'enseignement supérieur, vérifier les établissements exacts
- Les métriques de formation doivent être vérifiables
- Design Thinking complète le triptyque Agile/Lean/Design Thinking

**Source:**
Recommandations CNT-015-R05, R06, R07, R08 de l'analyse CV Flash

---

## Références externes

### Fichiers du projet

- [cv.typ:69-88](../../src/cv.typ#L69-L88) - Pills expertises
- [cv.typ:120-135](../../src/cv.typ#L120-L135) - Section Upwiser
- [cv.typ:287-294](../../src/cv.typ#L287-L294) - Mission i-BP

### Tâches liées

- [CNT-015](./CNT-015-analyse-cv-flash.md) - Analyse source
- [CNT-027](./CNT-027-ajouter-missions-clients-upwiser-manquantes.md) - Haute priorité
- [CNT-028](./CNT-028-ajouter-activites-communautaires-rayonnement.md) - Haute priorité

### Ressources

- Recommandations: CNT-015-R05, R06, R07, R08

---

## Commits Git associés

### Commit final

```bash
git commit -m "content(cv): ✨ apply medium priority improvements from CV Flash

- Added teaching in higher education mention
- Quantified training activity (~15 sessions/year)
- Added Design Thinking to skills
- Enriched i-BP with national scope

From CV Flash 2021 analysis (CNT-015-R05/R06/R07/R08)

Closes CNT-029"
```

---

## Tests / Vérifications

- [ ] Le CV compile sans erreur (`just build`)
- [ ] Le PDF s'affiche correctement
- [ ] Design Thinking apparaît dans les pills
- [ ] Les métriques de formation sont visibles
- [ ] La dimension nationale i-BP est ajoutée
- [ ] Les commits suivent la convention

---

## Historique des modifications

| Date | Action | Détails |
|------|--------|---------|
| 2025-11-25 | Création | Tâche créée depuis CNT-015-R05/R06/R07/R08 |

---

## Résultat final

[À remplir une fois la tâche terminée]
