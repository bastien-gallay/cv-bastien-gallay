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
  - *En tant que CTO (10/2024 - 10/2025) :* Responsable de la stratégie technologique et de l'innovation, avec participation au COMEX de l'entreprise.
  - Management et mentorat des équipes techniques (50 personnes) et développement des talents au sein de l'organisation.
  - Conception et mise en œuvre de Gen-e2, méthode basée sur l'IA pour la création de produits numériques.
  - Organisation des propositions commerciales et coordination des initiatives technologiques internationales.
  - *En tant que Consultant Senior :* Accompagnement des clients dans leurs stratégies technologiques et conseil en architecture logicielle.
  - Animation de la communauté technique interne, création du Career Path des consultants France et participation au recrutement.
  - Formation et coaching des équipes sur les méthodologies agiles, technologies émergentes et meilleures pratiques de développement.
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


= Expérience détaillée

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

  === Autres activités
  - Animation de formations et ateliers en agilité
  - Accompagnement d'une centaine de startups et PME
  - Création et animation du cercle Lean Startup Bordeaux
  - Conseil en stratégie produit et organisation
]

#entry(
  title: [Consultant Technique Senior → Chief Technology Officer],
  date: [02/2021 - 10/2025],
  institution: [PALO IT],
  location: [Bordeaux/Paris, France],
)[
  === Contexte
  Évolution de Consultant Senior à CTO au sein d'un cabinet de conseil international spécialisé dans la transformation digitale et le développement durable.

  === Missions clients

  ==== Mission Beta.gouv - Lead Developer (juil. 2023 - janv. 2024)
  #strong[Client:] Beta.gouv - MonEspaceNis2, France (Remote)
  #strong[Durée:] 7 mois

  - Création de l'infrastructure technique et de l'architecture applicative
  - Développement de la plateforme en React / JavaScript / TypeScript
  - Mise en place d'outils de mesure et de monitoring
  - #strong[Stack:] React, TypeScript, JavaScript

  ==== Mission Nalo - Coach Technique (fév. 2021 - fin 2021)
  #strong[Client:] Nalo (Fintech), Paris
  #strong[Durée:] ~10 mois (temps partiel)

  - Coaching du CTO et accompagnement de l'équipe technique
  - Mise en place de pratiques Software Craftsmanship
  - Refonte de l'architecture technique
  - #strong[Stack:] Python, Django
]

