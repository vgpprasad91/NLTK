# Organised Named Entity Recognition
# -*- coding: utf-8 -*-

import nltk
from nltk.corpus import inaugural
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk.chunk import conlltags2tree
from nltk.tree import Tree

result = []
 
nltktag = nltk.ne_chunk(nltk.pos_tag(word_tokenize(inaugural.raw("1789-Washington.txt"))))
	
for subtree in nltktag:
	if type(subtree) == Tree: 
		result.append((" ".join([Y for Y, Z in subtree.leaves()]), subtree.label()))

print(result)
