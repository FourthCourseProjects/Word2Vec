import numpy as np


class Co_ocurrenceMatrix:
    def __init__(self, vocabulary):
        self.vocabulary = vocabulary

    def create_from_skip_gram(self, entries_list):
        matrix = self._create_matrix()
        for entry in entries_list:
            for relation in self._relations(self.vocabulary.index(entry.input), entry.output):
                matrix[relation[0], relation[1]] += 1
        return matrix

    def create_from_CBOW(self, entries_list):
        matrix = self._create_matrix()
        for entry in entries_list:
            for relation in self._relations(self.vocabulary.index(entry.output), entry.input):
                matrix[relation[0], relation[1]] += 1
        return matrix

    def _create_matrix(self):
        return np.zeros((len(self.vocabulary), len(self.vocabulary)))

    def _relations(self, index_of_word, list_of_words):
        return [(index_of_word, self.vocabulary.index(word)) for word in list_of_words]
