# Word2Vec Models: CBOW and SkipGram
[![Skill Icons](https://skillicons.dev/icons?i=py&perline=2)](https://skillicons.dev)

In this repository, two popular Word2Vec architectures are implemented: CBOW (Continuous Bag of Words) and SkipGram. Both models are used for generating vector representations of words, known as embeddings.

## Description

### CBOW (Continuous Bag Of Words)

CBOW predicts target words from context words. Given a set of context words, CBOW tries to predict the word in the middle.

**Example**:
- Sentence: "The cat sleeps on the bed".
- Context words: "The", "cat", "on", "the".
- Target word: "sleeps".

### SkipGram

SkipGram does the opposite of CBOW. Given a word, it tries to predict the context words.

**Example**:
- Sentence: "The cat sleeps on the bed".
- Target word: "sleeps".
- Context words: "The", "cat", "on", "the".

---
## Contact

(c) 2023 José Juan Hernández Gálvez 
<br>Github: https://github.com/josejuanhernandezgalvez <br>
(c) 2023 Jorge Lang-Lenton Ferreiro          
Github: https://github.com/JorgeLLF
