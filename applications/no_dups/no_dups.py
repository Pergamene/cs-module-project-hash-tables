def no_dups(s):
  # Your code here
  word_set = {}
  new_s = ''
  for word in s.split():
    if word_set.get(word) is None:
      word_set[word] = 1
      new_s += f'{word} '
  return new_s.rstrip()

if __name__ == "__main__":
  print(no_dups(""))
  print(no_dups("hello"))
  print(no_dups("hello hello"))
  print(no_dups("cats dogs fish cats dogs"))
  print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
