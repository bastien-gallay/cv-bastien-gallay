// CV adapté pour: CTO Startup HealthTech @ Eurasanté
// Date: 2025-12-01
// Score d'adéquation: 75/100

#import "../../../src/neat-cv-local.typ": (
  cv-continued, cv-page-one, cv-setup, email-link, entry, contact-info, item-pills, social-links,
)

// Configuration partagée
#import "../../../src/shared/config.typ": accent-color, header-color, body-font, body-font-size, paper-size, side-width

// Métadonnées document
#set document(
  title: "CV - Bastien Gallay - CTO Startup HealthTech",
  author: "Bastien Gallay",
  date: datetime.today(),
)

// Configuration auteur adaptée (titre conservé)
#let author-adapted = (
  firstname: "Bastien",
  lastname: "Gallay",
  email: "bastien@gallay.org",
  address: [Bordeaux, France],
  phone: "(+33) 06 72 66 47 38",
  position: "Chief Technology Officer (CTO) | IA & Transformation Agile",
  linkedin: "bastiengallay",
)

// =============================================================================
// SIDEBAR ADAPTÉE - Réordonnée par pertinence
// =============================================================================

// "A propos" adapté - mention VR et IA
#let about-adapted = [
  CTO avec 25 ans d'expérience. Formation en Réalité Virtuelle (DEA 2002). Expert IA Générative et structuration R&D startup. Management de 50 professionnels techniques. Basé Bordeaux, mobilité nationale.
]

#let sidebar-adapted() = [
  = A propos
  #about-adapted

  = Rayonnement
  - Mentor Google Launchpad
  - Coach Startup Weekend
  - Orateur Agile Tour & Scrum Day

  = Contact
  #contact-info()

  = Informations
  Nationalité : Français

  Date de naissance : 3/03/1979

  #social-links()

  - *Français :* Langue maternelle
  - *Anglais :* Courant

  = Leadership
  #item-pills((
    "COMEX",
    "Stratégie Tech",
    "Recrutement",
    "Formation",
  ))

  = Tech & IA
  #item-pills((
    "GenAI Dev",
    "Python",
    "Azure",
    "TypeScript",
    "React",
    "Node.js",
    "C#",
    "Rust",
  ))

  = Méthodologie
  #item-pills((
    "Lean Startup",
    "SAFe",
    "Craftsmanship",
    "TDD",
    "DDD",
  ))
]

// =============================================================================
// EXPÉRIENCES ADAPTÉES - Réordonnées par pertinence (sans Cast Consulting)
// =============================================================================

// PALO IT - CTO (très pertinent: CTO, IA, management)
#let exp-palo-it-adapted = entry(
  title: "Consultant Technique Senior → Chief Technology Officer",
  date: "02/2021 - 08/2025",
  institution: "PALO IT",
  location: "Bordeaux/Paris, France",
)[
  - *Innovation IA :* Conception de Gen-e2, framework de développement accéléré par IA. 20-40 certifications GitHub Copilot. Partenariats Scaleway, GitHub, Microsoft.
  - *Leadership :* Direction stratégie technologique et COMEX. Pilotage presales 6+ opportunités (€15k-€500k+). Management de 50 professionnels techniques.
  - *Business :* Presales 6+ opportunités majeures (€15k-€500k+). Initiative Quantum Computing.
  - *Missions :* Bodic (External CTO), Beta.gouv (Lead Dev, 7 mois), Fircosoft (Dev Senior, 2 ans).
  - *Stack :* Azure, OpenAI, Anthropic, Python, C\#, TypeScript, Rust.
]

// CDISCOUNT - Pertinent pour conformité/DPO
#let exp-cdiscount-adapted = entry(
  title: "Chef de projet technique et Scrum Master",
  date: "10/2010 - 10/2013",
  institution: "CDiscount",
  location: "Bordeaux, France",
)[
  - Responsable technique plateforme paiement (*1 milliard € CA*, certification PCI DSS).
  - Gestion de *200 jours/projet par mois* en Scrum/Scrumban.
  - Industrialisation de l'anonymisation des données clients (précurseur RGPD).
  - *Stack :* .Net, C\#, SQL Server.
]

// UPWISER - Pertinent pour startups et R&D
#let exp-upwiser-adapted = entry(
  title: "Gérant & Coach Agile",
  date: "09/2013 - 02/2021",
  institution: "Upwiser",
  location: "Bordeaux, France",
)[
  - Pilotage de transformations Agiles à l'échelle (SAFe, Scrum) pour grands comptes (Dekra, i-BP).
  - Structuration R&D et coaching CTOs pour scale-ups (Dronisos, Wanteeed, Nalo, SeLoger).
  - Accompagnement de *~100 startups et PME* en transformation agile.
  - Animation de formations Agile, Lean, Design Thinking (*~15 sessions/an*).
  - Fondateur du cercle Lean Startup Bordeaux.
]

// BOONTY - Background technique (condensé)
#let exp-boonty-adapted = entry(
  title: "Développeur Web",
  date: "06/2002 - 07/2006",
  institution: "Boonty (devenu Nexway) / Indépendant",
  location: "Paris, France",
)[
  - Développement e-commerce et sites web professionnels.
]

// Section expériences page 1 - ordre adapté
#let experiences-page-1-adapted = [
  = Expérience Professionnelle

  #exp-palo-it-adapted
  #exp-cdiscount-adapted
  #exp-upwiser-adapted
  #exp-boonty-adapted
]

// =============================================================================
// SECTIONS ADDITIONNELLES
// =============================================================================

#let formation-dea-adapted = entry(
  title: "DEA Réalité Virtuelle et Maîtrise des Systèmes Complexes - Mention Bien",
  date: "2002",
  institution: "INSTN (CEA Saclay)",
  location: "Saclay, France",
)[
  Recherche : _"Comparaison des algorithmes de classification pour la segmentation multitexturées"_.
]

#let formation-maitrise = entry(
  title: "Maîtrise d'Informatique - Mention Bien",
  date: "2001",
  institution: "Université de Picardie Jules Verne",
  location: "Amiens, France",
)[
  Mémoire : _"Complexité des algorithmes quantiques"_.
]

#let cert-safe = entry(
  title: "SAFe Program Consultant (SPC5)",
  date: "2020",
  institution: "Scaled Agile, Inc.",
)[]

#let cert-scrum = entry(
  title: "Professional Scrum Master (PSM I & II) & Developer (PSD-I)",
  date: "2015-2018",
  institution: "Scrum.org",
)[]

#let engagement-agile = entry(
  title: "Organisateur Agile Tour Bordeaux",
  date: "2011 - Aujourd'hui",
  institution: "Agile Tour",
  location: "Bordeaux",
)[
  Organisation de la conférence annuelle (150+ participants). Fondateur Lean Startup Bordeaux (2012-2018). Co-fondateur Collectif Quinconces (2016-2018).
]

#let sections-page-1-adapted = [
  = Formation

  #formation-dea-adapted
  #formation-maitrise

  = Certifications

  #cert-safe
  #cert-scrum

  = Engagement communautaire

  #engagement-agile
]

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
  sidebar-adapted(),
  [
    #experiences-page-1-adapted
    #sections-page-1-adapted
  ],
)

// =============================================================================
// PAGE 2+ : Expérience détaillée (sans sidebar)
// =============================================================================

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
]
