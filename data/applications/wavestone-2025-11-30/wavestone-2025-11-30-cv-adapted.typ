// CV adapté pour: Consultant Senior GenAI / Copilots @ Wavestone
// Date: 2025-11-30
// Score d'adéquation: 78/100

#import "../../../src/neat-cv-local.typ": (
  cv-continued, cv-page-one, cv-setup, email-link, entry, publications,
  contact-info, item-pills, social-links,
)

#import "../../../src/shared/config.typ": *
#import "../../../src/shared/experiences.typ": *
#import "../../../src/shared/sections.typ": *

// =============================================================================
// CONFIGURATION ADAPTÉE - Consultant Senior GenAI @ Wavestone
// =============================================================================

#let author-adapted = (
  ..author-config,
  // Titre adapté pour mettre en avant GenAI et Copilot
  position: "Expert IA Générative & Copilots | CTO Advisory",
)

// =============================================================================
// SIDEBAR ADAPTÉE
// =============================================================================

// Texte "A propos" adapté pour Wavestone (focus GenAI, Copilot, transformation)
#let about-text-adapted = [
  CTO avec 25 ans d'expérience. Créateur de Gen-e2 (framework IA). Expert Microsoft Copilot : 20-40 certifications délivrées. Pilotage presales GenAI (€15k-€500k+). Conduite du changement et transformation digitale. Basé Bordeaux, mobilité Paris.
]

// Skills réordonnés selon les mots-clés ATS Wavestone
#let skills-leadership-adapted = (
  "CTO Advisory",      // Terme de l'offre
  "COMEX",
  "Conduite changement", // Terme de l'offre
  "Formation",
)

#let skills-tech-adapted = (
  "GenAI Dev",         // IA Générative prioritaire
  "Copilot",           // Terme clé de l'offre
  "Azure",             // Écosystème Microsoft
  "Python",
  "TypeScript",
  "React",
  "Node.js",
)

#let skills-methodo-adapted = (
  "Design Thinking",   // Mentionné dans l'offre
  "SAFe",
  "Lean Startup",
  "Craftsmanship",
  "TDD",
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

// Expérience PALO IT enrichie avec mots-clés Wavestone (GenAI, Copilot, transformation)
#let exp-palo-it-adapted = entry(
  title: "Consultant Technique Senior → Chief Technology Officer",
  date: "02/2021 - 08/2025",
  institution: "PALO IT",
  location: "Bordeaux/Paris, France",
)[
  - *IA Générative & Copilots :* Conception de Gen-e2, framework de développement accéléré par IA. Délivrance de 20-40 certifications GitHub Copilot. Partenariats Microsoft/GitHub, Mistral (Codestral).
  - *CTO Advisory :* Direction de la stratégie technologique et participation COMEX. Accompagnement CTOs clients (Bodic, Systel). Audit et conseil architecture.
  - *Presales GenAI :* Pilotage de 6+ opportunités majeures (€15k-€500k+). Clients : Natixis, CEVA Logistics, Aviva, Groupe BZ.
  - *Transformation digitale :* Learn & Lunch IA hebdomadaires, ateliers Hands-on. Organisation Tech\&Toast (70+ professionnels). Initiative Quantum Computing.
  - *Stack :* Azure (Databricks, Cosmos DB), OpenAI, Anthropic, Python, TypeScript.
]

// Expérience Upwiser adaptée (coaching, transformation, design thinking)
#let exp-upwiser-adapted = entry(
  title: "Gérant & Coach Agile",
  date: "09/2013 - 02/2021",
  institution: "Upwiser",
  location: "Bordeaux, France",
)[
  - *Conduite du changement :* Transformations Agiles à l'échelle (SAFe) pour grands comptes (Dekra, i-BP, 80+ personnes).
  - *CTO Advisory :* Coaching CTOs et structuration R&D pour scale-ups (Dronisos, Wanteeed, Nalo, SeLoger).
  - *Design Thinking :* Animation formations Agile, Lean, Design Thinking (~15 sessions/an). Fondateur Lean Startup Bordeaux.
]

// CDiscount condensé
#let exp-cdiscount-adapted = entry(
  title: "Chef de projet technique et Scrum Master",
  date: "10/2010 - 10/2013",
  institution: "CDiscount",
  location: "Bordeaux, France",
)[
  - Responsable technique plateforme paiement (1 milliard € CA). Gestion Scrum/Scrumban.
]

// Expériences réordonnées: CTO/GenAI d'abord, puis transformation
#let experiences-adapted = [
  = Expérience Professionnelle

  #exp-palo-it-adapted
  #exp-upwiser-adapted
  #exp-cdiscount-adapted
]

// =============================================================================
// SECTIONS ADDITIONNELLES
// =============================================================================

#let sections-adapted = [
  #section-formation-short
  #section-certifications
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
