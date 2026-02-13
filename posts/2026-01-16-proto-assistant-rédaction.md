# Proto assistant de rédaction

Texte rédigé: [2026-01-16-linkedin-infos-resultat.md](2026-01-16-linkedin-infos-resultat.md)

Fichier de suivi du processus: [2026-01-16-linkedin-infos-session.md](2026-01-16-linkedin-infos-session.md)

## Prompt initial

```text
Nous allons maintenant nous ateler au naratif sur linkedin, pour la section "Infos". Pour cela, je vais avoir besoin d'une aide à la rédaction. Je souhaite rédiger moi-même, mais avec ton aide. Pose-moi des questions et fais-moi des propositions afin de créer un texte complet composé à partir de mes réponses.

Règles à suivre:
- Suggère des options pour le plan, la structure et l'orientation des phrases
- Ajoute des rappels de mots-clés, décisions prises sur le contenu, facteurs de cohérences, faits importants concernant cette section linkedin
- Découpe la rédaction collaborative en itération; chaque itération représentant une majeure décision de structure, un paragraphe ou une phrase
- Ne rédige jamais directement le contenu
- Effectue une critique construite de mes rédaction avec des techniques comme: avocat du diable, first-principle, reader's journey map, analyse de cohérence, ou une autre qui te semble pertinente. Choisis le type d'analyse en fonction des éléments à revoir, de manière à être pertinent et avoir des analyses diversifiées tout au long du processus.
- Le plan d'avancement doit laisser de la place à de la découverte et de la surprise : dans la planification, crée des étapes qui changeront la suite ; garde le choix des types d'analyse critique pour le dernier moment, c'est à dire après ma réponse
- Enregristre les points importants de la rédaction dans un fichier : questions posées, réponses, analyses, choix de réorientation
- Crée un fichier contenant le résultat
```

## Processus proposé après réajustement

```text
┌─────────────────────────────────────────────────────────────┐
│  1. QUESTION / PROPOSITION                                  │
│     → Options avec exemples concrets                        │
│     → Rappels (mots-clés, décisions, cohérence)             │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│  2. RÉPONSE UTILISATEUR                                     │
│     → Choix ou rédaction                                    │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│  3. ANALYSE CRITIQUE                                        │
│     → Technique variée (avocat du diable, cohérence, etc.)  │
│     → Verdict : ✅ OK ou ⚠️ Ajustement suggéré              │
└─────────────────────────────────────────────────────────────┘
                            ↓
              ┌─────────────────────────────┐
              │  Problème détecté ?         │
              └─────────────────────────────┘
                    │              │
                   Non            Oui
                    ↓              ↓
┌──────────────────────┐   ┌─────────────────────────────────┐
│  4. ENREGISTREMENT   │   │  4. DEMANDE D'AJUSTEMENT        │
│     → Décision       │   │     → Problème identifié        │
│       validée        │   │     → Suggestions concrètes     │
└──────────────────────┘   │     → Retour à l'étape 2        │
                           └─────────────────────────────────┘
```

## Impressions et résultats

### Impressions générales

Au début, l'assistant a laissé beaucoup de place à mes rédactions. Par la suite, lui ayant demandé des exemples pour les options qu'il me proposait, il a commencé à écrire des phrases complètes que je devais ensuite ajuster. La plus grande partie du texte étant écrite, cela n'a pas été très gênant. Mais j'ai quand même dû me forcer à ré-écrire certaines parties pour éviter l'influence trop forte de l'IA.

### Points positifs

- Le processus est très motivant: chaque étape est claire, et le temps d'analyse est court.
- Les blocs rédigés à chaque itération sont réaffichés
- Le fichier de suivi est clair et utile pour suivre le progression, même après interuption
- L'analyse critique est pertinente et montrée clairement dans le fichier de suivi
- Travailler par petits blocs permet de se focaliser sur cette partie, et de surmonter les difficultés de rédaction et de parasitage cognitif
- Les itérations sont courtes, ce qui donne une capacité de switch très grande, mais aussi de ne pas se disperser
- Les itérations sont émergentes, et donne beaucoup de place à la découverte
- Les analyses sont bien décidées au dernier moment, ce qui permet de garder la surprise et la fraîcheur

### Points négatifs

- Tendance à faire des propositions complètes sur la fin, au lieu de simples options
- Malgré le suivi dans le fichier, il est parfois difficile de savoir où on en est et ce qu'il reste à faire
- La phase d'analyse n'est pas assez visible dans l'interface de chat, obligeant à aller voir le fichier de suivi pour comprendre les critiques
- Léger manque d'interactivité par moment, mais c'est mieux que trop d'interactivité
- Certaines itérations n'ont pas bénéficié d'une analyse critique: l'une car elle a été découpée en plusieurs sous-itérations, l'autre était la dernière.

## Prochaines étapes

### Recherches à faire

- Le mode "learning" de Claude doit avoir des pistes intéressantes
- Le repo qui refait le "learning mode" de Claude en open source aussi
- Le module rédactionnel de BMAD

### Idées d'amélioration

- Préciser que les exemples doivent être des propositions partielles
- S'assurer que les exemples sont donnés dans un contexte différent (donner quelques exemples, ou demander un scénario différent)
- Prompter une sorte de jeu où l'IA démarre les phrases, ou fais un texte à trous pour les moments de page blanche
- Interactions
  - Permettre de notifier une étape importante, au niveau de l'itération, afin de déclencher un processus plus détaillé (choix du type d'analyse, redécoupage, revue de cohérence globale, etc.)
  - Lors d'une itération importante, réafficher tout le texte et demander confirmation de la partie qui vient d'être écrite
  - Une fois toutes les 2-3 itérations, réafficher le texte complet pour validation
  - Utiliser le mode interactif de Clande (si possible) pour avoir un vrai échange en temps réel
- Affichages dans le chat
  - Réafficher un résumé des étapes restantes à chaque itération (Jauge ASCII ?)
  - Afficher l'analyse critique directement dans le chat, pas seulement dans le fichier de suivi
  - Ajouter des petites phrases de motivation ou d'encouragement entre les étapes, en lien avec le texte en cours de rédaction
- Analyse critique:
  - La rendre plus systématique, même sur les itérations redécoupées
  - Ajouter des techniques d'analyse supplémentaires, comme la carte d'empathie, l'analyse SWOT, ou la matrice d'impact/effort
  - Proposer une itération dédiée à une technique d'analyse en fin de rédaction, avec plus de choix et d'interactivité
  - Préciser les critères de choix de la technique d'analyse en fonction du contexte, pour permettre à l'IA de mieux choisir
- Fichier de suivi
  - Ajouter un sommaire automatique avec liens vers les étapes
  - Ajouter une section "Prochaines étapes" pour chaque itération, avec les actions à faire ensuite
  - Fournir un template de fichier et d'itération, pour assurer la cohérence et réduire l'errance générative
  - Ajouter un horodatage pour les itérations (début/fin)
- Disruptif
  - Ecrire dans un fichier séparé le texte complet généré par l'IA avant la première itération, pour analyser en fin de rédaction (influence, style, gain de style, etc.)
  - "Reformuler comme..." : une possibilité de reformuler un texte comme un auteur célèbre, un enfant, un robot, un archétype, etc.
  - Des "modes" de rédaction : texte limité en taille, texte chapitré, texte à intégrer avec des visuels, etc.

### Opportunités de réutilisation

- Ecrire un post LinkedIn
- Ecrire un article de blog
- Description d'un projet en cours
- En collaboration avec des collègues sur l'audit en cours
