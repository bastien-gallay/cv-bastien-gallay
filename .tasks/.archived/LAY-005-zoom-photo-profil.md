# LAY-005: Zoomer sur le visage dans la photo de profil

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | LAY-005 |
| **Titre** | Zoomer sur le visage dans la photo de profil |
| **Statut** | ✅ Terminé |
| **Priorité** | 🟡 Moyenne |
| **Trigramme** | LAY |
| **Section CV** | Sidebar |
| **Créé le** | 2025-11-27 |
| **Cible** | - |
| **Terminé le** | 2025-11-27 |
| **Temps estimé** | 0.5 heures |
| **Temps réel** | 0.25 heures |
| **Branche nécessaire** | Non |

---

## Description

La photo de profil actuelle utilise un plan trop éloigné pour un CV. Il faut zoomer légèrement sur le visage pour avoir un cadrage plus serré et professionnel.

### Contexte

Pour un CV, la photo de profil doit montrer clairement le visage du candidat. Un plan éloigné dilue l'impact visuel et peut paraître moins professionnel. Un cadrage plus serré (type portrait) est préférable.

### Objectif

Recadrer la photo de profil pour zoomer sur le visage, en gardant un cadrage harmonieux (visage centré, un peu d'espace au-dessus de la tête).

---

## Sous-tâches

- [ ] Identifier l'image source (identite.png ou profile.png)
- [ ] Recadrer/zoomer sur le visage
- [ ] Remplacer l'image dans src/assets/
- [ ] Vérifier le rendu dans le CV compilé
- [ ] Ajuster si nécessaire

---

## Notes pour Claude

> Instructions spécifiques pour l'assistance IA

Cette tâche nécessite une édition d'image. Options possibles :

1. **Via Python/Pillow** : Recadrer programmatiquement l'image
2. **Manuellement** : Demander à l'utilisateur de fournir une image recadrée
3. **Via ImageMagick** : Utiliser `convert` pour crop/resize

**Outils/commandes à utiliser:**

- `just build` pour vérifier le rendu
- Pillow ou ImageMagick pour le recadrage

**Fichiers à consulter:**

- [src/assets/identite.png](../../src/assets/identite.png) - Photo actuelle
- [src/cv.typ](../../src/cv.typ) - Configuration de l'image (lignes 28-30)

---

## Notes pour l'utilisateur

- Garder l'image originale en backup avant modification
- Le ratio de l'image doit rester cohérent avec la sidebar

---

## Références externes

### Fichiers du projet

- [src/assets/identite.png](../../src/assets/identite.png) - Photo de profil
- [src/cv.typ](../../src/cv.typ) - Fichier CV principal

### Tâches liées

- Aucune

---

## Commits Git associés

### Commit final

```bash
git commit -m "style(assets): 🖼️ zoom on profile photo for better framing

Cropped profile image to focus on face for more professional appearance.

Closes LAY-005"
```

---

## Tests / Vérifications

- [ ] Le CV compile sans erreur (`just build`)
- [ ] La photo est bien cadrée sur le visage
- [ ] L'image n'est pas déformée
- [ ] Le rendu dans la sidebar est harmonieux

---

## Historique des modifications

| Date | Action | Détails |
|------|--------|---------|
| 2025-11-27 | Création | Tâche créée |
| 2025-11-27 | En cours | Début du travail |
| 2025-11-27 | Terminé | Photo recadrée avec succès |

---

## Résultat final

**Ce qui a été fait:**

- Recadrage de photo-profile-pro.jpg (800x800 → 650x650) avec sips
- Crop centré pour zoomer sur le visage
- Vérification du rendu dans le CV compilé

**Difficultés rencontrées:**

- Confusion initiale sur le fichier image utilisé (identite.png vs photo-profile-pro.jpg)
