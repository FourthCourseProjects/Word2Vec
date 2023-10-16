class VocabularyCreator:
    def from_text_list(self, text_list):
        result = []
        for token_list in text_list:
            result.append(self.from_tokenized_list(token_list))
        return set(result)

    def from_tokenized_list(self, token_list):
        return list(set(token_list))
