from CoocurrenceMatrix import Co_ocurrenceMatrix
from VocabularyCreator import VocabularyCreator
from TxtReader import TxtReader
from filter.PunctuationRemover import PunctuationRemover
from mapper.Lowerizer import Lowerizer
from mapper.Tokenizer import Tokenizer
from text_representations.CBOW import CBOW
from text_representations.SkipGram import SkipGram

text = TxtReader().read("data/file1.txt")
text = PunctuationRemover().remove(text)
text = text.replace("  ", " ")
text = Tokenizer().tokenize(Lowerizer().lower(text))
vocabulary = VocabularyCreator().from_tokenized_list(text)
print(Co_ocurrenceMatrix(vocabulary).create_from_skip_gram(SkipGram().from_(text).to_entries(5)))
print(Co_ocurrenceMatrix(vocabulary).create_from_CBOW(CBOW().from_(text).to_entries(5)))
