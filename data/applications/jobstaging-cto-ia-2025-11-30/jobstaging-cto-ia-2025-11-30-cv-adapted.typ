// CV adapté pour: Lead Developer (futur CTO) React + IA @ Startup
// Date: 2025-11-30
// Score d'adéquation: 85/100

// Imports depuis data/applications/{app_id}/ (3 niveaux de profondeur)
#import "../../../src/neat-cv-local.typ": (
  cv-continued, cv-page-one, cv-setup, email-link, entry, publications,
  contact-info, item-pills, social-links,
)

// Configuration de base
#import "../../../src/shared/config.typ": *

// Expériences modulaires
#import "../../../src/shared/experiences.typ": exp-palo-it, exp-upwiser, exp-cdiscount

// Sections additionnelles
#import "../../../src/shared/sections.typ": section-formation-short, section-certifications

// =============================================================================
// MÉTADONNÉES DOCUMENT
// =============================================================================

#set document(
  title: "CV - Bastien Gallay - Lead Developer CTO @ Startup IA Coaching",
  author: "Bastien Gallay",
  date: datetime.today(),
)

// =============================================================================
// CONFIGURATION ADAPTÉE
// =============================================================================

#let author-adapted = (
  ..author-config,
  position: "Lead Developer / CTO | React & IA Générative",
)

// =============================================================================
// SIDEBAR ADAPTÉE
// =============================================================================

// About adapté : focus React/TypeScript, IA, startups, formations
#let about-text-adapted = [
  CTO avec 23 ans d'expérience tech. Expert React/TypeScript et IA Générative (LLM, RAG, OpenAI, Mistral). 10 ans de formation Agile et Software Craftsmanship. Accompagnement de 100+ startups. Basé Bordeaux, présence Paris régulière.
]

// Skills Tech réordonnés : React/TypeScript en premier
#let skills-tech-adapted = (
  "React",
  "TypeScript",
  "GenAI Dev",
  "Node.js",
  "Python",
  "PostgreSQL",
  "Azure",
)

// Skills Méthodologie : Lean Startup en premier (startup context)
#let skills-methodo-adapted = (
  "Lean Startup",
  "Craftsmanship",
  "TDD",
  "DDD",
  "SAFe",
)

// Skills Leadership
#let skills-leadership-adapted = (
  "Stratégie Tech",
  "Formation",
  "COMEX",
  "Recrutement",
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

  = Tech & IA
  #item-pills(skills-tech-adapted)

  = Méthodologie
  #item-pills(skills-methodo-adapted)

  = Leadership
  #item-pills(skills-leadership-adapted)
]

// =============================================================================
// EXPÉRIENCES ADAPTÉES (par pertinence, 15 dernières années)
// =============================================================================

#let experiences-adapted = [
  = Expérience Professionnelle

  #exp-palo-it
  #exp-upwiser
  #exp-cdiscount
]

// =============================================================================
// SECTIONS ADDITIONNELLES (version courte)
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
