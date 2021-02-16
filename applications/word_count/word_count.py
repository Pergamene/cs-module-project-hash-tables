def word_count(s):
  # Your code here
  count_dic = {}
  words = s.split()
  if len(words) != 0:
    for word in words:
      _count_word(count_dic, word)
  return count_dic

def _count_word(dic, word):
  formated_word = _format_word(word)
  if formated_word != '':
    count = dic.get(formated_word)
    if count is None:
      dic[formated_word] = 1
    else:
      dic[formated_word] = count + 1

def _format_word(word):
  return word.lower().translate({ord(i): None for i in '":;,.-+=/\|[]{}()*^&'})

if __name__ == "__main__":
  print(word_count(""))
  print(word_count("Hello"))
  print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
  print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
