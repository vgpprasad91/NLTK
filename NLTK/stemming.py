# Stemming words
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

#Stemming a single word

stemm = PorterStemmer()
print(stemm.stem('running'))

#output : run

#Stemming multiple words

sample = ["code","coder","coding","coded"]
print([stemm.stem(w) for w in sample])

#output : ['code', 'coder', 'code', 'code']

#Stemming a sentence

sample_text = "In hope of getting this internship I programmed these nltk programs. Programming with NLTK is easy beacuse of my knowlege with NLP and NLTK."
print([stemm.stem(w) for w in word_tokenize(sample_text)])

#output : ['In', 'hope', 'of', 'get', 'thi', 'internship', 'I', 'program', 'these', 'nltk', 'program', '.', 'Program', 'with', 'NLTK', 'is', 'easi', 'beacus', 'of', 'my', 'knowleg', 'with', 'NLP', 'and', 'NLTK', '.']
