# Métriques calculables sur un texte en langage naturel

Document de référence pour l'amélioration du [prototype d'assistant de rédaction](2026-01-16-proto-assistant-rédaction.md).

## Contexte

L'objectif est d'intégrer des métriques objectives dans un processus de rédaction assistée. Ces métriques permettent de :

- Donner un feedback quantitatif à l'utilisateur
- Détecter des problèmes de lisibilité ou de style
- Suivre l'évolution de la qualité du texte au fil des itérations
- Comparer différentes versions d'un même texte

## Catégories de métriques

### Métriques de lisibilité

Formules développées pour estimer la difficulté de lecture d'un texte.

| Métrique | Description | Formule simplifiée |
|----------|-------------|-------------------|
| Flesch Reading Ease | Score 0-100, plus élevé = plus facile | 206.835 - 1.015×(mots/phrases) - 84.6×(syllabes/mots) |
| Flesch-Kincaid Grade | Niveau scolaire américain requis | 0.39×(mots/phrases) + 11.8×(syllabes/mots) - 15.59 |
| Gunning Fog Index | Années d'éducation nécessaires | 0.4×[(mots/phrases) + 100×(mots complexes/mots)] |
| SMOG Index | Similaire à Fog, plus précis sur textes courts | 1.0430×√(polysyllabes×30/phrases) + 3.1291 |
| Coleman-Liau Index | Basé sur les caractères (pas les syllabes) | 0.0588×L - 0.296×S - 15.8 (L=lettres/100 mots, S=phrases/100 mots) |
| Automated Readability Index | Niveau scolaire, basé sur caractères | 4.71×(caractères/mots) + 0.5×(mots/phrases) - 21.43 |

### Métriques structurelles

Statistiques descriptives sur la structure du texte.

| Métrique | Description |
|----------|-------------|
| Nombre de phrases | Total des phrases dans le texte |
| Nombre de mots | Total des tokens (hors ponctuation) |
| Longueur moyenne des phrases | Mots par phrase en moyenne |
| Longueur moyenne des mots | Caractères par mot en moyenne |
| Nombre de syllabes | Total des syllabes (via Pyphen pour le français) |
| Syllabes par mot | Moyenne de syllabes par mot |

### Métriques lexicales

Indicateurs de richesse et diversité du vocabulaire.

| Métrique | Description | Calcul |
|----------|-------------|--------|
| Type-Token Ratio (TTR) | Richesse lexicale | mots uniques / mots totaux |
| Densité lexicale | Proportion de mots pleins | (noms + verbes + adjectifs + adverbes) / mots totaux |
| Hapax Legomena | Mots n'apparaissant qu'une fois | count(mots avec fréquence = 1) |

### Métriques stylistiques (via analyse POS)

Distribution des parties du discours et indicateurs de style.

| Métrique | Description |
|----------|-------------|
| Distribution POS | Répartition noms, verbes, adjectifs, adverbes, etc. |
| Ratio verbes/noms | Équilibre entre action et description |
| Ratio actif/passif | Dynamisme du texte |
| Densité d'adverbes | Souvent signe de style faible si trop élevée |
| Ratio pronoms personnels | Équilibre je/nous/on/il |

### Métriques syntaxiques

Complexité de la structure des phrases.

| Métrique | Description |
|----------|-------------|
| Profondeur syntaxique moyenne | Distance moyenne à la racine dans l'arbre de dépendances |
| Distance de dépendance | Écart moyen entre un mot et son gouverneur |
| Ratio de phrases complexes | Proportion de phrases avec subordonnées |

### Métriques de cohérence

Continuité thématique et logique du texte.

| Métrique | Description |
|----------|-------------|
| Similarité cosinus entre phrases | Proximité sémantique des phrases consécutives (via embeddings) |
| Répétition thématique | Récurrence des mots-clés principaux |
| Chaînes de référence | Cohérence des pronoms avec leurs antécédents |

## Bibliothèques Python pour le français

### textstat

Bibliothèque simple pour les métriques de lisibilité.

```python
import textstat

textstat.set_lang("fr")  # Active Pyphen pour le comptage syllabique français

text = "Votre texte ici..."

# Métriques de lisibilité
textstat.flesch_reading_ease(text)
textstat.flesch_kincaid_grade(text)
textstat.gunning_fog(text)
textstat.smog_index(text)
textstat.coleman_liau_index(text)
textstat.automated_readability_index(text)

# Statistiques descriptives
textstat.sentence_count(text)
textstat.lexicon_count(text)
textstat.syllable_count(text)
textstat.avg_sentence_length(text)
textstat.avg_syllables_per_word(text)
```

**Installation** : `pip install textstat`

**Limite** : Les formules de lisibilité sont calibrées pour l'anglais. Le comptage syllabique fonctionne en français, mais les seuils d'interprétation sont approximatifs.

### spaCy avec modèle français

Analyse linguistique complète : tokenisation, lemmatisation, POS tagging, parsing syntaxique.

```python
import spacy
from collections import Counter

nlp = spacy.load("fr_core_news_md")
doc = nlp("Votre texte ici...")

# Statistiques structurelles
nb_phrases = len(list(doc.sents))
nb_tokens = len([t for t in doc if not t.is_punct and not t.is_space])
nb_mots_uniques = len(set([t.lemma_ for t in doc if not t.is_punct]))

# Type-Token Ratio
ttr = nb_mots_uniques / nb_tokens

# Distribution POS
pos_counts = Counter([t.pos_ for t in doc])

# Densité lexicale
mots_pleins = ["NOUN", "VERB", "ADJ", "ADV"]
densite = sum(pos_counts.get(p, 0) for p in mots_pleins) / nb_tokens

# Profondeur syntaxique moyenne
depths = [len(list(token.ancestors)) for token in doc]
avg_depth = sum(depths) / len(depths) if depths else 0
```

**Installation** :

```bash
pip install spacy
python -m spacy download fr_core_news_md
```

**Modèles disponibles** :

- `fr_core_news_sm` : petit, rapide
- `fr_core_news_md` : moyen, bon compromis
- `fr_core_news_lg` : grand, plus précis

### TextDescriptives

Extension spaCy qui calcule automatiquement de nombreuses métriques.

```python
import spacy
import textdescriptives as td

nlp = spacy.blank("fr")
nlp.add_pipe("textdescriptives/all")

doc = nlp("Votre texte ici...")
df = td.extract_df(doc)
```

**Métriques incluses** :

- `descriptive_stats` : longueur tokens, phrases, syllabes
- `readability` : Flesch, Gunning Fog, SMOG, etc.
- `dependency_distance` : complexité syntaxique
- `pos_proportions` : distribution des parties du discours
- `coherence` : cohérence entre phrases

**Installation** : `pip install textdescriptives`

## Fiabilité des métriques pour le français

| Métrique | Bibliothèque | Fiabilité FR | Notes |
|----------|--------------|--------------|-------|
| Longueur phrases/mots | spaCy/textstat | Excellente | Tokenisation fiable |
| Comptage syllabes | textstat (Pyphen) | Bonne | Dictionnaire français intégré |
| Type-Token Ratio | spaCy | Excellente | Indépendant de la langue |
| Distribution POS | spaCy | Bonne | Modèle entraîné sur corpus français |
| Densité lexicale | spaCy | Excellente | Basé sur POS tagging |
| Flesch Reading Ease | textstat | Approximative | Formule calibrée pour l'anglais |
| Profondeur syntaxique | spaCy | Bonne | Parser entraîné sur français |
| Cohérence (embeddings) | TextDescriptives | Bonne | Dépend du modèle de vecteurs |

## Comment chaque métrique aide à améliorer un texte

### Longueur moyenne des phrases

**Problème détecté** : Phrases trop longues (> 25 mots) ou trop courtes (< 8 mots).

**Action corrective** :

- Phrases longues : découper en plusieurs phrases, supprimer les incises inutiles
- Phrases courtes : combiner des idées liées, ajouter des connecteurs

**Cible recommandée** : 15-20 mots par phrase pour un texte professionnel.

### Type-Token Ratio (TTR)

**Problème détecté** : TTR bas (< 0.4) indique des répétitions excessives.

**Action corrective** :

- Identifier les mots répétés via une analyse de fréquence
- Remplacer par des synonymes ou reformuler
- Utiliser des pronoms pour éviter les répétitions de noms

**Cible recommandée** : TTR > 0.5 pour un texte varié.

### Densité lexicale

**Problème détecté** :

- Densité haute (> 0.6) : texte dense, difficile à lire
- Densité basse (< 0.4) : texte creux, trop de mots outils

**Action corrective** :

- Densité haute : ajouter des connecteurs, simplifier les phrases
- Densité basse : remplacer les périphrases par des termes précis

**Cible recommandée** : 0.45-0.55 pour un équilibre optimal.

### Flesch Reading Ease

**Problème détecté** : Score bas (< 30) indique un texte difficile.

**Action corrective** :

- Raccourcir les phrases
- Remplacer les mots polysyllabiques par des équivalents simples
- Éviter le jargon technique non nécessaire

**Cible recommandée** : 50-70 pour un texte grand public, 30-50 pour un texte technique.

### Distribution des parties du discours

**Problème détecté** :

- Trop de noms : texte statique, descriptif
- Trop de verbes : texte haché, actions sans contexte
- Trop d'adverbes : style faible, manque de verbes forts

**Action corrective** :

- Excès de noms : transformer les nominalisations en verbes ("la réalisation de" → "réaliser")
- Excès d'adverbes : remplacer "verbe + adverbe" par un verbe plus précis ("marcher lentement" → "flâner")

**Cible recommandée** : Équilibre naturel, ratio verbes/noms entre 0.4 et 0.8.

### Profondeur syntaxique

**Problème détecté** : Profondeur élevée (> 4) indique des phrases complexes, imbriquées.

**Action corrective** :

- Découper les phrases avec plusieurs niveaux de subordination
- Transformer les relatives en phrases indépendantes
- Simplifier les constructions passives

**Cible recommandée** : Profondeur moyenne < 3 pour un texte accessible.

### Ratio de pronoms personnels

**Problème détecté** :

- Trop de "je" : texte égocentrique
- Absence de "nous" : manque d'inclusion
- Trop de "on" : imprécision, déresponsabilisation

**Action corrective** :

- Équilibrer "je" (expérience personnelle) et "nous" (collaboration)
- Remplacer "on" par des sujets précis quand possible

**Cible recommandée pour LinkedIn** : Ratio je/(je+nous) entre 0.5 et 0.7.

### Cohérence (similarité entre phrases)

**Problème détecté** : Faible similarité entre phrases consécutives indique des sauts thématiques.

**Action corrective** :

- Ajouter des transitions explicites
- Réorganiser les paragraphes par thème
- Introduire des rappels du sujet principal

**Cible recommandée** : Similarité moyenne > 0.3 entre phrases consécutives.

## Application au prototype d'assistant de rédaction

### Métriques à afficher à chaque itération

Pour un texte LinkedIn (section "Infos"), ces métriques sont particulièrement pertinentes :

```python
metriques_iteration = {
    "longueur_totale": nb_tokens,              # Limite LinkedIn : ~2600 caractères
    "nb_phrases": nb_phrases,
    "longueur_phrase_moy": avg_sentence_len,   # Cible : 15-20
    "ttr": ttr,                                # Cible : > 0.5
    "ratio_je_nous": ...,                      # Équilibre personnel/collectif
}
```

### Analyse en fin de rédaction

Métriques pour une analyse globale avant validation :

```python
metriques_finales = {
    "flesch_score": flesch,                    # Interprétation approximative
    "densite_lexicale": densite,               # Cible : 0.45-0.55
    "profondeur_syntaxique": avg_depth,        # Cible : < 3
    "coherence_moyenne": coherence,            # Cible : > 0.3
}
```

### Intégration dans le workflow

1. **Début d'itération** : afficher les métriques du texte actuel
2. **Après rédaction** : comparer avant/après, signaler les dégradations
3. **Fin de rédaction** : rapport complet avec recommandations

## Références

- [textstat sur PyPI](https://pypi.org/project/textstat/)
- [GitHub textstat](https://github.com/textstat/textstat)
- [spaCy - Modèles français](https://spacy.io/models/fr)
- [TextDescriptives sur GitHub](https://github.com/HLasse/TextDescriptives)
- [Publication TextDescriptives (JOSS)](https://joss.theoj.org/papers/10.21105/joss.05153.pdf)
