// Contenu de la sidebar commun aux deux versions du CV
// Utilisé par cv.typ et cv-short.typ

#import "../neat-cv-local.typ": contact-info, item-pills, social-links

// Texte "A propos" - version standard
#let about-text = [
  CTO avec 25 ans d'expérience. Expert IA Générative et transformation Agile. Management de 50 professionnels techniques, pilotage de 6+ opportunités presales (€15k-€500k+). Basé Bordeaux, présence Paris régulière.
]

// Fonction pour générer le contenu de la sidebar
#let sidebar-content() = [
  = A propos
  #about-text

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
    "Recrutement",
    "Stratégie Tech",
    "Formation",
  ))

  = Tech & IA
  #item-pills((
    "Python",
    "TypeScript",
    "Node.js",
    "C#",
    "Rust",
    "SQL",
    "IA",
  ))

  = Méthodologie
  #item-pills((
    "SAFe",
    "Lean Startup",
    "Craftsmanship",
    "TDD",
    "DDD",
  ))
]
