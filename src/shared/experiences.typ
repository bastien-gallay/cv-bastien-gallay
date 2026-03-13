// Expériences professionnelles réutilisables
// Utilisé par cv.typ et cv-short.typ pour la page 1
// Permet de créer des CV ciblés en sélectionnant les expériences pertinentes

#import "../neat-cv-local.typ": entry

// =============================================================================
// TERAGONE FACTORY - Consultant Architecture & Audit (2025-aujourd'hui)
// =============================================================================
#let exp-teragone = entry(
  title: "Consultant Architecture & Audit",
  date: "10/2025 - Aujourd'hui",
  institution: "Teragone Factory / Indépendant",
  location: "Remote / Bordeaux",
)[
  - *CISAC - Audit ISWC (2 mois) :* Audit technique plateforme ISWC (droits d'auteur). Analyse architecture cloud Azure (Databricks, Cosmos DB).
  - *Berger-Levrault - Audit plateforme (3 mois) :* Audit obsolescence, architecture et organisation sur 2 produits RH et Gestion Financière. #strong[Stack :] Java 8/25, Spring Boot, Oracle.
]

// =============================================================================
// PALO IT - CTO (2021-2025)
// =============================================================================
#let exp-palo-it = entry(
  title: "Consultant Technique Senior → Chief Technology Officer",
  date: "02/2021 - 08/2025",
  institution: "PALO IT",
  location: "Bordeaux/Paris, France",
)[
  - *CTO :* Direction stratégie technologique, COMEX, management 50 professionnels. Presales 6+ opportunités (€15k-€500k+).
  - *Innovation IA :* Conception Gen-e2 (framework IA). Partenariats Scaleway, GitHub, Microsoft.
  - *Missions :* Bodic (External CTO), Beta.gouv (Lead Dev), Fircosoft (Dev Senior, 2 ans), Nalo (Coach CTO).
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
  - Transformations Agiles grands comptes (Dekra, i-BP) et coaching CTOs scale-ups (Dronisos, Wanteeed, SeLoger).
  - Accompagnement *~100 startups et PME*. Formations Agile, Lean, Design Thinking.
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
  - Responsable technique plateforme paiement (*1 milliard € CA*, certification PCI DSS). Équipe 15 personnes.
  - #strong[Stack :] C\#, .Net, SQL Server.
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
  - Projets internationaux (JOA Online, Pixmania). Coordination équipes distribuées Europe.
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

  #exp-teragone
  #exp-palo-it
  #exp-upwiser
  #exp-cdiscount
  #exp-cast
  #exp-dev-web
]
