// Sections additionnelles réutilisables (Formation, Certifications, Engagement)
// Utilisé par cv.typ et cv-short.typ

#import "../neat-cv-local.typ": entry

// =============================================================================
// FORMATION
// =============================================================================

#let formation-dea = entry(
  title: "DEA Réalité Virtuelle et Maîtrise des Systèmes Complexes - Mention Bien",
  date: "2002",
  institution: "INSTN (CEA Saclay)",
  location: "Saclay, France",
)[
  Recherche : _"Comparaison des algorithmes de classification pour la segmentation multitexturées"_.
]

#let formation-maitrise = entry(
  title: "Maîtrise d'Informatique - Mention Bien",
  date: "2001",
  institution: "Université de Picardie Jules Verne",
  location: "Amiens, France",
)[
  Mémoire : _"Complexité des algorithmes quantiques"_.
]

// Section complète avec les deux formations
#let section-formation = [
  = Formation

  #formation-dea
  #formation-maitrise
]

// Section courte avec DEA uniquement
#let section-formation-short = [
  = Formation

  #formation-dea
]

// =============================================================================
// CERTIFICATIONS
// =============================================================================

#let cert-safe = entry(
  title: "SAFe Program Consultant (SPC5)",
  date: "2020",
  institution: "Scaled Agile, Inc.",
)[]

#let cert-scrum = entry(
  title: "Professional Scrum Master (PSM I & II) & Developer (PSD-I)",
  date: "2015-2018",
  institution: "Scrum.org",
)[]

// Section complète avec certifications séparées
#let section-certifications = [
  = Certifications

  #cert-safe
  #cert-scrum
]

// =============================================================================
// ENGAGEMENT COMMUNAUTAIRE
// =============================================================================

#let engagement-agile = entry(
  title: "Organisateur Agile Tour Bordeaux",
  date: "2011 - Aujourd'hui",
  institution: "Agile Tour",
  location: "Bordeaux",
)[
  Organisation de la conférence annuelle (150+ participants). Fondateur Lean Startup Bordeaux (2012-2018). Co-fondateur Collectif Quinconces (2016-2018).
]

#let section-engagement = [
  = Engagement communautaire

  #engagement-agile
]

// =============================================================================
// SECTION COMPLÈTE PAGE 1 (après expériences)
// =============================================================================

// Version complète avec 2 formations
#let sections-page-1-full = [
  #section-formation
  #section-certifications
  #section-engagement
]

// Version courte avec 1 formation
#let sections-page-1-short = [
  #section-formation-short
  #section-certifications
  #section-engagement
]
