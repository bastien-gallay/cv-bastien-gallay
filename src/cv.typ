#import "@preview/neat-cv:0.4.0": (
  contact-info, cv, email-link, entry, item-pills, item-with-level,
  publications, side, social-links,
) 

#show: cv.with(
  author: (
    firstname: "Bastien",
    lastname: "Gallay",
    email: "bastien@gallay.org",
    address: [17 rue du Petit Goave, 33000 Bordeaux, France],
    phone: "(+33) 06 72 66 47 38",
    // matrix: "",
    position: ("Crafting Technology Officer", "25 ans d'expérience en développement logiciel"),
    // website: "https://docbrownlabs.com",
    // twitter: "docbrown1955",
    // mastodon: "@docbrown@sciences.social",
    // github: "",
    // gitlab: "",
    linkedin: "bastiengallay",
    // researchgate: "emmett-brown",
    // scholar: "",
    // orcid: "0000-0000-0000-1955",
  ),
  profile-picture: image("assets/identite.png"),
  accent-color: rgb("#4682b4"),
  // font-color: rgb("#333333"),
  header-color: rgb("#3b4f60"),
  // date: datetime.today().display("[month repr:long] [year]"),
  // heading-font: "Fira Sans",
  // body-font: ("Noto Sans", "Roboto"),
  body-font-size: 10pt,
  paper-size: "a4",
  side-width: 4.5cm,
  // gdpr: false,
  // footer: auto,
)

#side[
  = A propos
  Passionné de logiciel depuis l'enfance, j'accompagne les équipes techniques dans l'innovation et la transformation digitale depuis plus de 25 ans.

  = Centres d'intérêt
  - Intelligence artificielle
  - Management et leadership
  - Entrepreneuriat

  = Rayonnement
  - Mentor Google Launchpad
  - Coach Startup Weekend
  - Orateur Agile Tour & Scrum Day

  = Contact
  #contact-info()

  = Informations
  Nationalité : Français

  Date de naissance : 3/03/1979

  // #v(1fr)

  #social-links()

  // Use colbreak() to insert a page break
  // #colbreak()

  = Langues
  #item-with-level("Français", 5, subtitle: "Langue maternelle")
  #item-with-level("Anglais", 4, subtitle: "Courant")
  // #item-with-level("Espagnol", 2, subtitle: "Notions")

  = Expertises
  #item-pills((
    "Lean",
    "Scrum",
    "Kanban",
    "eXtreme Programming",
    "IA",
    "Test Driven Development",
    "Spec Driven Development",
    "Clean Code",
    "Domain Driven Design",
    "TypeScript",
    "SQL",
    "Python",
    "C#",
    "C",
    "Rust",
    "Management",
    "Développement",
    "Architecture",
  ))

  // = Technology
  // #item-with-level("Flux Capacitor Design", 5)
  // #item-with-level("Time Machine Construction", 5)
  // #item-with-level("Robotics", 3)
  // #item-with-level("Computer Programming", 3)

  // = Other Skills
  // #item-pills((
  //   "Creative Problem Solving",
  //   "Improvisation",
  // ))
]

= Expérience Professionnelle

#entry(
  title: "Consultant Technique Senior → Chief Technology Officer",
  date: "02/2021 - 10/2025",
  institution: "PALO IT",
  location: "Bordeaux/Paris, France",
)[
  - *En tant que CTO (10/2024 - 10/2025) :* Stratégie technologique et participation au COMEX. Contribution à 15% de croissance du CA.
  - Management de 50 professionnels techniques. Délivrance de 20-40 certifications GitHub Copilot.
  - Conception de Gen-e2, framework de développement accéléré par IA. Initiative Quantum Computing.
  - Presales : 6+ opportunités majeures (€15k-€500k+). Partenariats Scaleway, GitHub, Mistral.
  - *En tant que Consultant Senior :* Missions clients (Bodic, Systel, TopTex, Beta.gouv, Nalo).
  - Animation de la communauté technique interne, Career Path des consultants France, recrutement.
  - *Stack :* Azure, AWS, OpenAI, Anthropic, LangChain, Python, C\#, TypeScript, Rust.
]

#entry(
  title: "Gérant & Coach Agile",
  date: "09/2013 - 02/2021",
  institution: "Upwiser",
  location: "Bordeaux, France",
)[
  - Animation de formations et d'ateliers sur l'agilité et le développement logiciel.
  - Ingénierie pédagogique pour des programmes de formation sur mesure.
  - Réponse et obtention d'appels d'offre de formation des OPCO en action collectives.
  - Recrutement d'un coach agile pour renforcer l'accompagnement des équipes.
  - Conseil en organisation et gestion de projets pour améliorer la productivité et la qualité.
  - Coaching individuel et d'équipe pour favoriser la collaboration et la communication.
  - Création du cercle Lean Startup Bordeaux pour promouvoir l'innovation locale.
  - Prises de parole lors d'événements et conférences sur l'agilité et les startups.
  - Accompagnement de près de 100 startups et PME dans leur transformation agile et leur gestion de l'innovation.
]

#entry(
  title: "Chef de projet technique et Scrum Master",
  date: "10/2010 - 10/2013",
  institution: "CDiscount",
  location: "Bordeaux, France",
)[
  - Gestion de projets techniques et Scrum Master pour des projets clients variés.
  - Environnement de développement .Net, C\#, SQL Server.
  - Responsable technique de la plateforme de paiement.
]

#entry(
  title: "Consultant Technique",
  date: "08/2006 - 09/2010",
  institution: "Cast Consulting",
  location: "Paris, France",
)[
  - Intervention sur des projets clients variés, principalement dans le domaine Web.
  - Domaines métiers : e-commerce, jeux d'argent, nucléaire, etc.
  - Environnement de développement : Java, PHP, SQL Server, Oracle, etc.
]


#entry(
  title: "Développeur Web",
  date: "06/2004 - 07/2006",
  institution: "Boonty (devenu Nexway)",
  location: "Paris, France",
)[]

#entry(
  title: "Webmaster ",
  date: "06/2002 - 06/2004",
  institution: "Indépendant",
  location: "Paris, France",
)[]

= Etudes

#entry(
  title: "DEA Réalité Virtuelle et Maîtrise des Systèmes Complexes",
  date: "2002",
  institution: "Institut National de Sciences et Techniques Nucléaires (INSTN)",
  location: "Sacclay, France",
  [Sujet de recherche: _"Comparaison des algorithmes de classification pour la segmentation multitexturées"_.],
)

#colbreak()

= Etudes - Détails

#entry(
  title: "DEA Réalité Virtuelle et Maîtrise des Systèmes Complexes - Mention Bien",
  date: "2002",
  institution: "Institut National de Sciences et Techniques Nucléaires (INSTN)",
  location: "Sacclay (91), France",
  [Sujet de recherche: _"Comparaison des algorithmes de classification pour la segmentation multitexturées"_.],
)

#entry(
  title: "Licence et Maîtrise d'Informatique - Mention Bien",
  date: "2001",
  institution: "Université de Picardie Jules Verne",
  location: "Amiens (80), France",
  [Mémoire: _"Complexité des algorithmes quantiques"_.],
)

#entry(
  title: "Diplôme Universitaire de Technologie (DUT) Informatique",
  date: "1999",
  institution: "Institut Universitaire de Technologie (IUT) d'Amiens",
  location: "Amiens (80), France",
  [Mémoire: _"Recherche de chemins pour une horde de robots"_.],
)

#entry(
  title: "Baccalauréat Scientifique - Mention Bien",
  date: "1996",
  institution: "Lycée Jean Moulin",
  location: "Les Andelys (27), France", 
  [Spécialité: _"Sciences de l'Ingénieur"_, Option: _"Informatique"_],
)

= Certifications

#entry(
  title: "Certification Scrum Master",
  date: "2008",
  institution: "Scrum Alliance",
)[]

#entry(
  title: "Professional Scrum Master",
  date: "2015",
  institution: "Scrum.org",
)[]

#entry(
  title: "Scaled Professional Scrum (SPS)",
  date: "2016",
  institution: "Scrum.org",
)[]

#entry(
  title: "Professional Scrum with Kanban",
  date: "2017",
  institution: "Scrum.org",
)[]

#entry(
  title: "Scaled Professional Scrum (Nexus)",
  date: "2017",
  institution: "Scrum.org",
)[]

#entry(
  title: "Professional Scrum Developer (PSD-I)",
  date: "2018",
  institution: "Scrum.org",
)[]

#entry(
  title: "SAFe Program Consultant (SPC4 et SPC5)",
  date: "2018, 2020",
  institution: "Scaled Agile, Inc.",
)[]

= Bénévolat

#entry(
  title: "Organisateur Agile Tour Bordeaux",
  date: "2011 - Aujourd'hui",
  institution: "Agile Tour",
  location: "Bordeaux, France",
)[
  - Organisation de la conférence annuelle (150+ participants)
  - Coordination des speakers et du programme
]

#entry(
  title: "Fondateur Lean Startup Bordeaux",
  date: "2012 - 2018",
  institution: "Lean Startup Circle",
  location: "Bordeaux, France",
)[
  - Animation de meetups réguliers sur le Lean Startup
  - Coaching de startups et entrepreneurs locaux
]

#entry(
  title: "Co-fondateur Collectif Quinconces",
  date: "2016 - 2018",
  institution: "Collectif Quinconces",
  location: "Bordeaux, France",
)[
  - Organisation et collaboration de TPE et Indépendants du numérique
  - Prospection de clients et de partenaires
  - Animation de réunions et de brainstorming
  - Gestion de projet et de la documentation
  - Synchronisation des missions
]

= Expérience détaillée


#entry(
  title: [Consultant Technique Senior → Chief Technology Officer],
  date: [02/2021 - 10/2025],
  institution: [PALO IT],
  location: [Bordeaux/Paris, France],
)[
  === Contexte
  Évolution de Consultant Senior à CTO au sein d'un cabinet de conseil international spécialisé dans la transformation digitale et le développement durable.
 === En tant que CTO (oct. 2024 - oct. 2025)

  ==== Leadership & Management
  - Direction de la stratégie technologique et participation au COMEX
  - Management de 50 professionnels techniques via organisation Hive Tech
  - Contribution à 15% de croissance du CA
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

  ==== Mission Bodic - Technical Lead (2024-2025)
  #strong[Client:] Bodic
  #strong[Durée:] 1.5 jours/semaine

  - Optimisation API : temps de réponse réduit à 72ms
  - Développement Outlook add-in avec intégration réussie
  - Code reviews et décisions d'architecture
  - Évolution vers rôle d'External CTO
  - #strong[Stack:] Azure, TypeScript, REST API, PostgreSQL, GitHub Copilot, GitHub Actions

  ==== Mission Systel - Team Coach (mars-juin 2025)
  #strong[Client:] Systel
  #strong[Durée:] 30 jours

  - Coaching quotidien d'une équipe de 3 développeurs
  - Revue architecture MAC avec pattern BFF
  - Préparation audit technique pour acquisition
  - Facilitation rétrospectives et planification sprints
  - #strong[Stack:] TFS, Java, Angular, Spring Boot, Azure DevOp

  ==== Mission TopTex - Architecture API (2025)
  #strong[Client:] TopTex
  #strong[Durée:] 2-4 jours

  - Étude architecture API et planification migration
  - Architecture multi-instance Sage
  - Feedback client : "très bien, carré, propre"

  ==== Mission Beta.gouv - Lead Developer (juil. 2023 - janv. 2024)
  #strong[Client:] Beta.gouv - MonEspaceNis2, France (Remote)
  #strong[Durée:] 7 mois

  - Création de l'infrastructure technique et de l'architecture applicative
  - Développement de la plateforme en React / JavaScript / TypeScript
  - Mise en place d'outils de mesure et de monitoring
  - #strong[Stack:] React, TypeScript, JavaScript, NestJS, PostgreSQL, Docker, GitHub Actions, Playwright, Sentry, Storybook

  ==== Mission Nalo - Coach Technique (fév. 2021 - fin 2021)
  #strong[Client:] Nalo (Fintech), Paris
  #strong[Durée:] ~10 mois (temps partiel)

  - Coaching du CTO et accompagnement de l'équipe technique
  - Mise en place de pratiques Software Craftsmanship
  - Refonte de l'architecture technique
  - #strong[Stack:] Python, Django, TDD, DDD, CI/CD
]

#entry(
  title: [Gérant & Coach Agile],
  date: [09/2013 - 02/2021],
  institution: [Upwiser],
  location: [Bordeaux, France],
)[
  === Contexte
  Création de ma société de conseil en agilité et développement logiciel, accompagnant startups et PME dans leur transformation numérique et organisationnelle.

  === Missions principales

  ==== Mission DEKRA - Coach Agile (oct. 2013 - janv. 2015)
  #strong[Client:] DEKRA, Bordeaux
  #strong[Durée:] 1 an 4 mois

  - Scrum Master pour projet de refonte logiciel interne
  - Mise en place de feature teams et coordination multi-équipes
  - Coaching et formation des nouveaux Scrum Masters
  - Accompagnement à l'adoption de bonnes pratiques Agile

  ==== Mission i-BP - Coach Agile (avr. 2015 - sept. 2015)
  #strong[Client:] i-BP, Nantes

  - Accompagnement de projets Agiles (Décisionnel, Livraison DevOps)
  - Coaching de la communauté de pratique des équipiers Agiles
  - Participation à des travaux transverses d'organisation
  - Mise en place de Coach Dating
  - #strong[Méthodes:] Scrum, Kanban, Lean Startup

  ==== Mission Dronisos - Scrum Master
  #strong[Client:] Dronisos (Startup événementiel), Bordeaux

  - Structuration de l'équipe R&D
  - Réorganisation des démonstrations pour l'innovation technique
  - #strong[Méthodes:] Scrum, Lean Startup

  ==== Mission Mieux Placer - Coach Agile
  #strong[Client:] Mieux Placer (Fintech), Paris

  - Accompagnement du Product Owner
  - Formation des équipes de production
  - #strong[Méthodes:] Scrum, Formation

  ==== Mission Wanteeed.com - PO & Coach Agile (2020)
  #strong[Client:] Wanteeed.com (Startup Web), Bordeaux
  #strong[Durée:] 6 mois

  - Product Owner remplaçant
  - Coach Agile pour startup de 20 personnes
  - Élaboration d'un modèle organisationnel agile
  - #strong[Méthodes:] Scrum, Coaching Agile

  ==== Mission Groupe SeLoger/Logic Immo - Développeur & Architecte (2020-2021)
  #strong[Client:] Groupe SeLoger/Logic Immo, Paris
  #strong[Durée:] 4 mois

  - Audit de la solution en place et proposition d'une architecture cible
  - Développement du nouveau système
  - #strong[Stack:] Architecture logicielle, Développement

  === Autres activités
  - Animation de formations et ateliers en agilité
  - Accompagnement d'une centaine de startups et PME
  - Création et animation du cercle Lean Startup Bordeaux
  - Conseil en stratégie produit et organisation
]

#entry(
  title: [Consultant Technique],
  date: [08/2006 - 09/2010],
  institution: [Cast Consulting],
  location: [Paris, France],
)[
  === Contexte
  Consultant technique au sein d'une ESN spécialisée dans le développement Web, intervenant sur des projets clients variés dans différents secteurs.

  === Missions clients

  ==== Mission JOA Online - Product Owner (07/2009 - 10/2010)
  #strong[Client:] JOA Online (Jeux en ligne), Paris
  #strong[Durée:] 16 mois

  - Product Owner d'une équipe de 10 personnes (France/Portugal)
  - Mise en place de Scrum distribué
  - Coordination de 10 sociétés sous-traitantes implantées en Europe
  - Suivi de l'appel d'offre jusqu'à la mise en production
  - #strong[Méthodes:] Scrum distribué, Product Management

  ==== Mission Pixmania/TheLink.com - Chef de projet (09/2007 - 12/2008)
  #strong[Client:] Fotovista/Pixmania (E-commerce téléphonie), Paris
  #strong[Durée:] 16 mois

  - Management d'une équipe de 7 développeurs
  - Coordination internationale avec Londres
  - Architecture, spécification et conception techniques
  - Développement et maintenance de 6 applications
  - #strong[Stack:] PHP, MySQL, Web, coordination internationale

  ==== Mission La Poste/DECLIC - Architecte (01/2008 - 08/2008)
  #strong[Client:] La Poste, Paris
  #strong[Durée:] 8 mois

  - Architecture SOA .Net
  - #strong[Stack:] .Net, SOA

  ==== Mission CEA GCAO - MOA (12/2008 - 08/2009)
  #strong[Client:] CEA (nucléaire), Saclay
  #strong[Durée:] 8 mois

  - Maîtrise d'ouvrage et maquettage
  - Documents confidentiels

  ==== Mission Nespresso - Développeur (09/2008 - 12/2008)
  #strong[Client:] Nespresso, Paris
  #strong[Durée:] 3 mois

  - Développement sites professionnels
]
