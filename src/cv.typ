// CV with sidebar on first page only
// Uses local fork of neat-cv with cv-setup, cv-page-one, cv-continued

#import "neat-cv-local.typ": (
  cv-continued, cv-page-one, cv-setup, email-link, entry, publications,
)

// Configuration partagée
#import "shared/config.typ": *
#import "shared/sidebar.typ": sidebar-content
#import "shared/experiences.typ": experiences-page-1
#import "shared/sections.typ": sections-page-1-full

#show: cv-setup.with(
  author: author-config,
  accent-color: accent-color,
  header-color: header-color,
  body-font: body-font,
  body-font-size: body-font-size,
  paper-size: paper-size,
  side-width: side-width,
)

// ============================================================================
// PAGE 1: Header + Sidebar + Main Content
// ============================================================================

#cv-page-one(
  profile-picture: image("assets/photo-profile-pro.jpg"),

  // SIDEBAR CONTENT (partagé via shared/sidebar.typ)
  sidebar-content(),

  // MAIN CONTENT (Page 1) - utilise les modules partagés
  [
    #experiences-page-1
    #sections-page-1-full
  ],
)

// ============================================================================
// PAGES 2+: Full Width Content (no sidebar)
// ============================================================================

#pagebreak()

#cv-continued[

  = Expérience détaillée


  #entry(
    title: [Consultant Technique Senior → Chief Technology Officer],
    date: [02/2021 - 08/2025],
    institution: [PALO IT],
    location: [Bordeaux/Paris, France],
  )[
    === Contexte
    Évolution de Consultant Senior à CTO au sein d'un cabinet de conseil international spécialisé dans la transformation digitale et le développement durable.
    === En tant que CTO (oct. 2024 - août 2025)

    ==== Leadership & Management
    - Direction de la stratégie technologique et participation au COMEX
    - Management de 50 professionnels techniques via organisation Hive Tech
    - Pilotage de 6+ opportunités presales majeures (€15k-€500k+)
    - 20-40 certifications GitHub Copilot délivrées

    ==== Innovation & Gen-e2
    - Conception de Gen-e2, framework de développement accéléré par IA
    - Learn & Lunch hebdomadaires et ateliers Hands-on
    - Initiative Quantum Computing : stage de 10 semaines
    - Organisation Tech\&Toast : 70+ professionnels

    ==== Presales & Business Development
    - Gestion de 6+ opportunités majeures (€15k-€500k+)
    - Clients presales : Natixis, CEVA Logistics, Aviva, Groupe BZ

    ==== Partenariats Stratégiques
    - Scaleway : partenariat cloud infrastructure
    - GitHub : programme de certification Copilot
    - Mistral : intégration Codestral dans Gen-e2

    ==== Stack Technique
    - #strong[Cloud:] Azure (Databricks, SQL Hyperscale, Cosmos DB), AWS (Bedrock), Scaleway
    - #strong[AI/ML:] OpenAI, Anthropic, Mistral, GitHub Copilot
    - #strong[Langages:] Python, Java, TypeScript, Rust
    - #strong[Architecture:] DDD, BFF, REST API, microservices, multi-cloud

    === Missions clients

    - *Bodic - External CTO (2024-2025, 1.5j/sem) :* API optimisée à 72ms, Outlook add-in. #strong[Stack:] Azure, TypeScript, PostgreSQL.
    - *Systel - Team Coach (2025, 30j) :* Coaching équipe 3 dev, audit technique acquisition. #strong[Stack:] Java, Angular, Spring Boot.
    - *TopTex - Architecture API (2025, 4j) :* Étude migration API multi-instance Sage.
    - *Beta.gouv - Lead Dev (2023-2024, 7 mois) :* Création infrastructure MonEspaceNis2. #strong[Stack:] React, TypeScript, NestJS, PostgreSQL.
    - *Fircosoft - Dev Senior (2021-2023, 2 ans 4 mois) :* Filtrage transactions bancaires, CI/CD langages propriétaires, SAFe 80+ personnes. #strong[Domaine:] AML, KYC, SWIFT. #strong[Stack:] Python, C, Oracle.
    - *Nalo - Coach Technique (2021, 10 mois) :* Coaching CTO, Software Craftsmanship. #strong[Stack:] Python, Django, TDD, DDD.
  ]

  #entry(
    title: [Gérant & Coach Agile],
    date: [09/2013 - 02/2021],
    institution: [Upwiser],
    location: [Bordeaux, France],
  )[
    === Missions principales

    - *DEKRA - Coach Agile (2013-2015, 16 mois) :* Scrum Master refonte logiciel, feature teams, coaching Scrum Masters. #strong[Méthodes:] Scrum, Coaching.
    - *i-BP - Coach Agile (2015, 6 mois) :* Projets Agiles (Décisionnel, DevOps), Communautés de Pratiques nationales. #strong[Méthodes:] Scrum, Kanban.
    - *Dronisos - Scrum Master :* Structuration R&D startup événementiel drones. #strong[Méthodes:] Scrum, Lean Startup.
    - *Mieux Placer - Coach Agile :* Coaching Product Owner, formation équipes Fintech. #strong[Méthodes:] Scrum.
    - *Wanteeed - PO & Coach Agile (2020, 6 mois) :* Product Owner, modèle organisationnel startup 20 personnes. #strong[Méthodes:] Scrum.
    - *SeLoger/Logic Immo - Architecte (2020-2021, 4 mois) :* Audit et refonte architecture. #strong[Stack:] Architecture logicielle.
  ]

  #entry(
    title: [Chef de projet technique et Scrum Master],
    date: [10/2010 - 10/2013],
    institution: [CDiscount],
    location: [Bordeaux, France],
  )[
    - Responsable technique plateforme paiement (*1 milliard € CA annuel*)
    - Équipe 5 personnes local + 10 centre de service
    - Certification *PCI DSS*, méthodes *Scrum/Scrumban*, anonymisation données (précurseur RGPD)
    - #strong[Stack:] C\#, .Net, SQL Server
  ]

  #entry(
    title: [Consultant Technique],
    date: [08/2006 - 09/2010],
    institution: [Cast Consulting],
    location: [Paris, France],
  )[
    - *JOA Online - Product Owner (2009-2010, 16 mois) :* Équipe 10p (France/Portugal), Scrum distribué, coordination 10 sous-traitants Europe.
    - *Pixmania - Chef de projet (2007-2008, 16 mois) :* Équipe 7 dev, coordination internationale Londres, 6 applications. #strong[Stack:] PHP, MySQL.
  ]
]
