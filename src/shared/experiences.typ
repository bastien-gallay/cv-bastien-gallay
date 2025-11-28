// Expériences professionnelles réutilisables
// Utilisé par cv.typ et cv-short.typ pour la page 1
// Permet de créer des CV ciblés en sélectionnant les expériences pertinentes

#import "../neat-cv-local.typ": entry

// =============================================================================
// PALO IT - CTO (2021-2025)
// =============================================================================
#let exp-palo-it = entry(
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

// =============================================================================
// UPWISER - Coach Agile (2013-2021)
// =============================================================================
#let exp-upwiser = entry(
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

// =============================================================================
// CDISCOUNT - Chef de projet (2010-2013)
// =============================================================================
#let exp-cdiscount = entry(
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

// =============================================================================
// CAST CONSULTING - Consultant (2006-2010)
// =============================================================================
#let exp-cast = entry(
  title: "Consultant Technique",
  date: "08/2006 - 09/2010",
  institution: "Cast Consulting",
  location: "Paris, France",
)[
  - Product Owner JOA Online (équipe 10p, Scrum distribué, coordination 10 sous-traitants).
  - Chef de projet Pixmania/TheLink (équipe 7 dev, coordination internationale).
  - Clients : La Poste, CEA, Nespresso. Domaines : e-commerce, jeux en ligne, nucléaire.
]

// =============================================================================
// BOONTY/NEXWAY - Développeur (2002-2006)
// =============================================================================
#let exp-dev-web = entry(
  title: "Développeur Web",
  date: "06/2002 - 07/2006",
  institution: "Boonty (devenu Nexway) / Indépendant",
  location: "Paris, France",
)[
  - Développement e-commerce et sites web professionnels.
]

// =============================================================================
// SECTION COMPLÈTE - Page 1
// =============================================================================
// Fonction pour générer la section expérience complète de la page 1
#let experiences-page-1 = [
  = Expérience Professionnelle

  #exp-palo-it
  #exp-upwiser
  #exp-cdiscount
  #exp-cast
  #exp-dev-web
]
