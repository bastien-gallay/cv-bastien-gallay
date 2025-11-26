// cv-data.typ - Données structurées du CV
// Ce fichier contient uniquement les données, pas la mise en forme
// Source unique de vérité pour toutes les versions du CV
//
// Usage:
//   #import "cv-data.typ": cv-data
//   #cv-data.personal.firstname

#let cv-data = (
  // ============================================================
  // INFORMATIONS PERSONNELLES
  // ============================================================
  personal: (
    firstname: "Bastien",
    lastname: "Gallay",
    email: "bastien@gallay.org",
    phone: "(+33) 06 72 66 47 38",
    address: "Bordeaux, France",
    position: "Chief Technology Officer (CTO) | IA & Transformation Agile",
    photo: "assets/photo-profile-pro.jpg",
    nationality: "Français",
    birthdate: "3/03/1979",
  ),

  // ============================================================
  // RÉSEAUX SOCIAUX
  // ============================================================
  social: (
    linkedin: "bastiengallay",
    // github: "",
    // website: "",
  ),

  // ============================================================
  // À PROPOS
  // ============================================================
  about: "CTO avec 25 ans d'expérience. Expert IA Générative et transformation Agile. Management de 50 professionnels techniques, pilotage de 6+ opportunités presales (€15k-€500k+).",

  // ============================================================
  // CENTRES D'INTÉRÊT
  // ============================================================
  interests: (
    "Intelligence artificielle",
    "Management et leadership",
    "Entrepreneuriat",
  ),

  // ============================================================
  // RAYONNEMENT
  // ============================================================
  influence: (
    "Mentor Google Launchpad",
    "Coach Startup Weekend",
    "Orateur Agile Tour & Scrum Day",
  ),

  // ============================================================
  // LANGUES
  // ============================================================
  languages: (
    (name: "Français", level: 5, subtitle: "Langue maternelle"),
    (name: "Anglais", level: 4, subtitle: "Courant"),
  ),

  // ============================================================
  // EXPERTISES / COMPÉTENCES
  // ============================================================
  skills: (
    methodologies: (
      "Lean",
      "Scrum",
      "Kanban",
      "eXtreme Programming",
      "Design Thinking",
    ),
    practices: (
      "Test Driven Development",
      "Spec Driven Development",
      "BDD",
      "Clean Code",
      "Domain Driven Design",
    ),
    technologies: (
      "IA",
      "TypeScript",
      "Node.js",
      "React",
      "SQL",
      "Python",
      "Java",
      "C#",
      "C",
      "Rust",
    ),
    roles: (
      "Management",
      "Développement",
      "Architecture",
    ),
    // Version flat pour affichage pills
    all: (
      "Lean",
      "Scrum",
      "Kanban",
      "eXtreme Programming",
      "Design Thinking",
      "IA",
      "Test Driven Development",
      "Spec Driven Development",
      "BDD",
      "Clean Code",
      "Domain Driven Design",
      "TypeScript",
      "Node.js",
      "React",
      "SQL",
      "Python",
      "Java",
      "C#",
      "C",
      "Rust",
      "Management",
      "Développement",
      "Architecture",
    ),
  ),

  // ============================================================
  // EXPÉRIENCES PROFESSIONNELLES (résumé)
  // ============================================================
  experiences: (
    (
      id: "palo-it",
      title: "Consultant Technique Senior → Chief Technology Officer",
      company: "PALO IT",
      location: "Bordeaux/Paris, France",
      period: (start: "02/2021", end: "10/2025"),
      summary: (
        "Innovation IA : Conception de Gen-e2, framework de développement accéléré par IA. 20-40 certifications GitHub Copilot. Partenariats Scaleway, GitHub, Mistral.",
        "Leadership : Direction stratégie technologique et COMEX. Pilotage presales 6+ opportunités (€15k-€500k+). Management de 50 professionnels techniques.",
        "Business : Presales 6+ opportunités majeures (€15k-€500k+). Initiative Quantum Computing.",
        "Missions Clients : Bodic (External CTO, API optimisée à 72ms), Beta.gouv (Lead Dev, 7 mois).",
      ),
      stack: ("Azure", "AWS", "OpenAI", "Anthropic", "LangChain", "Python", "C#", "TypeScript", "Rust"),
    ),
    (
      id: "upwiser",
      title: "Gérant & Coach Agile",
      company: "Upwiser",
      location: "Bordeaux, France",
      period: (start: "09/2013", end: "02/2021"),
      summary: (
        "Animation de formations (Agile, Lean, Design Thinking) : ~15 sessions/an depuis 2015.",
        "Ingénierie pédagogique pour des programmes de formation sur mesure.",
        "Réponse et obtention d'appels d'offre de formation des OPCO en action collectives.",
        "Recrutement d'un coach agile pour renforcer l'accompagnement des équipes.",
        "Conseil en organisation et gestion de projets pour améliorer la productivité et la qualité.",
        "Coaching individuel et d'équipe pour favoriser la collaboration et la communication.",
        "Création du cercle Lean Startup Bordeaux pour promouvoir l'innovation locale.",
        "Prises de parole lors d'événements et conférences sur l'agilité et les startups.",
        "Accompagnement de près de 100 startups et PME dans leur transformation agile et leur gestion de l'innovation.",
      ),
      stack: (),
    ),
    (
      id: "cdiscount",
      title: "Chef de projet technique et Scrum Master",
      company: "CDiscount",
      location: "Bordeaux, France",
      period: (start: "10/2010", end: "10/2013"),
      summary: (
        "Gestion de projets techniques et Scrum Master pour des projets clients variés.",
        "Environnement de développement .Net, C#, SQL Server.",
        "Responsable technique de la plateforme de paiement.",
      ),
      stack: (".Net", "C#", "SQL Server"),
    ),
    (
      id: "cast",
      title: "Consultant Technique",
      company: "Cast Consulting",
      location: "Paris, France",
      period: (start: "08/2006", end: "09/2010"),
      summary: (
        "Intervention sur des projets clients variés, principalement dans le domaine Web.",
        "Domaines métiers : e-commerce, jeux d'argent, nucléaire, etc.",
        "Environnement de développement : Java, PHP, SQL Server, Oracle, etc.",
      ),
      stack: ("Java", "PHP", "SQL Server", "Oracle"),
    ),
    (
      id: "boonty",
      title: "Développeur Web",
      company: "Boonty (devenu Nexway)",
      location: "Paris, France",
      period: (start: "06/2004", end: "07/2006"),
      summary: (),
      stack: (),
    ),
    (
      id: "freelance-web",
      title: "Webmaster",
      company: "Indépendant",
      location: "Paris, France",
      period: (start: "06/2002", end: "06/2004"),
      summary: (),
      stack: (),
    ),
  ),

  // ============================================================
  // EXPÉRIENCES DÉTAILLÉES (avec missions clients)
  // ============================================================
  experiences-detailed: (
    // --- PALO IT ---
    (
      id: "palo-it",
      title: "Consultant Technique Senior → Chief Technology Officer",
      company: "PALO IT",
      location: "Bordeaux/Paris, France",
      period: (start: "02/2021", end: "10/2025"),
      description: "Évolution de Consultant Senior à CTO au sein d'un cabinet de conseil international spécialisé dans la transformation digitale et le développement durable.",
      sections: (
        (
          title: "En tant que CTO (oct. 2024 - oct. 2025)",
          subsections: (
            (
              title: "Leadership & Management",
              items: (
                "Direction de la stratégie technologique et participation au COMEX",
                "Management de 50 professionnels techniques via organisation Hive Tech",
                "Pilotage de 6+ opportunités presales majeures (€15k-€500k+)",
                "20-40 certifications GitHub Copilot délivrées",
              ),
            ),
            (
              title: "Innovation & Gen-e2",
              items: (
                "Conception de Gen-e2, framework de développement accéléré par IA",
                "Learn & Lunch hebdomadaires et ateliers Hands-on",
                "Initiative Quantum Computing : stage de 10 semaines",
                "Organisation Tech&Toast : 70+ professionnels",
              ),
            ),
            (
              title: "Presales & Business Development",
              items: (
                "Gestion de 6+ opportunités majeures (€15k-€500k+)",
                "Clients presales : Natixis, CEVA Logistics, Aviva, Groupe BZ",
              ),
            ),
            (
              title: "Partenariats Stratégiques",
              items: (
                "Scaleway : partenariat cloud infrastructure",
                "GitHub : programme de certification Copilot",
                "Mistral : intégration Codestral dans Gen-e2",
              ),
            ),
          ),
          stack: (
            cloud: ("Azure (Databricks, SQL Hyperscale, Cosmos DB)", "AWS (Bedrock)", "Scaleway"),
            ai: ("OpenAI", "Anthropic", "Mistral", "GitHub Copilot"),
            languages: ("Python", "Java", "TypeScript", "Rust"),
            architecture: ("DDD", "BFF", "REST API", "microservices", "multi-cloud"),
          ),
        ),
      ),
      missions: (
        (
          title: "Mission Bodic - Technical Lead",
          period: "2024-2025",
          client: "Bodic",
          duration: "1.5 jours/semaine",
          items: (
            "Optimisation API : temps de réponse réduit à 72ms",
            "Développement Outlook add-in avec intégration réussie",
            "Code reviews et décisions d'architecture",
            "Évolution vers rôle d'External CTO",
          ),
          stack: ("Azure", "TypeScript", "REST API", "PostgreSQL", "GitHub Copilot", "GitHub Actions"),
        ),
        (
          title: "Mission Systel - Team Coach",
          period: "mars-juin 2025",
          client: "Systel",
          duration: "30 jours",
          items: (
            "Coaching quotidien d'une équipe de 3 développeurs",
            "Revue architecture MAC avec pattern BFF",
            "Préparation audit technique pour acquisition",
            "Facilitation rétrospectives et planification sprints",
          ),
          stack: ("TFS", "Java", "Angular", "Spring Boot", "Azure DevOps"),
        ),
        (
          title: "Mission TopTex - Architecture API",
          period: "2025",
          client: "TopTex",
          duration: "2-4 jours",
          items: (
            "Étude architecture API et planification migration",
            "Architecture multi-instance Sage",
            "Feedback client : \"très bien, carré, propre\"",
          ),
          stack: (),
        ),
        (
          title: "Mission Beta.gouv - Lead Developer",
          period: "juil. 2023 - janv. 2024",
          client: "Beta.gouv - MonEspaceNis2, France (Remote)",
          duration: "7 mois",
          items: (
            "Création de l'infrastructure technique et de l'architecture applicative",
            "Développement de la plateforme en React / JavaScript / TypeScript",
            "Mise en place d'outils de mesure et de monitoring",
          ),
          stack: ("React", "TypeScript", "JavaScript", "NestJS", "PostgreSQL", "Docker", "GitHub Actions", "Playwright", "Sentry", "Storybook"),
        ),
        (
          title: "Mission Fircosoft - Développeur Senior",
          period: "mars 2021 - juin 2023",
          client: "Fircosoft (LexisNexis Risk Solutions), Bordeaux",
          duration: "2 ans 4 mois",
          items: (
            "Développement de solutions de filtrage des transactions et listes de sanctions pour institutions bancaires",
            "Création d'une infrastructure de test automatisé multi-systèmes (Linux, AIX, HP-UX, Solaris)",
            "Mise en place de CI/CD pour langages propriétaires (Claire, FKScript)",
            "TDD et génération de documentation par les tests automatisés",
            "Mob-programming et pair-programming intensifs en environnement SAFe (train 80+ personnes)",
          ),
          domain: "Conformité financière (AML, KYC, FATF, DORA), SWIFT, ISO 20022",
          stack: ("Claire", "FKScript", "Python", "C", "Oracle", "SQL Server", "DB2"),
        ),
        (
          title: "Mission Nalo - Coach Technique",
          period: "fév. 2021 - fin 2021",
          client: "Nalo (Fintech), Paris",
          duration: "~10 mois (temps partiel)",
          items: (
            "Coaching du CTO et accompagnement de l'équipe technique",
            "Mise en place de pratiques Software Craftsmanship",
            "Refonte de l'architecture technique",
          ),
          stack: ("Python", "Django", "TDD", "DDD", "CI/CD"),
        ),
      ),
    ),

    // --- Upwiser ---
    (
      id: "upwiser",
      title: "Gérant & Coach Agile",
      company: "Upwiser",
      location: "Bordeaux, France",
      period: (start: "09/2013", end: "02/2021"),
      description: "Création de ma société de conseil en agilité et développement logiciel, accompagnant startups et PME dans leur transformation numérique et organisationnelle.",
      missions: (
        (
          title: "Mission DEKRA - Coach Agile",
          period: "oct. 2013 - janv. 2015",
          client: "DEKRA, Bordeaux",
          duration: "1 an 4 mois",
          items: (
            "Scrum Master pour projet de refonte logiciel interne",
            "Mise en place de feature teams et coordination multi-équipes",
            "Coaching et formation des nouveaux Scrum Masters",
            "Accompagnement à l'adoption de bonnes pratiques Agile",
          ),
          stack: (),
        ),
        (
          title: "Mission i-BP - Coach Agile",
          period: "avr. 2015 - sept. 2015",
          client: "i-BP, Nantes",
          duration: none,
          items: (
            "Accompagnement de projets Agiles (Décisionnel, Livraison DevOps)",
            "Animation de Communautés de Pratiques nationales (équipiers Agiles)",
            "Participation à des travaux transverses d'organisation",
            "Mise en place de Coach Dating",
          ),
          methods: ("Scrum", "Kanban", "Lean Startup"),
        ),
        (
          title: "Mission Dronisos - Scrum Master",
          period: none,
          client: "Dronisos (Startup événementiel), Bordeaux",
          duration: none,
          items: (
            "Structuration de l'équipe R&D",
            "Réorganisation des démonstrations pour l'innovation technique",
          ),
          methods: ("Scrum", "Lean Startup"),
        ),
        (
          title: "Mission Mieux Placer - Coach Agile",
          period: none,
          client: "Mieux Placer (Fintech), Paris",
          duration: none,
          items: (
            "Accompagnement du Product Owner",
            "Formation des équipes de production",
          ),
          methods: ("Scrum", "Formation"),
        ),
        (
          title: "Mission Wanteeed.com - PO & Coach Agile",
          period: "2020",
          client: "Wanteeed.com (Startup Web), Bordeaux",
          duration: "6 mois",
          items: (
            "Product Owner remplaçant",
            "Coach Agile pour startup de 20 personnes",
            "Élaboration d'un modèle organisationnel agile",
          ),
          methods: ("Scrum", "Coaching Agile"),
        ),
        (
          title: "Mission Groupe SeLoger/Logic Immo - Développeur & Architecte",
          period: "2020-2021",
          client: "Groupe SeLoger/Logic Immo, Paris",
          duration: "4 mois",
          items: (
            "Audit de la solution en place et proposition d'une architecture cible",
            "Développement du nouveau système",
          ),
          stack: ("Architecture logicielle", "Développement"),
        ),
      ),
      other-activities: (
        "Animation de formations et ateliers en agilité",
        "Accompagnement d'une centaine de startups et PME",
        "Création et animation du cercle Lean Startup Bordeaux",
        "Conseil en stratégie produit et organisation",
      ),
    ),

    // --- Cast Consulting ---
    (
      id: "cast",
      title: "Consultant Technique",
      company: "Cast Consulting",
      location: "Paris, France",
      period: (start: "08/2006", end: "09/2010"),
      description: "Consultant technique au sein d'une ESN spécialisée dans le développement Web, intervenant sur des projets clients variés dans différents secteurs.",
      missions: (
        (
          title: "Mission JOA Online - Product Owner",
          period: "07/2009 - 10/2010",
          client: "JOA Online (Jeux en ligne), Paris",
          duration: "16 mois",
          items: (
            "Product Owner d'une équipe de 10 personnes (France/Portugal)",
            "Mise en place de Scrum distribué",
            "Coordination de 10 sociétés sous-traitantes implantées en Europe",
            "Suivi de l'appel d'offre jusqu'à la mise en production",
          ),
          methods: ("Scrum distribué", "Product Management"),
        ),
        (
          title: "Mission Pixmania/TheLink.com - Chef de projet",
          period: "09/2007 - 12/2008",
          client: "Fotovista/Pixmania (E-commerce téléphonie), Paris",
          duration: "16 mois",
          items: (
            "Management d'une équipe de 7 développeurs",
            "Coordination internationale avec Londres",
            "Architecture, spécification et conception techniques",
            "Développement et maintenance de 6 applications",
          ),
          stack: ("PHP", "MySQL", "Web", "coordination internationale"),
        ),
        (
          title: "Mission La Poste/DECLIC - Architecte",
          period: "01/2008 - 08/2008",
          client: "La Poste, Paris",
          duration: "8 mois",
          items: (
            "Architecture SOA .Net",
          ),
          stack: (".Net", "SOA"),
        ),
        (
          title: "Mission CEA GCAO - MOA",
          period: "12/2008 - 08/2009",
          client: "CEA (nucléaire), Saclay",
          duration: "8 mois",
          items: (
            "Maîtrise d'ouvrage et maquettage",
            "Documents confidentiels",
          ),
          stack: (),
        ),
        (
          title: "Mission Nespresso - Développeur",
          period: "09/2008 - 12/2008",
          client: "Nespresso, Paris",
          duration: "3 mois",
          items: (
            "Développement sites professionnels",
          ),
          stack: (),
        ),
      ),
    ),

    // --- CDiscount ---
    (
      id: "cdiscount",
      title: "Chef de projet technique et Scrum Master",
      company: "CDiscount",
      location: "Bordeaux, France",
      period: (start: "10/2010", end: "10/2013"),
      description: "Responsable technique au sein de l'un des leaders français du e-commerce, en charge de la plateforme de paiement et de la gestion de projets techniques.",
      sections: (
        (
          title: "Plateforme de paiement",
          items: (
            "Responsable technique de la plateforme de paiement",
            "Obtention de la certification PCI DSS (Payment Card Industry Data Security Standard)",
            "Refonte technique de l'application vers un mode SaaS",
            "Maintenance et évolution des applications en production",
          ),
        ),
        (
          title: "Gestion de projets",
          items: (
            "Mise en place des méthodes Scrum et Scrumban",
            "Gestion de 200 jours de projet par mois en moyenne",
            "Prise en charge des développements au forfait",
          ),
        ),
        (
          title: "Données et conformité",
          items: (
            "Industrialisation de l'anonymisation des données clients (précurseur RGPD)",
          ),
        ),
        (
          title: "Animation technique",
          items: (
            "Création de déjeuners Scrum pour partager les bonnes pratiques",
            "Animation de Coding Dojos internes pour la montée en compétences",
            "Coaching des développeurs et chefs de projets",
          ),
        ),
      ),
      stack: (
        languages: ("C#", ".Net", "SQL Server"),
        methods: ("Scrum", "Scrumban", "TDD"),
        domain: ("E-commerce", "paiement en ligne", "sécurité"),
      ),
    ),
  ),

  // ============================================================
  // FORMATION (résumé)
  // ============================================================
  education: (
    (
      id: "dea",
      degree: "DEA Réalité Virtuelle et Maîtrise des Systèmes Complexes",
      school: "Institut National de Sciences et Techniques Nucléaires (INSTN)",
      location: "Sacclay, France",
      year: "2002",
      details: "Sujet de recherche: \"Comparaison des algorithmes de classification pour la segmentation multitexturées\".",
    ),
  ),

  // ============================================================
  // FORMATION (détaillée)
  // ============================================================
  education-detailed: (
    (
      id: "dea",
      degree: "DEA Réalité Virtuelle et Maîtrise des Systèmes Complexes - Mention Bien",
      school: "Institut National de Sciences et Techniques Nucléaires (INSTN)",
      location: "Sacclay (91), France",
      year: "2002",
      details: "Sujet de recherche: \"Comparaison des algorithmes de classification pour la segmentation multitexturées\".",
    ),
    (
      id: "maitrise",
      degree: "Licence et Maîtrise d'Informatique - Mention Bien",
      school: "Université de Picardie Jules Verne",
      location: "Amiens (80), France",
      year: "2001",
      details: "Mémoire: \"Complexité des algorithmes quantiques\".",
    ),
    (
      id: "dut",
      degree: "Diplôme Universitaire de Technologie (DUT) Informatique",
      school: "Institut Universitaire de Technologie (IUT) d'Amiens",
      location: "Amiens (80), France",
      year: "1999",
      details: "Mémoire: \"Recherche de chemins pour une horde de robots\".",
    ),
    (
      id: "bac",
      degree: "Baccalauréat Scientifique - Mention Bien",
      school: "Lycée Jean Moulin",
      location: "Les Andelys (27), France",
      year: "1996",
      details: "Spécialité: \"Sciences de l'Ingénieur\", Option: \"Informatique\"",
    ),
  ),

  // ============================================================
  // CERTIFICATIONS
  // ============================================================
  certifications: (
    (name: "Certification Scrum Master", issuer: "Scrum Alliance", year: "2008"),
    (name: "Professional Scrum Master", issuer: "Scrum.org", year: "2015"),
    (name: "Scaled Professional Scrum (SPS)", issuer: "Scrum.org", year: "2016"),
    (name: "Professional Scrum with Kanban", issuer: "Scrum.org", year: "2017"),
    (name: "Scaled Professional Scrum (Nexus)", issuer: "Scrum.org", year: "2017"),
    (name: "Professional Scrum Developer (PSD-I)", issuer: "Scrum.org", year: "2018"),
    (name: "SAFe Program Consultant (SPC4 et SPC5)", issuer: "Scaled Agile, Inc.", year: "2018, 2020"),
  ),

  // ============================================================
  // BÉNÉVOLAT
  // ============================================================
  volunteering: (
    (
      title: "Organisateur Agile Tour Bordeaux",
      organization: "Agile Tour",
      location: "Bordeaux, France",
      period: "2011 - Aujourd'hui",
      items: (
        "Organisation de la conférence annuelle (150+ participants)",
        "Coordination des speakers et du programme",
      ),
    ),
    (
      title: "Fondateur Lean Startup Bordeaux",
      organization: "Lean Startup Circle",
      location: "Bordeaux, France",
      period: "2012 - 2018",
      items: (
        "Animation de meetups réguliers sur le Lean Startup",
        "Coaching de startups et entrepreneurs locaux",
      ),
    ),
    (
      title: "Co-fondateur Collectif Quinconces",
      organization: "Collectif Quinconces",
      location: "Bordeaux, France",
      period: "2016 - 2018",
      items: (
        "Organisation et collaboration de TPE et Indépendants du numérique",
        "Prospection de clients et de partenaires",
        "Animation de réunions et de brainstorming",
        "Gestion de projet et de la documentation",
        "Synchronisation des missions",
      ),
    ),
  ),

  // ============================================================
  // CONFIGURATION VISUELLE (optionnel, pour référence)
  // ============================================================
  style: (
    accent-color: "#4682b4",
    header-color: "#3b4f60",
    body-font-size: "10pt",
    paper-size: "a4",
    side-width: "4.5cm",
  ),
)
