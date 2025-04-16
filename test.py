from collections import Counter

def count_occurences(word, words):
    return Counter(words.lower().split(" "))[word.lower()]

word = 'python'
words = 'Python Conferences python training python events'

print(count_occurences(word, words))
