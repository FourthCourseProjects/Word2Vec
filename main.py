from TxtReader import TxtReader
from filter.PunctuationRemover import PunctuationRemover
from mapper.Lowerizer import Lowerizer
from mapper.Tokenizer import Tokenizer
from text_representations.CBOW import CBOW
from text_representations.Skipgram import SkipGram

text = TxtReader().read("data/file1.txt")
text = PunctuationRemover().remove(text)
text = text.replace("  ", " ")
text = Tokenizer().tokenize(Lowerizer().lower(text))
print(CBOW().from_(text).to_entries(5)[2])
print(SkipGram().from_(text).to_entries(5)[2])
