# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
import re

def _get_counts(text):
  letter_freq = {}
  for char in text:
    if re.match(r'[A-Z]', char):
      if letter_freq.get(char) is None:
        letter_freq[char] = 1
      else:
        letter_freq[char] += 1
  return sorted(letter_freq.items(), key=lambda pair: -pair[1])

def _generate_mapping(letter_freq):
  mapping = {}
  frequencies = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U', 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']
  for index, letter_pair in enumerate(letter_freq):
    mapping[letter_pair[0]] = frequencies[index]
  return mapping

def _decode(words, mapping):
  decoded_str = ''
  for index, char in enumerate(words):
    if re.match(r'[A-Z]', char):
      decoded_str += mapping.get(char)
    else:
      decoded_str += char
  return decoded_str

def decode(file):
  with open('applications/markov/input.txt') as f:
    words = f.read()
    letter_freq = _get_counts(words)
    mapping = _generate_mapping(letter_freq)
    return _decode(words, mapping)

print(decode('applications/crack_caesar/ciphertext.txt'))
