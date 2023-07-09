'''
Write a function that, given a string of text (possibly with punctuation and line-breaks), returns an array of the top-3 most occurring words, in descending order of the number of occurrences.
Assumptions:

    A word is a string of letters (A to Z) optionally containing one or more apostrophes (') in ASCII.
    Apostrophes can appear at the start, middle or end of a word ('abc, abc', 'abc', ab'c are all valid)
    Any other characters (e.g. #, \, / , . ...) are not part of a word and should be treated as whitespace.
    Matches should be case-insensitive, and the words in the result should be lowercased.
    Ties may be broken arbitrarily.
    If a text contains fewer than three unique words, then either the top-2 or top-1 words should be returned, or an empty array if a text contains no words.
'''

import re
from collections import Counter

def top_3_words(text):
    # text = text.lower()
    # text = re.sub(r'[^a-z\']+', ' ', text)
    # text = re.sub(r'\'\w+\'', ' ', text)
    # text = re.sub(r'\'', '', text)
    # text = re.sub(r'\s+', ' ', text)
    # text = text.strip()
    # text = text.split(' ')
    # text = [word for word in text if word != '']
    # text = Counter(text).most_common(3)
    # return [word[0] for word in text]
    return [word[0] for word in Counter(re.findall(r"[a-z']+", text.lower())).most_common(3)]

print(top_3_words("a a a  b  c c  d d d d  e e e e e")) # ['e', 'd', 'a']
print(top_3_words("a a c b b")) # ['a', 'b', 'c']
print(top_3_words("a a a  b  c c  d d d d  e e e e e")) # ['e', 'd', 'a']
print(top_3_words("a a c b b")) # ['a', 'b', 'c']