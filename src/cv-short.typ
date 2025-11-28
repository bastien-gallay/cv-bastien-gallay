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
#import "shared/sections.typ": sections-page-1-short

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

  // MAIN CONTENT - utilise les modules partagés
  [
    #experiences-page-1
    #sections-page-1-short
  ],
)
