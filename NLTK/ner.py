#Named Entity Recognition
#Chunking with NLTK with the help of regular expressions

#get all imports

import nltk
from nltk.corpus import inaugural
from nltk.tokenize import PunktSentenceTokenizer

#Create training and testing data

train_data = inaugural.raw("1789-Washington.txt")
sample_data = inaugural.raw("1793-Washington.txt")

train_tokenizer = PunktSentenceTokenizer(train_data)

def named_entity_recognition():
    try:
        print([nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(w)), binary=False).draw() for w in train_tokenizer.tokenize(sample_data)])

    except Exception as e:
        print(str(e))

named_entity_recognition()
