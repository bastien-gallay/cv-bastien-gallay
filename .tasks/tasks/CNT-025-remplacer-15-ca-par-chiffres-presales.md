# CNT-025: Remplacer "15% CA" par chiffres presales

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | CNT-025 |
| **Titre** | Remplacer "15% CA" par chiffres presales |
| **Statut** | ✅ Terminé |
| **Priorité** | 🟡 Moyenne |
| **Trigramme** | CNT |
| **Section CV** | Experience |
| **Créé le** | 2025-11-26 |
| **Cible** | - |
| **Terminé le** | - |
| **Temps estimé** | 0.5 heures |
| **Temps réel** | - |
| **Branche nécessaire** | Non |

---

## Description

Remplacer l'affirmation "15% de croissance CA" par des chiffres presales plus défendables dans le CV.

### Contexte

L'affirmation "contribution à 15% de croissance CA" (source: townhall mars 2025, audit CNT-014) pose problème :

1. **Difficile à défendre** : Pas de calcul détaillé ni de chiffres précis pour étayer
2. **Contexte contradictoire** : La filiale France PALO IT a fermé pour cessation de paiement quelques mois après cette annonce
3. **Crédibilité** : En entretien, ce chiffre serait difficile à justifier

Les chiffres de contribution presales sont plus fiables et documentés :
- 6+ opportunités majeures gérées simultanément
- Budget €15k-€500k+ par projet

### Objectif

Remplacer les 3 occurrences de "15% CA" par des formulations basées sur les chiffres presales, plus défendables et vérifiables.

---

## Sous-tâches

- [x] Modifier section "À propos" (cv.typ:41)
- [x] Modifier résumé expérience PALO IT (cv.typ:111)
- [x] Modifier détails expérience CTO (cv.typ:312)
- [x] Mettre à jour cv-data.typ (lignes 37, 140, 232)
- [x] Compiler et vérifier le rendu

---

## Notes pour Claude

### Modifications à effectuer

**1. Section "À propos" (cv.typ:41 et cv-data.typ:37)**

Actuel :
```
CTO avec 25 ans d'expérience. Expert IA Générative et transformation Agile. Management de 50 professionnels techniques, contribution à 15% de croissance CA.
```

Nouveau :
```
CTO avec 25 ans d'expérience. Expert IA Générative et transformation Agile. Management de 50 professionnels techniques, pilotage de 6+ opportunités presales (€15k-€500k+).
```

**2. Résumé expérience PALO IT (cv.typ:111 et cv-data.typ:140)**

Actuel :
```
Leadership : Direction stratégie technologique et COMEX. Contribution à 15% de croissance CA. Management de 50 professionnels techniques.
```

Nouveau :
```
Leadership : Direction stratégie technologique et COMEX. Pilotage presales 6+ opportunités (€15k-€500k+). Management de 50 professionnels techniques.
```

**3. Détails expérience CTO (cv.typ:312 et cv-data.typ:232)**

Actuel :
```
Contribution à 15% de croissance du CA
```

Nouveau :
```
Pilotage de 6+ opportunités presales majeures (€15k-€500k+)
```

**Fichiers à modifier:**

- [cv.typ](../../src/cv.typ) (lignes 41, 111, 312)
- [cv-data.typ](../../src/cv-data.typ) (lignes 37, 140, 232)

---

## Notes pour l'utilisateur

- Les chiffres presales proviennent de l'audit CNT-014
- Cette modification aligne le CV avec des données plus défendables en entretien

---

## Références externes

### Fichiers du projet

- [cv.typ:41](../../src/cv.typ#L41) - Section "À propos"
- [cv.typ:111](../../src/cv.typ#L111) - Résumé PALO IT
- [cv.typ:312](../../src/cv.typ#L312) - Détails CTO
- [cv-data.typ](../../src/cv-data.typ) - Données structurées

### Analyses liées

- [CNT-014 audit-report](../resources/analyses/CNT-014/audit-report.md) - Source des chiffres presales
- [CNT-014 recommendations](../resources/analyses/CNT-014/recommendations.md) - Recommandation R02

---

## Tests / Vérifications

- [x] Le CV compile sans erreur (`just build`)
- [x] Le PDF s'affiche correctement
- [x] Les 3 occurrences sont mises à jour de manière cohérente
- [x] Les commits suivent la convention

---

## Historique des modifications

| Date | Action | Détails |
|------|--------|---------|
| 2025-11-26 | Création | Tâche créée suite à discussion sur la défendabilité du chiffre 15% CA |

---

## Résultat final

[À remplir une fois la tâche terminée]
