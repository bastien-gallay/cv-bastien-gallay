// CV adapté pour: Expert AI Engineering & Audit Technique @ Egis Group
// Via: Teragone Factory
// Date: 2026-03-17
// Score d'adéquation: 89/100
// Cible: 2 pages

#import "../../../src/neat-cv-local.typ": (
  cv-continued, cv-page-one, cv-setup, email-link, entry,
  contact-info, item-pills, social-links,
)

// Configuration de base
#import "../../../src/shared/config.typ": *

// =============================================================================
// MÉTADONNÉES DOCUMENT
// =============================================================================

#set document(
  title: "CV - Bastien Gallay - Expert AI Engineering & Audit Technique @ Egis Group",
  author: "Bastien Gallay",
  date: datetime.today(),
)

// =============================================================================
// CONFIGURATION ADAPTÉE
// =============================================================================

#let author-adapted = (
  ..author-config,
  position: "Expert AI Engineering & Audit Technique | Formation & Accompagnement",
)

// =============================================================================
// SIDEBAR ADAPTÉE
// =============================================================================

#let sidebar-adapted() = [
  = A propos
  Expert AI Engineering, 23 ans d'expérience. Ambassadeur Gen-e2 en France et praticien Specification Driven Development (BMAD, OpenSpec, SpecKit, framework SDD personnel). Audit technique de plateformes. Formation et coaching d'équipes sur les pratiques AI Engineering et code quality.

  = Informations
  Nationalité : Français

  #social-links()

  - *Français :* Langue maternelle
  - *Anglais :* Courant

  = AI Engineering
  #item-pills((
    "LLM",
    "Claude",
    "Copilot",
    "Cursor",
    "GenAI Dev",
    "Python",
    "TypeScript",
  ))

  = Méthodologie
  #item-pills((
    "Spec Driven Dev",
    "AI Code Quality",
    "Craftsmanship",
    "TDD",
    "Code Review",
  ))

  = Leadership
  #item-pills((
    "Formation",
    "Coaching",
    "Audit",
    "Management",
  ))

  = Rayonnement
  - Mentor Google Launchpad
  - Orateur Agile Tour & Scrum Day
]

// =============================================================================
// EXPÉRIENCES PAGE 1 - PAR PERTINENCE (compact)
// =============================================================================

#let experiences-adapted-page1 = [
  = Expérience Professionnelle

  #entry(
    title: [Consultant Architecture & Audit],
    date: [10/2025 - Aujourd'hui],
    institution: [Teragone Factory / Indépendant],
    location: [Remote-Bordeaux],
  )[
    - *Berger-Levrault - Audit plateforme (3 mois) :* Audit d'obsolescence, d'architecture et d'organisation humaine sur 2 produits majeurs. Recommandations d'évolution technique et organisationnelle. #strong[Stack :] Java 8/25, Spring Boot, Oracle.
    - *CISAC - Audit ISWC (2 mois) :* Audit technique de la plateforme ISWC. Évaluation qualité du code et des pratiques de développement. #strong[Stack :] Azure Databricks, Cosmos DB.
  ]

  #entry(
    title: [Projets personnels - AI Engineering & SDD],
    date: [2025 - Aujourd'hui],
    institution: [Side projects],
    location: [Remote],
  )[
    - Multiples projets Specification Driven Development (BMAD, OpenSpec, SpecKit, framework SDD personnel) : analyseur rhétorique (détection arguments fallacieux), prototype jeu vidéo, gestion documentaire, générateur de musique.
  ]

  #entry(
    title: [Consultant Technique Senior → CTO],
    date: [02/2021 - 08/2025],
    institution: [PALO IT],
    location: [Bordeaux/Paris],
  )[
    - *AI Engineering :* Ambassadeur Gen-e2 en France et fort contributeur. Partenariats GitHub, Microsoft. Négociations avancées : Mistral, Anthropic, Scaleway, OVH, MongoDB.
    - *Formation AI Engineering :* 20-40 certifications GitHub Copilot délivrées. Learn & Lunch hebdomadaires IA. Tech\&Toast 70+ professionnels. Accompagnement des équipes sur les bonnes pratiques AI-assisted development.
    - *Coaching technique :* Coaching CTO Nalo (Craftsmanship, TDD, DDD) et équipe Systel (3 dev, audit acquisition).
    - *CTO & Management :* Direction stratégie technologique, COMEX, 50 personnes. Presales €15k-€500k+.
  ]

  #entry(
    title: [Gérant, Coach Agile & Formateur],
    date: [09/2013 - 02/2021],
    institution: [Upwiser],
    location: [Bordeaux],
  )[
    - Coaching et formation Agile auprès de grands comptes et startups (~100 accompagnements).
    - Missions : DEKRA, i-BP, Dronisos, Mieux Placer, Wanteeed, SeLoger.
  ]

  #entry(
    title: [Chef de projet technique et Scrum Master],
    date: [10/2010 - 10/2013],
    institution: [CDiscount],
    location: [Bordeaux],
  )[
    - Plateforme paiement (*1 milliard € CA*). Équipe 15 personnes. #strong[Stack :] C\#, .Net, SQL Server.
  ]

  #entry(
    title: [Consultant Technique],
    date: [08/2006 - 09/2010],
    institution: [Cast Consulting],
    location: [Paris],
  )[
    - Projets internationaux (JOA Online, Pixmania). Coordination équipes distribuées Europe (France, Portugal, Londres).
  ]
]

// =============================================================================
// SECTIONS PAGE 1
// =============================================================================

#let sections-adapted = [
  = Formation

  #entry(
    title: [DEA Réalité Virtuelle et Maîtrise des Systèmes Complexes - Mention Bien],
    date: [2002],
    institution: [INSTN (CEA Saclay)],
    location: [Saclay],
  )[]

  #entry(
    title: [Maîtrise d'Informatique - Mention Bien],
    date: [2001],
    institution: [Université de Picardie Jules Verne],
    location: [Amiens],
  )[]

  = Certifications

  #entry(
    title: [SAFe Program Consultant (SPC5)],
    date: [2020],
    institution: [Scaled Agile, Inc.],
  )[]

  #entry(
    title: [Professional Scrum Master (PSM I & II) & Developer (PSD-I)],
    date: [2015-2018],
    institution: [Scrum.org],
  )[]
]

// =============================================================================
// LOGO TERAGONE FACTORY (cropped)
// =============================================================================

#let teragone-logo = box(
  fill: white,
  radius: 3pt,
  inset: (x: 5pt, y: 4pt),
  box(
    clip: true,
    width: 2.8cm,
    inset: (left: -18%, right: -10%, top: -22%, bottom: -22%),
    image("../../../src/assets/logo-teragone-factory.png"),
  ),
)

// =============================================================================
// DOCUMENT - PAGE 1
// =============================================================================

#show: cv-setup.with(
  author: author-adapted,
  accent-color: accent-color,
  header-color: header-color,
  body-font: body-font,
  body-font-size: body-font-size,
  paper-size: paper-size,
  side-width: side-width,
)

#cv-page-one(
  profile-picture: image("../../../src/assets/photo-profile-pro.jpg"),
  header-logo: teragone-logo,
  sidebar-adapted(),
  [
    #experiences-adapted-page1
    #sections-adapted
  ],
)

// =============================================================================
// PAGE 2 - EXPÉRIENCE DÉTAILLÉE (chronologique inverse, compact)
// =============================================================================

#pagebreak()

#cv-continued[

  = Expérience détaillée

  #entry(
    title: [Consultant Architecture Senior - Audit de plateforme],
    date: [11/2025 - 02/2026],
    institution: [Berger-Levrault],
    location: [Remote / Bordeaux],
  )[
    Audit d'obsolescence, d'architecture et d'organisation humaine sur 2 produits majeurs (RH, Gestion Financière) pour des collectivités de taille moyenne et grande.
    - Analyse obsolescence technologique (Java 8 → Java 25), revue d'architecture applicative
    - Évaluation de l'organisation des équipes, recommandations d'évolution
    - #strong[Stack :] Java 8, Java 25, Spring Boot, Python, Oracle
  ]

  #entry(
    title: [Auditeur Technique - Plateforme ISWC],
    date: [10/2025 - 11/2025],
    institution: [CISAC],
    location: [Remote / Bordeaux],
  )[
    Audit technique de la plateforme ISWC pour la Confédération Internationale des Sociétés d'Auteurs et Compositeurs.
    - Analyse de l'architecture cloud Azure (Databricks, Cosmos DB)
    - Évaluation de la qualité du code et des pratiques de développement
    - #strong[Domaine :] Droits d'auteur, standards internationaux (ISWC)
  ]

  #entry(
    title: [Projets personnels - AI Engineering & SDD],
    date: [2025 - Aujourd'hui],
    institution: [Side projects],
    location: [Remote],
  )[
    Pratique intensive du Specification Driven Development sur des projets variés avec différents frameworks :
    - *Analyseur de rhétorique :* Détection d'arguments fallacieux à partir d'articles de presse. #strong[Framework :] SpecKit (et Lovable)
    - *Prototype jeu vidéo :* Développement piloté par spécifications. #strong[Framework :] BMAD
    - *Gestion documentaire :* Documents personnels dont CV. #strong[Framework :] Custom
    - *Générateur de musique :* Création musicale exploitant des modèles existants #strong[Framework :] OpenSpec
    - *Framework SDD personnel :* Création d'un mini framework Specification Driven Development
  ]

  #entry(
    title: [Chief Technology Officer (CTO)],
    date: [10/2024 - 08/2025],
    institution: [PALO IT],
    location: [Bordeaux/Paris],
  )[
    Direction stratégie technologique, COMEX. Management 50 professionnels techniques.
    - Ambassadeur Gen-e2 en France et fort contributeur. Specification Driven Development : spécifications structurées → génération LLM → validation qualité
    - Formation AI Engineering : 20-40 certifications GitHub Copilot délivrées, Learn & Lunch hebdomadaires, ateliers hands-on prompt engineering et AI-assisted development
    - Partenariats GitHub (Copilot), Microsoft. Négociations avancées : Mistral (Codestral), Anthropic (Claude), Scaleway, OVH, MongoDB
    - Pilotage 6+ opportunités presales (€15k-€500k+) : Natixis, CEVA Logistics, Aviva
  ]

  #entry(
    title: [Coach Technique - Audit acquisition],
    date: [2025],
    institution: [Systel (via PALO IT)],
    location: [Bordeaux],
  )[
    - Coaching équipe 3 développeurs, audit technique dans le cadre d'une acquisition. #strong[Stack :] Java, Angular, Spring Boot.
  ]

  #entry(
    title: [Lead Developer - MonEspaceNis2],
    date: [09/2023 - 03/2024],
    institution: [Beta.gouv (via PALO IT)],
    location: [Remote / Paris],
  )[
    Création de l'infrastructure MonEspaceNis2, plateforme de conformité cybersécurité (directive NIS2).
    - Architecture et développement backend API + frontend
    - Mise en place CI/CD et bonnes pratiques (TDD, Clean Architecture)
    - #strong[Stack :] NestJS, React, TypeScript, PostgreSQL
  ]

  #entry(
    title: [Développeur Senior - Filtrage transactions bancaires],
    date: [09/2021 - 01/2023],
    institution: [Fircosoft / Accuity (via PALO IT)],
    location: [Remote / Paris],
  )[
    Filtrage de transactions bancaires dans un contexte SAFe à 80+ personnes.
    - Développement composants de filtrage (AML, KYC, SWIFT), CI/CD langages propriétaires
    - #strong[Stack :] Python, C, Oracle. #strong[Méthodes :] SAFe, CI/CD
  ]

  #entry(
    title: [Coach Technique CTO],
    date: [03/2021 - 12/2021],
    institution: [Nalo (via PALO IT)],
    location: [Remote / Paris],
  )[
    - Coaching du CTO, mise en place pratiques Software Craftsmanship. #strong[Stack :] Python, Django, TDD, DDD.
  ]
]
