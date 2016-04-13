#Parts of Speech tagging using unsupervised machine learning

#get all imports

import nltk
from nltk.corpus import inaugural
from nltk.tokenize import PunktSentenceTokenizer

#Create training and testing data

train_data = inaugural.raw("1789-Washington.txt")
sample_data = inaugural.raw("1793-Washington.txt")

train_tokenizer = PunktSentenceTokenizer(train_data)

def parts_of_speech():
    try:
        print([nltk.pos_tag(nltk.word_tokenize(w)) for w in train_tokenizer.tokenize(sample_data)])

    except Exception as e:
        print(str(e))


parts_of_speech()

#output : [[('Fellow', 'NNP'), ('citizens', 'NNS'), (',', ','), ('I', 'PRP'), ('am', 'VBP'), ('again', 'RB'), ('called', 'VBN'), ('upon', 'NN'), ('by', 'IN'), ('the', 'DT'), ('voice', 'NN'), ('of', 'IN'), ('my', 'PRP$'), ('country', 'NN'), ('to', 'TO'), ('execute', 'VB'), ('the', 'DT'), ('functions', 'NNS'), ('of', 'IN'), ('its', 'PRP$'), ('Chief', 'NNP'), ('Magistrate', 'NNP'), ('.', '.')], [('When', 'WRB'), ('the', 'DT'), ('occasion', 'NN'), ('proper', 'NN'), ('for', 'IN'), ('it', 'PRP'), ('shall', 'MD'), ('arrive', 'VB'), (',', ','), ('I', 'PRP'), ('shall', 'MD'), ('endeavor', 'VB'), ('to', 'TO'), ('express', 'VB'), ('the', 'DT'), ('high', 'JJ'), ('sense', 'NN'), ('I', 'PRP'), ('entertain', 'VBP'), ('of', 'IN'), ('this', 'DT'), ('distinguished', 'VBN'), ('honor', 'NN'), (',', ','), ('and', 'CC'), ('of', 'IN'), ('the', 'DT'), ('confidence', 'NN'), ('which', 'WDT'), ('has', 'VBZ'), ('been', 'VBN'), ('reposed', 'VBN'), ('in', 'IN'), ('me', 'PRP'), ('by', 'IN'), ('the', 'DT'), ('people', 'NNS'), ('of', 'IN'), ('united', 'JJ'), ('America', 'NNP'), ('.', '.')], [('Previous', 'JJ'), ('to', 'TO'), ('the', 'DT'), ('execution', 'NN'), ('of', 'IN'), ('any', 'DT'), ('official', 'JJ'), ('act', 'NN'), ('of', 'IN'), ('the', 'DT'), ('President', 'NNP'), ('the', 'DT'), ('Constitution', 'NNP'), ('requires', 'VBZ'), ('an', 'DT'), ('oath', 'NN'), ('of', 'IN'), ('office', 'NN'), ('.', '.')], [('This', 'DT'), ('oath', 'NN'), ('I', 'PRP'), ('am', 'VBP'), ('now', 'RB'), ('about', 'IN'), ('to', 'TO'), ('take', 'VB'), (',', ','), ('and', 'CC'), ('in', 'IN'), ('your', 'PRP$'), ('presence', 'NN'), (':', ':'), ('That', 'IN'), ('if', 'IN'), ('it', 'PRP'), ('shall', 'MD'), ('be', 'VB'), ('found', 'VBN'), ('during', 'IN'), ('my', 'PRP$'), ('administration', 'NN'), ('of', 'IN'), ('the', 'DT'), ('Government', 'NNP'), ('I', 'PRP'), ('have', 'VBP'), ('in', 'IN'), ('any', 'DT'), ('instance', 'NN'), ('violated', 'VBN'), ('willingly', 'RB'), ('or', 'CC'), ('knowingly', 'VB'), ('the', 'DT'), ('injunctions', 'NNS'), ('thereof', 'VBP'), (',', ','), ('I', 'PRP'), ('may', 'MD'), ('(', '('), ('besides', 'IN'), ('incurring', 'VBG'), ('constitutional', 'JJ'), ('punishment', 'NN'), (')', ')'), ('be', 'VB'), ('subject', 'JJ'), ('to', 'TO'), ('the', 'DT'), ('upbraidings', 'NNS'), ('of', 'IN'), ('all', 'DT'), ('who', 'WP'), ('are', 'VBP'), ('now', 'RB'), ('witnesses', 'NNS'), ('of', 'IN'), ('the', 'DT'), ('present', 'JJ'), ('solemn', 'NN'), ('ceremony', 'NN'), ('.', '.')]]
