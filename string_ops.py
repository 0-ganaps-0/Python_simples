# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 14:29:34 2020

@author: ganapathy
"""

zenPython = ''' 
The Zen of Python, by Tim Peters 

Beautiful is better than ugly. 
Explicit is better than implicit. 
Simple is better than complex. 
Complex is better than complicated. 
Flat is better than nested.
Sparse is better than dense. 
Readability counts. 
Special cases aren't special enough to break the rules. 
Although practicality beats purity. 
Errors should never pass silently. 
Unless explicitly silenced. 
In the face of ambiguity, refuse the temptation to guess. 
There should be one-- and preferably only one --obvious way to do it. 
Although that way may not be obvious at first unless you're Dutch. 
Now is better than never. 
Although never is often better than *right* now. 
If the implementation is hard to explain, it's a bad idea. 
If the implementation is easy to explain, it may be a good idea.
'''
words=zenPython.split()
print(len(words))
words=[word.strip(',.-*!') for word in words]
print(words[3])
words=[word.lower() for word in words]
print(words[3])
unique_words=list(set(words))
len(unique_words)
word_frequency={k:words.count(k) for k in unique_words}
print(word_frequency['the'])
frequent_words={k:v for k,v in word_frequency.items() if v>5}
print(len(frequent_words))