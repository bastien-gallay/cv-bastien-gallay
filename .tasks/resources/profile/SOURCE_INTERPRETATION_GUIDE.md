# Guide d'Interprétation des Sources

**Document méthodologique**
**Dernière mise à jour :** 24 novembre 2025
**Usage :** Interprétation correcte des sources pour mise à jour du profil professionnel

---

## 1. Objectif

Ce guide définit les règles d'interprétation des différentes sources (CV, LinkedIn, Journal CTO, analyses) pour éviter la sur-représentation ou sous-représentation des compétences et réalisations dans le profil professionnel.

**Principe fondamental :** La précision et l'honnêteté sont prioritaires sur l'exhaustivité. Il vaut mieux sous-estimer légèrement que surestimer une compétence.

---

## 2. Niveaux d'Expertise Définis

### 2.1 Pratique Directe (Hands-On)

**Définition :** Technologies et compétences pratiquées personnellement avec écriture de code ou mise en œuvre technique directe.

**Critères de qualification :**

- Code écrit personnellement
- Architecture conçue et implémentée directement
- Projets livrés avec contribution technique personnelle
- Capacité à résoudre des problèmes techniques complexes sans assistance

**Formulation dans le profil :**

- "Expertise en [technologie]"
- "[Technologie] : [détails techniques]"
- Sans qualificatif additionnel

**Exemples validés :**

- TypeScript, Python, C#, Rust (langages pratiqués chez PALO IT)
- OpenAI, Anthropic (LLMs utilisés dans Gen-e2)
- GitHub Copilot (certifications délivrées, usage personnel)
- DRM (intégration serveurs chez Boonty 2004-2006)

### 2.2 Architecture et Design

**Définition :** Conception d'architectures techniques sans nécessairement coder l'implémentation complète.

**Critères de qualification :**

- Décisions architecturales prises personnellement
- Conception de patterns et structures
- Revue de code et validation technique
- Capacité à expliquer les choix techniques et leurs trade-offs

**Formulation dans le profil :**

- "Architecture [pattern]"
- "Conception de [système]"
- "Revue d'architecture [contexte]"

**Exemples validés :**

- MAC (Model-Actor-Controller) avec BFF (revue architecture Systel)
- REST API, Microservices, SOA (conçu dans missions Cast et PALO IT)
- Multi-cloud (stratégie définie en tant que CTO)

### 2.3 Management Technique

**Définition :** Technologies pratiquées par les équipes managées, avec supervision, décisions stratégiques et validation par le manager.

**Critères de qualification :**

- Équipe directe pratique la technologie
- Supervision de projets utilisant la technologie
- Décisions sur choix technologiques
- Capacité à évaluer compétences techniques des équipes
- Compréhension des concepts et cas d'usage

**Formulation dans le profil :**

- "Connaissance via management d'équipe"
- "Technologies pratiquées par équipes managées"
- "Supervision de projets [technologie]"

**Exemples validés :**

- **Bases de données vectorielles** (OpenSearch, Pinecone, AWS Kendra, PGVector) : Équipes PALO IT les ont pratiquées, management et supervision des projets
- **LangChain** : Framework utilisé par l'équipe dans projets Gen-e2
- **AWS Bedrock** : Évalué en presales, pas de mise en œuvre directe

### 2.4 Presales et Évaluation

**Définition :** Technologies rencontrées lors d'appels d'offre, études de faisabilité, estimations de projets, sans mise en œuvre.

**Critères de qualification :**

- Participation à des appels d'offre
- Études de faisabilité technique
- Estimations de charge et ROI
- Connaissance théorique des concepts
- Pas de mise en œuvre concrète

**Formulation dans le profil :**

- "Évalué en presales"
- "Étude de faisabilité [projet]"
- "Estimation [contexte]"
- Ne PAS inclure dans section "Compétences" sauf mention explicite

**Exemples validés :**

- **Unreal Engine UE3→UE5.5** : Étude presales pour projet Virtuos (60 personnes-mois estimés), pas de mise en œuvre
- **AWS Bedrock** : Évalué en presales pour projets AI/ML
- **Divers projets presales** : Natixis, Groupe BZ, CEVA Logistics, Virtuos (études, pas livrés)

---

## 3. Clarifications Utilisateur Documentées

### 3.1 Technologies AI/ML (Novembre 2025)

**Clarification :**

> "Je les ai rencontrés en appel d'offre et mes collègues/subordonnés les ont pratiqués, mais je ne les ai jamais pratiqués, voir jamais appris pour certains."

**Technologies concernées :**

- Bases de données vectorielles : OpenSearch, Pinecone, AWS Kendra, PGVector
- Frameworks ML : LangChain
- AWS : Bedrock (AI/ML services)

**Niveau d'expertise qualifié :** Management Technique + Presales

**Traitement dans le profil :**

- Déplacées vers section "Connaissance via management d'équipe et presales"
- Retirées des listes de compétences directes
- Contexte précisé : "(équipes managées)" ou "(évalué en presales)"

### 3.2 Unreal Engine (Novembre 2025)

**Clarification :**

> "C'était juste une étude, je n'ai pas fait la mise en œuvre"

**Projet concerné :** Migration UE3→UE5.5 pour portage de jeux (projet Virtuos, 60 personnes-mois)

**Niveau d'expertise qualifié :** Presales et Évaluation uniquement

**Traitement dans le profil :**

- Retiré de la section "Compétences Techniques > Développement de Jeux Vidéo"
- Retiré de la section Technologies PALO IT CTO
- Modifié dans "Réalisations Clés" : "**Étude presales** migration Unreal Engine pour portage de jeux (estimation 60 personnes-mois, projet Virtuos)"

### 3.3 Expérience DRM (Validée)

**Projet concerné :** Intégration serveurs DRM chez Boonty (2004-2006)

**Technologies :** Macrovision, Starforce, Sony/SecuROM

**Niveau d'expertise qualifié :** Pratique Directe

**Traitement dans le profil :** Conservé dans "Compétences Techniques > Développement de Jeux Vidéo" avec contexte "Expérience Boonty (2004-2006)"

---

## 4. Règles d'Interprétation par Source

### 4.1 CV Typst 2025 (src/cv.typ)

**Caractéristiques :**

- Document actuel, optimisé pour recrutement
- Focus sur expériences récentes et compétences actuelles
- Descriptions génériques par choix éditorial

**Règles d'interprétation :**

- ✅ Technologies listées = Expertise directe ou Architecture/Design
- ✅ Réalisations mentionnées = Livrées et validées
- ⚠️ Descriptions courtes ≠ Manque de détails, vérifier autres sources
- ⚠️ Absences possibles = Choix éditoriaux, pas forcément gaps

**Exemple :** Skills pills dans CV (TypeScript, Python, Rust, etc.) = Technologies pratiquées directement

### 4.2 Profil LinkedIn

**Caractéristiques :**

- Historique complet de carrière
- Endorsements = Validation communautaire
- Recommandations = Témoignages vérifiables
- Peut contenir des simplifications

**Règles d'interprétation :**

- ✅ Positions listées = Confirmées et vérifiables
- ✅ Endorsements élevés (>10) = Compétence reconnue publiquement
- ✅ Recommandations écrites = Témoignages factuels prioritaires
- ⚠️ Skills sans endorsements = À vérifier dans autres sources
- ⚠️ Dates parfois arrondies = Vérifier précision dans autres docs

**Exemple :** Scrum (93 endorsements) = Expertise reconnue, niveau élevé confirmé

### 4.3 CV 2019

**Caractéristiques :**

- Détails exhaustifs des missions Upwiser et Cast
- Format long avec descriptions techniques complètes
- Contextes métiers précisés
- Dernier CV détaillé avant passage PALO IT

**Règles d'interprétation :**

- ✅ Missions avec "Contexte" technique = Technologies pratiquées
- ✅ Réalisations quantifiées = Chiffres exacts et vérifiables
- ✅ Clients nommés = Missions réelles et traçables
- ✅ Technologies dans contexte = Niveau Pratique Directe
- ⚠️ Certifications avec dates 2015-2018 = Certaines expirées, vérifier validité

**Exemple :** Mission i-BP avec contexte "Coaching, Scrum, Kanban, LeSS, Feature Teams, multi-sites, secteur bancaire" = Toutes technologies pratiquées

### 4.4 Journal CTO PALO IT (Mars-Juillet 2025)

**Caractéristiques :**

- Notes quotidiennes d'activités
- Mélange projets livrés ET études presales
- Détails techniques et business
- Source la plus récente et détaillée pour période PALO IT

**Règles d'interprétation :**

- ✅ Projets avec "livrables" = Mise en œuvre réelle
- ⚠️ Projets avec "presales", "étude", "RFP" = Pas de livraison, niveau Presales uniquement
- ⚠️ "En attente de Go" = Étude, pas réalisation
- ⚠️ Technologies mentionnées = Vérifier si pratique directe ou équipe
- ✅ Métriques business (15% croissance, etc.) = Factuelles et vérifiables

**Exemples :**

- ✅ Bodic/Armen : "Livraison réussie add-in Outlook" + "API 72ms" = Projet livré, réalisation validée
- ✅ Systel : "Coaching quotidien 3 jours/semaine" = Mission livrée
- ⚠️ Virtuos : "RFP", "portage de jeux UE3→UE5.5", "60 personnes-mois" = Étude presales uniquement
- ⚠️ Natixis : "Budget validé", "Q3 2025" = Presales, statut livraison inconnu

### 4.5 Analyses Comparatives (CNT-001, CNT-013, CNT-014)

**Caractéristiques :**

- Rapports d'audit entre sources
- Identifient gaps et incohérences
- Recommandations de corrections
- Méthodologie documentée

**Règles d'interprétation :**

- ✅ Gaps identifiés = À vérifier avec utilisateur avant ajout
- ✅ Incohérences datées = Nécessitent clarification
- ⚠️ Recommandations = Suggestions, pas faits établis
- ✅ Scores de cohérence = Indicateurs de fiabilité des sources

**Exemple :** CNT-013 identifie perte de détails missions Cast → Restaurer détails du CV 2019 après validation

---

## 5. Matrice de Qualification des Compétences

### Comment qualifier une nouvelle technologie ou compétence ?

| Critère | Pratique Directe | Architecture/Design | Management Technique | Presales/Évaluation |
|---------|------------------|---------------------|----------------------|---------------------|
| **Code écrit personnellement** | ✅ Oui | ❌ Non | ❌ Non | ❌ Non |
| **Architecture conçue** | ✅ Souvent | ✅ Oui | ⚠️ Validée | ⚠️ Étudiée |
| **Équipe pratique sous supervision** | ➖ N/A | ⚠️ Possible | ✅ Oui | ❌ Non |
| **Projet livré en production** | ✅ Oui | ✅ Oui | ✅ Oui | ❌ Non |
| **Étude/RFP uniquement** | ❌ Non | ❌ Non | ❌ Non | ✅ Oui |
| **Capacité résolution problèmes** | ✅ Autonome | ✅ Avec équipe | ⚠️ Via équipe | ❌ Théorique |
| **Durée d'expérience minimum** | 3+ mois | 1+ mois | 6+ mois | N/A |

### Exemple d'Application

**Technologie à qualifier :** LangChain (framework ML)

**Questions à poser :**

1. Ai-je écrit du code LangChain moi-même ? → ❌ Non
2. Ai-je conçu des architectures utilisant LangChain ? → ⚠️ Validé architectures d'équipe
3. Mon équipe a-t-elle utilisé LangChain sous ma supervision ? → ✅ Oui, dans projets Gen-e2
4. Des projets ont-ils été livrés en production ? → ✅ Oui, projets Gen-e2
5. S'agit-il uniquement d'études presales ? → ❌ Non, projets livrés

**Qualification résultante :** Management Technique

**Formulation dans profil :** "Frameworks ML : LangChain (projets d'équipe)"

---

## 6. Processus de Mise à Jour du Profil

### 6.1 Ajout d'une Nouvelle Compétence

**Étape 1 : Qualification**

- Utiliser la matrice de qualification (Section 5)
- Identifier le niveau d'expertise exact
- Vérifier la durée et l'intensité d'expérience

**Étape 2 : Contextualisation**

- Identifier le projet/contexte d'acquisition
- Vérifier si livré ou presales
- Préciser la période temporelle

**Étape 3 : Formulation**

- Choisir la section appropriée dans le profil
- Utiliser la formulation adaptée au niveau (Section 2)
- Ajouter contexte si nécessaire

**Étape 4 : Vérification croisée**

- Cohérence avec autres compétences du même niveau
- Pas de sur-représentation vs expériences décrites
- Traçabilité dans au moins une source documentée

### 6.2 Ajout d'une Nouvelle Réalisation

**Étape 1 : Validation factuelle**

- Le projet a-t-il été livré en production ? (Oui/Non)
- S'agit-il d'une étude/RFP ? (Oui/Non)
- Les chiffres sont-ils vérifiables dans sources ? (Oui/Non)

**Étape 2 : Formulation selon type**

**Si projet livré :**

- "[Métrique] : [Description] ([Contexte/Client])"
- Exemple : "72ms : Temps de réponse API optimisé (projet Bodic/Armen)"

**Si étude presales :**

- "[Métrique] : **Étude presales** [Description] (estimation [chiffre], [Contexte])"
- Exemple : "UE3→UE5.5 : Étude presales migration Unreal Engine (estimation 60 personnes-mois, projet Virtuos)"

**Si en cours :**

- Ne PAS ajouter aux réalisations, mentionner dans description de poste uniquement

**Étape 3 : Quantification**

- Privilégier métriques mesurables (€, %, ms, nombre de personnes, durée)
- Si pas de chiffre exact : estimer ou ne pas quantifier
- Préciser nature de la métrique (réel vs estimation)

### 6.3 Correction d'une Incohérence

**Étape 1 : Identification source fiable**

Ordre de priorité des sources :

1. Clarifications directes utilisateur (priorité absolue)
2. Documents officiels (contrats, certifications)
3. Journal CTO / Notes contemporaines
4. CV historiques avec détails techniques
5. LinkedIn (validation communautaire)

**Étape 2 : Correction**

- Corriger dans professional-profile.md
- Documenter la correction dans ce guide (Section 3 "Clarifications")
- Ajouter date de correction

**Étape 3 : Propagation**

- Vérifier autres occurrences dans le document
- Vérifier cohérence dans CV Typst si applicable
- Mettre à jour analyses si nécessaire

---

## 7. Cas d'Usage et Exemples

### 7.1 Cas : Technologie Rencontrée en Presales

**Situation :** Une technologie X apparaît dans le journal CTO dans le contexte d'un appel d'offre, sans mention de livraison.

**Questions à poser :**

1. Le projet a-t-il été gagné et livré ? → Vérifier statut dans sources
2. Ai-je personnellement pratiqué la technologie ? → Clarifier avec utilisateur si doute
3. Une équipe a-t-elle livré un projet avec cette techno ? → Vérifier dans journal/rapports

**Décisions possibles :**

- ✅ Projet gagné + livré + équipe pratique → Management Technique
- ⚠️ Projet gagné + livré + pratique directe → Pratique Directe
- ❌ Projet non gagné ou étude uniquement → Presales (ne pas ajouter aux compétences, uniquement mentionner dans presales si pertinent)

### 7.2 Cas : Compétence avec Endorsements LinkedIn

**Situation :** Une compétence a 50+ endorsements sur LinkedIn mais n'apparaît pas dans CV actuel.

**Questions à poser :**

1. La compétence est-elle encore pertinente/actuelle ? → Vérifier dernière utilisation
2. Y a-t-il des projets documentés utilisant cette compétence ? → Chercher dans CV 2019, journal
3. Le niveau d'expertise est-il suffisant pour valoriser ? → Évaluer selon matrice

**Décisions possibles :**

- ✅ Pertinent + documenté + niveau suffisant → Ajouter au profil
- ⚠️ Pertinent mais ancien (>5 ans) → Ajouter avec mention "Maîtrise historique"
- ❌ Non pertinent pour objectif actuel → Ne pas ajouter (choix éditorial)

### 7.3 Cas : Réalisation Business Sans Détails Techniques

**Situation :** "15% de croissance de chiffre d'affaires" mentionné dans journal CTO.

**Questions à poser :**

1. Le chiffre est-il confirmé officiellement ? → Vérifier source (townhall, rapport)
2. Ma contribution est-elle directe ou indirecte ? → Qualifier niveau d'impact
3. Le contexte est-il clair pour lecteur externe ? → Ajouter précisions si nécessaire

**Décisions possibles :**

- ✅ Chiffre officiel + contribution claire → Ajouter tel quel avec source
- ⚠️ Chiffre estimé → Préciser "environ", "~", "estimation"
- ⚠️ Contribution indirecte → Préciser contexte (ex: "annoncé en townhall", "équipe a contribué à")

---

## 8. Maintenance de ce Guide

### 8.1 Quand Mettre à Jour ce Guide ?

**Obligatoire :**

- Nouvelle clarification utilisateur sur niveau d'expertise
- Identification d'erreur d'interprétation dans profil
- Ajout d'une nouvelle source de données (nouveau CV, nouveau journal, etc.)

**Recommandé :**

- Ajout d'un nouveau cas d'usage complexe
- Évolution des critères de qualification (changement de rôle, de contexte)
- Retour utilisateur sur ambiguïté dans formulations

### 8.2 Structure des Clarifications (Section 3)

Pour chaque nouvelle clarification, documenter :

```markdown
### X.X [Technologie/Projet] ([Date])

**Clarification :**
> [Citation exacte utilisateur]

**Technologies/Projets concernés :**
- [Liste détaillée]

**Niveau d'expertise qualifié :** [Pratique Directe / Architecture / Management / Presales]

**Traitement dans le profil :**
- [Action 1]
- [Action 2]
- [Action N]
```

### 8.3 Revue Périodique

**Fréquence recommandée :** Tous les 6 mois ou à chaque mise à jour majeure du profil

**Points à vérifier :**

- ✅ Cohérence entre ce guide et professional-profile.md
- ✅ Nouvelles technologies/compétences nécessitant qualification
- ✅ Clarifications anciennes toujours pertinentes
- ✅ Exemples à jour avec état actuel du profil

---

## 9. Checklist de Validation

### Avant de publier/diffuser le profil professionnel

- [ ] Toutes les compétences listées correspondent à un niveau d'expertise qualifié
- [ ] Aucune technologie presales-only dans section "Compétences"
- [ ] Toutes les réalisations sont soit livrées, soit explicitement marquées "étude/presales"
- [ ] Les chiffres quantifiés sont tracés dans au moins une source documentée
- [ ] Les clarifications utilisateur sont toutes appliquées
- [ ] Aucune contradiction entre sections du document
- [ ] Dates cohérentes et vérifiées
- [ ] Clients/projets nommés sont vérifiables dans sources

### Avant d'ajouter une nouvelle technologie

- [ ] Niveau d'expertise qualifié selon matrice (Section 5)
- [ ] Contexte d'acquisition identifié et documenté
- [ ] Formulation adaptée au niveau choisie (Section 2)
- [ ] Cohérence vérifiée avec autres compétences similaires
- [ ] Durée minimale d'expérience respectée si applicable

### Avant d'ajouter une nouvelle réalisation

- [ ] Nature validée : livré en production OU étude presales
- [ ] Formulation adaptée selon nature (Section 6.2)
- [ ] Chiffres vérifiés dans sources
- [ ] Contexte/client précisé si pertinent
- [ ] Métrique mesurable ou estimation clarifiée

---

## 10. Résumé des Règles d'Or

1. **Honnêteté absolue** : En cas de doute, sous-estimer plutôt que surestimer
2. **Traçabilité** : Toute information doit être traçable dans une source documentée
3. **Clarifications prioritaires** : Les clarifications directes utilisateur sont la source ultime de vérité
4. **Distinction niveaux** : Toujours qualifier le niveau d'expertise (Pratique / Architecture / Management / Presales)
5. **Presales ≠ Compétence** : Les études presales ne sont PAS des compétences à lister
6. **Contexte obligatoire** : Management et Presales nécessitent précision du contexte
7. **Quantification prudente** : Estimations à préciser explicitement ("estimation", "environ", "~")
8. **Validation croisée** : Vérifier cohérence entre toutes sections du profil
9. **Documentation continue** : Documenter toute clarification dans ce guide (Section 3)
10. **Revue régulière** : Revoir ce guide tous les 6 mois

---

**Document créé le :** 24 novembre 2025
**Dernière révision :** 24 novembre 2025
**Auteur :** Bastien Gallay (avec assistance Claude Code)
**Version :** 1.0
