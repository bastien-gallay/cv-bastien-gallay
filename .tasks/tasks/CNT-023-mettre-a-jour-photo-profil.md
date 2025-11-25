# CNT-023: Mettre à jour la photo du CV

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | CNT-023 |
| **Titre** | Mettre à jour la photo du CV |
| **Statut** | ⏳ À faire |
| **Priorité** | 🟡 Moyenne |
| **Trigramme** | CNT |
| **Section CV** | Sidebar |
| **Créé le** | 2025-11-25 |
| **Cible** | - |
| **Terminé le** | - |
| **Temps estimé** | 1.5 heures |
| **Temps réel** | - |
| **Branche nécessaire** | Non |

---

## Description

Remplacer la photo actuelle du CV par la photo professionnelle `photo-profile-pro.jpg` disponible dans `src/assets/`. Cette nouvelle photo devra potentiellement être recadrée, redimensionnée ou ajustée pour s'adapter au format requis par le template neat-cv.

### Contexte

Le CV utilise actuellement une photo de profil (`identite.png`) mais une nouvelle photo professionnelle de meilleure qualité est disponible (`photo-profile-pro.jpg`). Cette photo présente un cadrage plus professionnel avec fond neutre et chemise blanche, ce qui correspond mieux aux standards d'un CV professionnel.

### Objectif

- Intégrer la nouvelle photo professionnelle dans le CV
- S'assurer que la photo est correctement dimensionnée et cadrée pour le format sidebar du CV
- Vérifier que le rendu PDF est optimal (qualité, dimensions, positionnement)
- Supprimer ou archiver l'ancienne photo si nécessaire

---

## Sous-tâches

- [ ] Analyser les dimensions et format requis par le template neat-cv pour la photo
- [ ] Examiner la photo actuelle (identite.png) pour comprendre les spécifications
- [ ] Préparer photo-profile-pro.jpg (recadrage, redimensionnement si nécessaire)
- [ ] Mettre à jour la référence dans cv.typ
- [ ] Compiler le CV et vérifier le rendu PDF
- [ ] Ajuster si nécessaire (taille, qualité, positionnement)
- [ ] Décider du sort de l'ancienne photo (conserver en backup ou supprimer)

---

## Notes pour Claude

> Instructions spécifiques pour l'assistance IA

**Actions à réaliser:**

1. Lire le fichier cv.typ pour identifier où et comment la photo est intégrée
2. Vérifier les dimensions de l'image actuelle (identite.png)
3. Évaluer si photo-profile-pro.jpg nécessite un traitement (recadrage, conversion)
4. Si nécessaire, proposer un script ou commande pour préparer l'image
5. Mettre à jour la référence dans cv.typ
6. Compiler et vérifier le résultat

**Outils/commandes à utiliser:**

- `just build` - Compiler le CV
- Outils image (ImageMagick, sips, ou équivalent) pour traiter l'image si nécessaire
- Lecteur PDF pour vérifier le rendu final

**Fichiers à consulter:**

- [cv.typ](../../src/cv.typ) - Configuration de la photo
- [src/assets/photo-profile-pro.jpg](../../src/assets/photo-profile-pro.jpg) - Nouvelle photo
- [src/assets/identite.png](../../src/assets/identite.png) - Photo actuelle

**Considérations techniques:**

- Le template neat-cv accepte probablement différents formats (PNG, JPG)
- La photo est affichée dans la sidebar (largeur limitée à 4.5cm)
- Vérifier le poids du fichier pour ne pas alourdir le PDF inutilement
- S'assurer que la qualité reste optimale après compilation

---

## Notes pour l'utilisateur

> Rappels, références, notes personnelles

**Points d'attention:**

- La nouvelle photo (photo-profile-pro.jpg) semble avoir un cadrage portrait standard
- Le fond est neutre (gris clair), ce qui est idéal pour un CV
- La chemise blanche donne un aspect professionnel
- Vérifier que le recadrage met bien en valeur le visage

**Décisions à prendre:**

- Faut-il conserver l'ancienne photo en backup ou la supprimer ?
- Le format JPG est-il optimal ou faut-il convertir en PNG ?
- La résolution actuelle est-elle suffisante ou faut-il l'optimiser ?

---

## Références externes

### Fichiers du projet

- [cv.typ:6-37](../../src/cv.typ#L6-L37) - Configuration document incluant la photo
- [src/assets/](../../src/assets/) - Dossier des assets images

### Tâches liées

- Aucune tâche directement liée

### Ressources

- Documentation neat-cv: Template 0.4.0
- Standards CV professionnels : photo fond neutre, cadrage buste, tenue professionnelle

---

## Commits Git associés

### En cours de travail

```bash
git commit -m "content(sidebar): 🖼️ update profile photo

Replace identite.png with photo-profile-pro.jpg

Refs CNT-023"
```

### Commit final

```bash
git commit -m "content(sidebar): 🖼️ update CV profile photo to professional version

- Replace identite.png with photo-profile-pro.jpg
- Adjust image dimensions for optimal sidebar rendering
- Verify PDF output quality

Closes CNT-023"
```

**Format suggéré:**

- **Type**: content
- **Scope**: sidebar
- **Emoji**: 🖼️ (image/photo)

---

## Tests / Vérifications

- [ ] Le CV compile sans erreur (`just build`)
- [ ] Le PDF s'affiche correctement
- [ ] La photo est bien positionnée dans la sidebar
- [ ] La qualité de la photo est optimale (pas de pixelisation)
- [ ] La taille du fichier PDF reste raisonnable
- [ ] Le cadrage met bien en valeur le visage
- [ ] Les proportions sont respectées (pas de déformation)

---

## Historique des modifications

| Date | Action | Détails |
|------|--------|---------|
| 2025-11-25 | Création | Tâche créée |

---

## Résultat final

[À remplir une fois la tâche terminée]

**Ce qui a été fait:**

- [À compléter]

**Difficultés rencontrées:**

- [À compléter]

**Améliorations futures:**

- [À compléter]
