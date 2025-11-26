# Checklist de Vérification du CV

Guide systématique pour vérifier la qualité du CV avant diffusion.

## Utilisation

Avant chaque export final du CV, parcourir cette checklist et cocher chaque élément vérifié.
Pour une vérification automatique, exécuter: `just validate`

---

## 1. Compilation

- [ ] Le CV compile sans erreur (`just build`)
- [ ] Le PDF est généré dans `dist/cv.pdf`
- [ ] Le PDF s'ouvre correctement dans un lecteur PDF
- [ ] Le texte est sélectionnable (pas d'image rasterisée)
- [ ] Les liens sont cliquables dans le PDF

## 2. Informations de Contact

- [ ] Nom complet correct
- [ ] Email professionnel valide et à jour
- [ ] Numéro de téléphone actuel (format international)
- [ ] Adresse/localisation cohérente
- [ ] Lien LinkedIn fonctionnel
- [ ] Lien GitHub fonctionnel (si présent)
- [ ] Autres liens vérifiés (portfolio, site personnel)

## 3. Orthographe et Grammaire

- [ ] Titre/intitulé du poste correct
- [ ] Noms d'entreprises orthographiés correctement
- [ ] Noms de technologies orthographiés correctement (ex: TypeScript, PostgreSQL)
- [ ] Pas de fautes d'orthographe dans les descriptions
- [ ] Accents corrects en français
- [ ] Majuscules appropriées (début de phrase, noms propres)

## 4. Cohérence des Dates

- [ ] Format de date uniforme dans tout le CV
- [ ] Dates dans l'ordre chronologique inverse (plus récent en premier)
- [ ] Pas de chevauchement de dates incohérent
- [ ] Dates de début et fin cohérentes pour chaque poste
- [ ] Année actuelle correcte pour les postes en cours ("Présent" ou année courante)

## 5. Cohérence du Style

- [ ] Temps verbal uniforme (présent ou passé, mais pas mélangé)
- [ ] Style d'écriture cohérent (bullet points vs paragraphes)
- [ ] Niveau de détail similaire pour des postes comparables
- [ ] Utilisation cohérente des abréviations
- [ ] Ponctuation uniforme (points en fin de bullet, virgules)

## 6. Formatage Visuel

- [ ] Alignement correct des sections
- [ ] Espacement uniforme entre les sections
- [ ] Police lisible et de taille appropriée
- [ ] Pas de texte coupé ou débordant
- [ ] Sidebar correctement dimensionnée (pas de débordement)
- [ ] Sauts de page aux bons endroits
- [ ] Pas de sections orphelines (titre seul en bas de page)

## 7. Contenu Professionnel

- [ ] Section "À propos" concise et percutante
- [ ] Compétences pertinentes pour le poste visé
- [ ] Descriptions d'expérience axées sur les résultats/impact
- [ ] Certifications avec dates de validité
- [ ] Formations listées avec diplômes obtenus
- [ ] Pas d'informations obsolètes ou non pertinentes

## 8. Confidentialité et Sécurité

- [ ] Pas d'informations sensibles (numéro de sécu, date de naissance exacte)
- [ ] Pas de données confidentielles d'anciens employeurs
- [ ] Pas de mentions de projets sous NDA sans autorisation
- [ ] Pas d'informations financières (salaires, CA)

## 9. Longueur et Lisibilité

- [ ] Longueur appropriée pour le profil (junior: 1p, senior: 2p)
- [ ] Informations clés visibles en moins de 30 secondes (scanning test)
- [ ] Sections prioritaires en haut du CV
- [ ] Pas de zones trop denses ou trop vides

## 10. Vérification Finale

- [ ] Relecture complète à voix haute
- [ ] Test d'affichage sur écran mobile
- [ ] Test d'impression (ou aperçu avant impression)
- [ ] Vérification par une tierce personne si possible
- [ ] Nom de fichier approprié pour l'envoi

---

## Scripts de Vérification Automatique

```bash
# Exécuter toutes les vérifications
just verify

# Vérifications individuelles
just verify-build   # Compilation
just verify-dates   # Cohérence des dates
just verify-format  # Formatage de base

# Exécuter les tests de vérification
just test-verify
```

## Fréquence de Vérification

| Situation | Niveau de vérification |
|-----------|------------------------|
| Modification mineure (typo) | Compilation uniquement |
| Ajout/modification de contenu | Compilation + sections concernées |
| Nouvelle candidature | Checklist complète |
| Mise à jour majeure | Checklist complète + relecture tierce |

---

## Problèmes Courants

| Problème | Solution |
|----------|----------|
| PDF non généré | Vérifier syntaxe Typst, relancer `just build` |
| Texte déborde de la sidebar | Réduire le contenu ou augmenter `sidebar-width` |
| Dates incohérentes | Vérifier ordre chronologique et format |
| Liens cassés | Mettre à jour les URLs dans `cv.typ` |
| Polices manquantes | Vérifier installation des polices système |

---

*Dernière mise à jour: 2025-11-26*
