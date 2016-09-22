#stopwords filtering
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
stopwordlist = set(stopwords.words('english'))
Sample_text = "So, I thought I can prove my skills in NLP by writing programs using NLTK toolkit."
splitwordlist = word_tokenize(Sample_text)
print([w for w in splitwordlist if w not in stopwordlist])

#output : ['So', ',', 'I', 'thought', 'I', 'prove', 'skills', 'NLP', 'writing', 'programs', 'using', 'NLTK', 'toolkit', '.']
