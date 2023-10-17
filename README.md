# Modelos Word2Vec: CBOW y SkipGram

En este repositorio, se implementan dos populares arquitecturas de Word2Vec: CBOW (Continuous Bag of Words) y SkipGram. Ambos modelos son utilizados para la generación de representaciones vectoriales de palabras, conocidos como embeddings.

## Descripción

### CBOW (Continuous Bag Of Words)

CBOW predice palabras target a partir de palabras de contexto. Dado un conjunto de palabras de contexto, CBOW trata de predecir la palabra en el medio.

**Ejemplo**:
- Oración: "El gato duerme en la cama".
- Palabras de contexto: "El", "gato", "en", "la".
- Palabra target: "duerme".

### SkipGram

SkipGram hace lo opuesto a CBOW. Dada una palabra, intenta predecir las palabras de contexto.

**Ejemplo**:
- Oración: "El gato duerme en la cama".
- Palabra target: "duerme".
- Palabras de contexto: "El", "gato", "en", "la".
