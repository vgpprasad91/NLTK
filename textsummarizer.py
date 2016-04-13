import urllib2
from frequencysummarizer import FrequencySummarizer
from summarizer import get_only_text
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
from string import punctuation
from heapq import nlargest

def freqcnt(summ):
    dictfrq = defaultdict(int)
    for s in summ:
      for w in s:
        if w not in set(stopwords.words('english') + list(punctuation)):
          dictfrq[w] += 1

    for w in dictfrq.keys():
      dictfrq[w] = dictfrq[w]/float(max(dictfrq.values()))
      if dictfrq[w] >= 0.9 or dictfrq[w] <= 0.1:
        del dictfrq[w]
    return dictfrq

def text_summarize(summary, n):
    frecoun = freqcnt([word_tokenize(w.lower()) for w in sent_tokenize(summary)])
    dicttxt = defaultdict(int)
    for i,m in enumerate([word_tokenize(s.lower()) for s in sent_tokenize(summary)]):
      for w in m:
        if w in frecoun:
          dicttxt[i] += frecoun[w]   
    return [sent_tokenize(summary)[j] for j in nlargest(n, dicttxt, key=dicttxt.get)]

def text_summarize_main():
  txtsum = map(lambda p: p.text, BeautifulSoup(urllib2.urlopen('http://feeds.bbci.co.uk/news/rss.xml').read().decode('utf8'), "lxml").find_all('guid'))
  for news in txtsum[:5]:
    headline = BeautifulSoup(urllib2.urlopen(news).read().decode('utf8'), "lxml").title.text
    summary = ' '.join(map(lambda p: p.text, BeautifulSoup(urllib2.urlopen(news).read().decode('utf8'), "lxml").find_all('p')))
    print "\n"
    print '============================================================================================================================================================='
    print "\n"
    print headline
    print "\n"
    m=1;
    for s in text_summarize(summary, 2):
     print m,'.',s
     m=m+1

if __name__ == '__main__':
	text_summarize_main()
