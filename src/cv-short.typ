// CV Court (1-2 pages) - Version condensée pour candidatures rapides
// Basé sur cv.typ (version exhaustive)

#import "neat-cv-local.typ": (
  cv-setup, cv-page-one, cv-continued,
  contact-info, email-link, entry, item-pills, item-with-level,
  publications, social-links,
)

#show: cv-setup.with(
  author: (
    firstname: "Bastien",
    lastname: "Gallay",
    email: "bastien@gallay.org",
    address: [Bordeaux, France],
    phone: "(+33) 06 72 66 47 38",
    position: "Chief Technology Officer (CTO) | IA & Transformation Agile",
    linkedin: "bastiengallay",
  ),
  accent-color: rgb("#4682b4"),
  header-color: rgb("#3b4f60"),
  body-font-size: 11pt,
  paper-size: "a4",
  side-width: 4.5cm,
)

// ============================================================================
// PAGE 1: Header + Sidebar + Main Content
// ============================================================================

#cv-page-one(
  profile-picture: image("assets/photo-profile-pro.jpg"),

  // SIDEBAR CONTENT
  [
    = A propos
    CTO avec 25 ans d'expérience. Expert IA Générative et transformation Agile. Management de 50 professionnels techniques.

    = Contact
    #contact-info()

    #social-links()

    = Langues
    #item-with-level("Français", 5, subtitle: "Langue maternelle")
    #item-with-level("Anglais", 4, subtitle: "Courant")

    = Rayonnement
    - Mentor Google Launchpad
    - Coach Startup Weekend
    - Orateur Agile Tour & Scrum Day

    = Expertises
    #item-pills((
      "Agile",
      "IA / LLM",
      "Leadership",
      "TypeScript",
      "Python",
      "Node.js",
      "C#",
      "Rust",
      "TDD",
      "DDD",
    ))
  ],

  // MAIN CONTENT
  [
    = Expérience Professionnelle

    #entry(
      title: "Consultant Technique Senior → Chief Technology Officer",
      date: "02/2021 - 10/2025",
      institution: "PALO IT",
      location: "Bordeaux/Paris, France",
    )[
      - *Innovation IA :* Conception de Gen-e2, framework de développement accéléré par IA. 20-40 certifications GitHub Copilot. Partenariats Scaleway, GitHub, Mistral.
      - *Leadership :* Direction stratégie technologique et COMEX. Management de 50 professionnels techniques.
      - *Business :* Presales 6+ opportunités majeures (€15k-€500k+). Initiative Quantum Computing.
      - *Missions :* Bodic (External CTO, API 72ms), Beta.gouv (Lead Dev, 7 mois), Fircosoft (Dev Senior, 2 ans).
      - *Stack :* Azure, AWS, OpenAI, Anthropic, LangChain, Python, TypeScript, Rust.
    ]

    #entry(
      title: "Gérant & Coach Agile",
      date: "09/2013 - 02/2021",
      institution: "Upwiser",
      location: "Bordeaux, France",
    )[
      - Animation de formations Agile, Lean, Design Thinking (~15 sessions/an depuis 2015).
      - Accompagnement de ~100 startups et PME en transformation agile.
      - Réponse et obtention d'appels d'offre de formation des OPCO.
      - Conseil en organisation, coaching d'équipes et individuel.
      - Création du cercle Lean Startup Bordeaux.
    ]

    #entry(
      title: "Chef de projet technique et Scrum Master",
      date: "10/2010 - 10/2013",
      institution: "CDiscount",
      location: "Bordeaux, France",
    )[
      - Responsable technique de la plateforme de paiement (certification PCI DSS).
      - Gestion de 200 jours/projet par mois en Scrum/Scrumban.
      - Industrialisation de l'anonymisation des données clients (précurseur RGPD).
      - Environnement .Net, C\#, SQL Server.
    ]

    #entry(
      title: "Consultant Technique",
      date: "08/2006 - 09/2010",
      institution: "Cast Consulting",
      location: "Paris, France",
    )[
      - Product Owner, Chef de projet, Architecte sur projets clients variés.
      - Clients : JOA Online, Pixmania, La Poste, CEA, Nespresso.
      - Domaines : e-commerce, jeux en ligne, nucléaire.
    ]

    #entry(
      title: "Développeur Web",
      date: "06/2002 - 07/2006",
      institution: "Boonty (devenu Nexway) / Indépendant",
      location: "Paris, France",
    )[
      - Développement e-commerce et sites web professionnels.
    ]

    = Formation

    #entry(
      title: "DEA Réalité Virtuelle et Maîtrise des Systèmes Complexes - Mention Bien",
      date: "2002",
      institution: "INSTN (CEA Saclay)",
      location: "Saclay, France",
    )[
      Recherche : _"Comparaison des algorithmes de classification pour la segmentation multitexturées"_.
    ]

    #entry(
      title: "Maîtrise d'Informatique - Mention Bien",
      date: "2001",
      institution: "Université de Picardie Jules Verne",
      location: "Amiens, France",
    )[
      Mémoire : _"Complexité des algorithmes quantiques"_.
    ]

    = Certifications

    #entry(
      title: "SAFe Program Consultant (SPC5)",
      date: "2020",
      institution: "Scaled Agile, Inc.",
    )[]

    #entry(
      title: "Professional Scrum Master (PSM) & Developer (PSD-I)",
      date: "2015-2018",
      institution: "Scrum.org",
    )[]

    = Engagement communautaire

    #entry(
      title: "Organisateur Agile Tour Bordeaux",
      date: "2011 - Aujourd'hui",
      institution: "Agile Tour",
      location: "Bordeaux",
    )[
      Organisation de la conférence annuelle (150+ participants). Coordination speakers et programme.
    ]
  ],
)
