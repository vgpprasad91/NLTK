#imort nltk 
import nltk
nltk.download()

# Tokenize sentences
from nltk.tokenize import sent_tokenize, word_tokenize
Sample_text = " Hello I am Mr. Guruprasad. I am looking for a NLP job."
print (sent_tokenize(Sample_text))

# Output : [' Hello I am Mr. Guruprasad.', 'I am looking for a NLP job.']

# Tokenize words 
print (word_tokenize(Sample_text))

# Output : ['Hello', 'I', 'am', 'Mr.', 'Guruprasad', '.', 'I', 'am', 'looking', 'for', 'a', 'NLP', 'job', '.']


