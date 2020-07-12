import random
import re
  
dic = {'start_word': [], 'end_word': []}

# Read in all the words in one go
with open('applications/markov/input.txt') as f:
  words = f.read()
  words = words.split()
  # TODO: analyze which words can follow other words
  # Your code here
  for i in range(len(words) - 1):
    word = words[i]
    next_word = words[i + 1]
    if re.match(r'^"?[A-Z]\S*', word):
      dic.get('start_word').append(word)
    if re.match(r'\S*[.!?]"?$', word):
      dic.get('end_word').append(word)
    word_list = dic.get(word)
    if word_list is None:
      dic[word] = [next_word]
    else:
      word_list.append(next_word)

def print_sentence():
  word = random.choice(dic.get('start_word'))
  print(word, end=' ')
  while word not in dic.get('end_word'):
    word = random.choice(dic.get(word))
    print(word, end=' ')

# TODO: construct 5 random sentences
# Your code here
for i in range(5):
  print()
  print_sentence()
  print()
