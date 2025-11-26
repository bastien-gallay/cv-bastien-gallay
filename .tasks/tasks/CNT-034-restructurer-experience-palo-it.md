# CNT-034: Restructurer l'expérience PALO IT par résultats

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | CNT-034 |
| **Titre** | Restructurer l'expérience PALO IT par résultats (pas par tâches) |
| **Statut** | ✅ Terminé |
| **Priorité** | 🔴 Haute |
| **Trigramme** | CNT (Content) |
| **Section CV** | Experience |
| **Créé le** | 2025-11-25 |
| **Cible** | - |
| **Terminé le** | 2025-11-25 |
| **Temps estimé** | 1-2 heures |
| **Temps réel** | - |
| **Branche nécessaire** | Auto |

---

## Description

Réorganiser la section PALO IT (2021-2025) pour mettre en avant les résultats plutôt que les tâches.

### Contexte

**Audit novembre 2025:**

L'expérience PALO IT est la vitrine actuelle du CV. Elle doit être structurée par **Résultats** et non par tâches.

**Recommandations clés:**

1. **Mettre en avant l'IA:** Le framework Gen-e2 et les certifications GitHub Copilot sont des atouts majeurs → remonter en tête
2. **Business:** Valoriser le rôle au COMEX et le développement commercial (Presales 15k-500k€)
3. **Missions Clients:** Garder Bodic et Beta.gouv car elles prouvent le côté "Hands-on" (apprécié pour un CTO)

### Objectif

- Réorganiser par impact business, pas par chronologie de tâches
- Mettre l'IA et l'innovation en premier
- Garder les missions clients qui démontrent l'expertise technique
- Condenser sans perdre les métriques clés

---

## Sous-tâches

- [x] Analyser la structure actuelle de la section PALO IT
- [x] Identifier les 5-7 réalisations les plus impactantes
- [x] Réorganiser avec l'IA/Innovation en premier
- [x] Ajouter/mettre en avant les métriques business
- [x] Sélectionner 2-3 missions clients à garder (Bodic, Beta.gouv)
- [ ] Déplacer le détail des autres missions vers cv-exhaustive.typ (reporté à TPL-001)
- [x] Compiler et vérifier le rendu

---

## Notes pour Claude

> Instructions spécifiques pour l'assistance IA

**Structure recommandée (audit):**

```markdown
## PALO IT (02/2021 - 10/2025)
Consultant Technique Senior → Chief Technology Officer

### Innovation & IA (mettre en premier!)
- Conception de Gen-e2, framework de développement accéléré par IA
- 20-40 certifications GitHub Copilot délivrées
- Initiative Quantum Computing (stage 10 semaines)
- Partenariats: Scaleway, GitHub, Mistral

### Leadership & Business
- Direction stratégie technologique, participation au COMEX
- Contribution à 15% de croissance du CA
- Management de 50 professionnels techniques
- Presales: 6+ opportunités majeures (€15k-€500k+)

### Missions Clients (Hands-on)
- Bodic: Optimisation API 72ms, évolution vers External CTO
- Beta.gouv: Lead Developer MonEspaceNis2 (7 mois)
```

**Missions à conserver (prouvent le Hands-on):**

- Bodic (Technical Lead, External CTO) - Prouve expertise technique récente
- Beta.gouv (Lead Developer) - Prouve capacité à coder/architecturer

**Missions à déplacer vers exhaustive:**

- Systel (Team Coach)
- TopTex (Architecture API)
- Nalo (Coach Technique)

**Fichiers à modifier:**

- [src/cv.typ](../../src/cv.typ) - Section expérience PALO IT
- [src/cv-exhaustive.typ](../../src/cv-exhaustive.typ) - Créer si n'existe pas

---

## Notes pour l'utilisateur

> Rappels, références, notes personnelles

**Pourquoi cette réorganisation?**

Les recruteurs CTO recherchent:

1. Vision stratégique (COMEX, croissance)
2. Innovation (IA, nouvelles technos)
3. Capacité technique (hands-on)
4. Management (équipes, budget)

L'ordre actuel (chronologique par rôle) ne met pas ces éléments en avant.

**Trade-off:**

- Moins de détails sur les missions → mais impact plus fort
- Version exhaustive garde tout pour candidatures spécifiques

---

## Références externes

### Fichiers du projet

- [src/cv.typ](../../src/cv.typ) - Expérience PALO IT

### Tâches liées

- [CNT-033](./CNT-033-ameliorer-section-a-propos.md) - Améliorer "À propos" (métriques liées)
- [TPL-001](./TPL-001-cv-versions.md) - Versions courte/longue (structure)
- [LAY-002](./LAY-002-consolidation-sections-dupliquees.md) - Consolidation (complémentaire)

### Ressources

- Audit CV novembre 2025

---

## Commits Git associés

### Commit final

```bash
git commit -m "content(experience): ✏️ restructure PALO IT by results

- Prioritized AI/Innovation section (Gen-e2, Copilot)
- Added business metrics (15% growth, COMEX)
- Kept hands-on missions (Bodic, Beta.gouv)
- Moved other missions to exhaustive version

Closes CNT-034"
```

---

## Tests / Vérifications

- [x] Le CV compile sans erreur
- [x] L'IA/Innovation apparaît en premier
- [x] Les métriques business sont visibles
- [x] Les missions hands-on sont présentes
- [ ] Le contenu supprimé est dans cv-exhaustive.typ (reporté à TPL-001)

---

## Historique des modifications

| Date | Action | Détails |
|------|--------|---------|
| 2025-11-25 | Création | Tâche créée suite à audit CV |

---

## Résultat final

**Nouvelle structure PALO IT (version courte):**

1. *Innovation IA :* Gen-e2, Copilot, Partenariats (Scaleway, GitHub, Mistral)
2. *Leadership :* COMEX, 15% croissance, Management 50 personnes
3. *Business :* Presales €15k-€500k+, Quantum Computing
4. *Missions Clients :* Bodic (External CTO), Beta.gouv (Lead Dev)
5. *Stack :* Azure, AWS, OpenAI, etc.

**Améliorations:**

- IA/Innovation mise en premier (différenciation)
- Section condensée de 7 à 5 bullet points
- Seules les missions hands-on conservées (Bodic, Beta.gouv)
- Version détaillée conservée dans "Expérience détaillée"

**Note:** La création de cv-exhaustive.typ est reportée à TPL-001 (versions courte/longue)
