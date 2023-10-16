from Entry import Entry


class SkipGram:
    def __init__(self):
        self.tokenized_text = None

    def from_(self, tokenized_text):
        self.tokenized_text = tokenized_text
        return self

    def to_entries(self, window_size=5):
        if window_size % 2 == 0: raise Exception("Window size must be odd")
        return [self.entry(self.tokenized_text[start_index: start_index + window_size])
                for start_index in range(len(self.tokenized_text) - window_size)]

    def entry(self, tokenized_list):
        return Entry(tokenized_list[:self.core_index(len(tokenized_list)) - 1] +
                     tokenized_list[self.core_index(len(tokenized_list)):],
                     tokenized_list[self.core_index(len(tokenized_list)) - 1])

    def core_index(self, length):
        return int(length / 2 + 1)
