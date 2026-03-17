// CV adapté pour: CTO @ TechStartup
// Date: 2025-11-30
// Score d'adéquation: 85/100

#import "../../../src/neat-cv-local.typ": (
  cv-continued, cv-page-one, cv-setup, email-link, entry, publications,
  contact-info, item-pills, social-links,
)

#import "../../../src/shared/config.typ": *
#import "../../../src/shared/experiences.typ": *
#import "../../../src/shared/sections.typ": *

// =============================================================================
// CONFIGURATION ADAPTÉE - CTO @ TechStartup
// =============================================================================

#let author-adapted = (
  ..author-config,
  // Titre adapté pour mettre en avant Cloud et IA
  position: "Chief Technology Officer (CTO) | Cloud Architecture & IA Générative",
)

// =============================================================================
// SIDEBAR ADAPTÉE
// =============================================================================

// Texte "A propos" adapté pour ce poste CTO startup
#let about-text-adapted = [
  CTO avec 25 ans d'expérience. Expert Cloud (Azure, AWS) et IA Générative (LLMs, RAG). Management de 50 professionnels techniques et participation COMEX. Créateur de Gen-e2, framework de développement accéléré par IA. Basé Bordeaux, présence Paris régulière.
]

// Skills réordonnés selon les mots-clés ATS de l'offre
#let skills-leadership-adapted = (
  "COMEX",           // Mentionné dans l'offre
  "Stratégie Tech",  // CTO = stratégie
  "Recrutement",
  "Formation",
)

#let skills-tech-adapted = (
  "GenAI Dev",       // IA Générative prioritaire
  "Azure",           // Cloud mentionné
  "Python",          // Mentionné dans l'offre
  "TypeScript",      // Mentionné dans l'offre
  "React",
  "Node.js",
  "C#",
  "Rust",
)

#let skills-methodo-adapted = (
  "SAFe",            // Mentionné dans l'offre
  "DevOps",          // CI/CD mentionné
  "Craftsmanship",
  "TDD",
  "DDD",
)

#let sidebar-adapted() = [
  = A propos
  #about-text-adapted

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
  #item-pills(skills-leadership-adapted)

  = Tech & IA
  #item-pills(skills-tech-adapted)

  = Méthodologie
  #item-pills(skills-methodo-adapted)
]

// =============================================================================
// EXPÉRIENCES ADAPTÉES
// =============================================================================

// Expérience PALO IT enrichie avec mots-clés ATS
#let exp-palo-it-adapted = entry(
  title: "Consultant Technique Senior → Chief Technology Officer",
  date: "02/2021 - 08/2025",
  institution: "PALO IT",
  location: "Bordeaux/Paris, France",
)[
  - *IA Générative & Innovation :* Conception de Gen-e2, framework de développement accéléré par IA. 20-40 certifications GitHub Copilot. Intégration LLMs (OpenAI, Anthropic, Mistral).
  - *Leadership & COMEX :* Direction de la stratégie technologique. Management de 50 professionnels techniques via organisation Hive Tech.
  - *Cloud Architecture :* Expertise Azure (Databricks, SQL Hyperscale, Cosmos DB), AWS (Bedrock). Partenariat Scaleway.
  - *Presales & Business :* Pilotage de 6+ opportunités majeures (€15k-€500k+). Clients: Natixis, CEVA Logistics, Aviva.
  - *Stack :* Azure, AWS, Python, TypeScript, C\#, Rust, CI/CD, DevOps.
]

// Expérience Upwiser condensée mais pertinente (coaching CTOs)
#let exp-upwiser-adapted = entry(
  title: "Gérant & Coach Agile",
  date: "09/2013 - 02/2021",
  institution: "Upwiser",
  location: "Bordeaux, France",
)[
  - Coaching de CTOs et structuration R&D pour scale-ups (Dronisos, Wanteeed, Nalo, SeLoger).
  - Transformations Agiles à l'échelle (SAFe, Scrum) pour grands comptes.
  - Accompagnement de ~100 startups et PME en transformation technique.
]

// CDiscount maintenu (expérience e-commerce/paiement pertinente)
#let exp-cdiscount-adapted = entry(
  title: "Chef de projet technique et Scrum Master",
  date: "10/2010 - 10/2013",
  institution: "CDiscount",
  location: "Bordeaux, France",
)[
  - Responsable technique plateforme paiement (1 milliard € CA, certification PCI DSS).
  - Gestion Scrum/Scrumban, management équipe technique.
]

// Expériences réordonnées: CTO d'abord, puis coaching startups
#let experiences-adapted = [
  = Expérience Professionnelle

  #exp-palo-it-adapted
  #exp-upwiser-adapted
  #exp-cdiscount-adapted
  #exp-cast
]

// =============================================================================
// SECTIONS ADDITIONNELLES
// =============================================================================

#let sections-adapted = [
  #section-formation
  #section-certifications
  #section-engagement
]

// =============================================================================
// DOCUMENT
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
    #experiences-adapted
    #sections-adapted
  ],
)
