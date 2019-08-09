import collections


text = "aa bb cc dd ee ee ee ff ff gg"
words = text.split()

res = collections.Counter(words)
print(res)
