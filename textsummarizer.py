# This particular application reads RSS feeds from CNN.com and then summarizes the text from it.

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
  txtsum = map(lambda p: p.text, BeautifulSoup(urllib2.urlopen('http://rss.cnn.com/rss/cnn_topstories.rss').read().decode('utf8'), "lxml").find_all('guid'))
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
	

output:

	
"""

=============================================================================================================================================================


Democratic debate in New York: What to watch - CNNPolitics.com


1 . By MJ Lee and Chris Moody, CNN  Updated 8:29 AM ET, Thu April 14, 2016  New York (CNN)Hillary Clinton and Bernie Sanders will face off in CNN's Democratic presidential debate in Brooklyn Thursday night as they spar ahead of a critical contest in New York — a state where both candidates have deep roots.
2 . This is exactly what @BernieSanders pledged to his supporters that he wouldn't do.


=============================================================================================================================================================


The two Brooklyns await the debate (Opinion) - CNN.com


1 . Set edition preference: Set edition preference: Set edition preference: By Tanwi Nandini Islam   Updated 7:39 AM ET, Thu April 14, 2016  Watch Hillary Clinton and Bernie Sanders take part in the CNN Democratic Debate on Thursday evening at 9 p.m.
2 . Tanwi Nandini Islam is the author of "Bright Lines," which was shortlisted for the Center for Fiction First Novel Prize and a finalist for the Edmund White Award for Debut Fiction.


=============================================================================================================================================================


Bernie and Hillary, stop the nastiness (Opinion) - CNN.com


1 . Set edition preference: Set edition preference: Set edition preference: By Julian Zelizer  Updated 5:36 PM ET, Wed April 13, 2016   Watch Hillary Clinton and Bernie Sanders take part in the CNN Democratic Debate Thursday evening at 9 p.m. ET.Julian Zelizer is a professor of history and public affairs at Princeton University and a New America fellow.
2 . (CNN)In Thursday night's Democratic debate in Brooklyn, Bernie Sanders and Hillary Clinton have an opportunity to restore a constructive tone to their competition and bring back the kind of vibrant ideological debate that until recently shaped much of the primary.


=============================================================================================================================================================


Bernie and Hillary: The toughest call - CNN.com


1 . Set edition preference: Set edition preference: Set edition preference: By Sally Kohn, CNN Political Commentator  Updated 11:01 PM ET, Wed April 13, 2016   Sally Kohn is an activist, columnist and television commentator.
2 . (CNN)Like a lot of New Yorkers, I haven't decided whether I'm voting for Hillary Clinton or Bernie Sanders in next week's New York State primary.


=============================================================================================================================================================


Who'd Putin save from drowning, Erdogan or Poroshenko? - CNN.com


1 . Set edition preference: Set edition preference: Set edition preference: By Don Melvin, CNN  Updated 9:30 AM ET, Thu April 14, 2016   (CNN)[Breaking news update, posted at 9:30 a.m.

"""
