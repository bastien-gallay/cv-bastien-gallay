// CV adapté pour: Senior Software Crafter / Chef de Projet @ CISAC
// Via: Teragone Factory
// Date: 2026-02-13
// Score d'adéquation: 94/100
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
  title: "CV - Bastien Gallay - Senior Fullstack Lead Developer @ CISAC",
  author: "Bastien Gallay",
  date: datetime.today(),
)

// =============================================================================
// CONFIGURATION ADAPTÉE
// =============================================================================

#let author-adapted = (
  ..author-config,
  position: "Senior Fullstack Lead Developer | AI & Craftsmanship",
)

// =============================================================================
// SIDEBAR ADAPTÉE (compacte pour tenir sur 1 page)
// =============================================================================

#let sidebar-adapted() = [
  = A propos
  Développeur Senior Fullstack, 23 ans d'expérience. Expert TypeScript/NestJS et Java/Spring Boot. Architecte microservices cloud Azure. AI Engineer. Software Craftsmanship (TDD, DDD). Connaissance CISAC (audit ISWC 2025).

  = Informations
  Nationalité : Français

  #social-links()

  - *Français :* Langue maternelle
  - *Anglais :* Courant

  = Leadership
  #item-pills((
    "Lead Tech",
    "Architecture",
    "Coordination",
    "Audit",
  ))

  = Tech & IA
  #item-pills((
    "TypeScript",
    "NestJS",
    "NuxtJs",
    "Java",
    "Spring Boot",
    "Azure",
    "PostgreSQL",
    "React",
    "AI/LLM",
  ))

  = Méthodologie
  #item-pills((
    "Craftsmanship",
    "TDD",
    "DDD",
    "DevOps",
    "Agile",
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
    - *CISAC - Audit ISWC (2 mois) :* Analyse architecture Azure Databricks et Cosmos DB. #strong[Domaine :] droits d'auteur, standards internationaux.
    - *Berger-Levrault - Audit plateforme (3 mois) :* Obsolescence, architecture et organisation sur 2 produits RH et Gestion Financière. #strong[Stack :] Java 8/25, Spring Boot, Oracle.
  ]

  #entry(
    title: [Consultant Technique Senior → CTO],
    date: [02/2021 - 08/2025],
    institution: [PALO IT],
    location: [Bordeaux/Paris],
  )[
    - *Bodic - Lead Dev (6 mois) :* Back office fonds d'investissements durables. #strong[Stack :] NestJS, React, TypeScript, Azure (full).
    - *Beta.gouv - Lead Dev (7 mois) :* Infrastructure MonEspaceNis2. #strong[Stack :] NestJS, TypeScript, React, PostgreSQL.
    - *Fircosoft - Dev Senior (2 ans) :* Filtrage transactions bancaires, CI/CD. SAFe 80+ personnes. #strong[Stack :] Python, C, Oracle.
    - *SeLoger - Dev Fullstack (6 mois, 2021) :* Backoffice gestion immobilière. Java et ReactAdmin. #strong[Stack :] Java, React.
    - *AI & Leadership :* Conception Gen-e2 (framework IA). CTO, management 50 personnes, COMEX. Partenariats Microsoft, Github Copilot, MongoDB.
  ]

  #entry(
    title: [Gérant, Coach Agile & Développeur],
    date: [09/2013 - 02/2021],
    institution: [Upwiser],
    location: [Bordeaux],
  )[
    - Transformations Agiles grands comptes et startups (~100 accompagnements).
    - Développement site web Upwiser (#strong[NuxtJS]).
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
    - Projets internationaux (JOA Online, Pixmania). Coordination équipes distribuées Europe.
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
    Audit technique de la plateforme ISWC (International Standard Work Code) pour la Confédération Internationale des Sociétés d'Auteurs et Compositeurs.
    - Analyse de l'architecture cloud Azure (Databricks, Cosmos DB)
    - Évaluation de la qualité du code et des pratiques de développement
    - #strong[Domaine :] Droits d'auteur, standards internationaux (ISWC)
  ]

  #entry(
    title: [Lead Developer / External CTO],
    date: [02/2025 - 08/2025],
    institution: [Bodic (via PALO IT)],
    location: [Remote / Bordeaux],
  )[
    Back office de gestion de fonds d'investissements durables. Infrastructure full Azure.
    - Développement API backend (optimisée à 72ms) et frontend React
    - Création Outlook add-in, mise en place infrastructure cloud Azure
    - #strong[Stack :] NestJS, React, TypeScript, Node.js, Azure, PostgreSQL
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
    - #strong[Stack :] Python, C, Oracle. #strong[Domaine :] conformité bancaire. #strong[Méthodes :] SAFe, CI/CD
  ]

  #entry(
    title: [Coach Technique CTO],
    date: [03/2021 - 12/2021],
    institution: [Nalo (via PALO IT)],
    location: [Remote / Paris],
  )[
    - Coaching du CTO, mise en place pratiques Software Craftsmanship. #strong[Stack :] Python, Django, TDD, DDD.
  ]

  #entry(
    title: [Développeur Java - Backoffice gestion immobilière],
    date: [2021],
    institution: [Seloger (via PALO IT)],
    location: [Bordeaux],
  )[
    - Développement backoffice de gestion immobilière. Java et ReactAdmin. #strong[Stack :] Java, React.
  ]
]
