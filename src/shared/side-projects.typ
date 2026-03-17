// Projets personnels AI Engineering & Specification Driven Development
// Utilisé par les CVs adaptés pour sélectionner les projets pertinents
// Période : 2025-présent (après PALO IT)

#import "../neat-cv-local.typ": entry

// =============================================================================
// PROJETS INDIVIDUELS
// =============================================================================

// Analyseur de rhétorique - détection d'arguments fallacieux
#let project-rhetoric-analyzer = (
  name: "Analyseur de rhétorique",
  description: "Détection d'arguments fallacieux à partir d'articles de presse",
  frameworks: "SpecKit (et Lovable)",
  stack: "",
)

// Prototype de jeu vidéo
#let project-game-prototype = (
  name: "Prototype jeu vidéo",
  description: "Prototypage d'un jeu vidéo avec approche Specification Driven Development",
  frameworks: "BMAD",
  stack: "",
)

// Gestion documentaire personnelle (dont CV)
#let project-document-management = (
  name: "Gestion documentaire",
  description: "Gestion de documents personnels dont CV, avec génération assistée par IA",
  frameworks: "Custom",
  stack: "Typst",
)

// Générateur de musique
#let project-music-generator = (
  name: "Générateur de musique",
  description: "Création d'un générateur de musique exploitant des modèles existants",
  frameworks: "OpenSpec",
  stack: "",
)

// =============================================================================
// LISTE COMPLÈTE
// =============================================================================

#let all-side-projects = (
  project-rhetoric-analyzer,
  project-game-prototype,
  project-document-management,
  project-music-generator,
)

// =============================================================================
// ENTRÉE CV - Version complète (pour CV détaillé ou adapté)
// =============================================================================

#let side-projects-entry = entry(
  title: "Projets personnels - AI Engineering & SDD",
  date: "2025 - Aujourd'hui",
  institution: "Side projects",
  location: "Remote",
)[
  Projets personnels exploitant le Specification Driven Development avec différents frameworks (SpecKit, BMAD, OpenSpec, framework custom) :
  - Analyseur de rhétorique : détection d'arguments fallacieux dans la presse (SpecKit, Lovable)
  - Prototype de jeu vidéo (BMAD)
  - Gestion documentaire personnelle dont CV (Custom)
  - Générateur de musique avec modèles existants (OpenSpec)
]

// =============================================================================
// ENTRÉE CV - Version compacte (1 ligne, pour page 1 des CVs adaptés)
// =============================================================================

#let side-projects-compact = entry(
  title: [Projets personnels - AI Engineering & SDD],
  date: [2025 - Aujourd'hui],
  institution: [Side projects],
  location: [Remote],
)[
  - Multiples projets SDD (SpecKit, BMAD, OpenSpec, framework custom) : analyseur rhétorique, prototype jeu vidéo, gestion documentaire, générateur de musique.
]
