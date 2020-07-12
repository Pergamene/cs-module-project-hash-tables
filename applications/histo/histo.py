# Your code here
def _format_word(word):
  return word.lower().translate({ord(i): None for i in '":;,.-+=/\|[]{}()*^&'})

def _generate_word_list(file):
  words = []
  with open(file) as f:
    text = f.read()
    textArr = text.split()
    for word in textArr:
      words.append(_format_word(word))
    return words

def _count_word(dic, word):
  if word != '':
    count = dic.get(word)
    if count is None:
      dic[word] = '#'
    else:
      dic[word] = count + '#'

def _format_line(line, longest):
  formated_line = line[0]
  return formated_line.ljust(longest+2) + line[1]

def _print_histogram(histogram, longest):
  for line in histogram:
    print(_format_line(line, longest))
    pass

def histogram(file):
  words = _generate_word_list(file)
  dic = {}
  longest = 0
  for word in words:
    if len(word) > longest:
      longest = len(word)
    _count_word(dic, word)
    histogram = sorted(dic.items(), key=lambda pair: (-len(pair[1]), pair[0]))
  _print_histogram(histogram, longest)
  
histogram('applications/histo/robin.txt')
