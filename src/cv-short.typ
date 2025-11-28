// CV Court (1-2 pages) - Version condensée pour candidatures rapides
// Basé sur cv.typ (version exhaustive)

#import "neat-cv-local.typ": (
  cv-setup, cv-page-one, cv-continued,
  email-link, entry,
)

// Configuration partagée
#import "shared/config.typ": *
#import "shared/sidebar.typ": sidebar-content
#import "shared/experiences.typ": experiences-page-1

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

  // MAIN CONTENT
  [
    #experiences-page-1

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
