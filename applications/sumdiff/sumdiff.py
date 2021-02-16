"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

def _add_to_map(num_map, key, value):
  if num_map.get(key) is None:
    num_map[key] = [value]
  else:
    num_map[key].append(value)

def _populate_maps(sums, diffs, num_set):
  for i in range(len(num_set)):
    for j in range(i, len(num_set)):
      num1 = num_set[i]
      num2 = num_set[j]
      val1 = f(num1)
      val2 = f(num2)
      num_sum = val1 + val2
      num_diff = abs(val1 - val2)
      _add_to_map(sums, num_sum, {'vals': (num1, num2), 'f_vals': (val1, val2)})
      if num1 != num2:
        _add_to_map(sums, num_sum, {'vals': (num2, num1), 'f_vals': (val2, val1)})
      _add_to_map(diffs, num_diff, {'vals': (max(num1, num2), min(num1, num2)), 'f_vals': (max(val1, val2), min(val1, val2))})

def _find_equalities(sums, diffs):
  equalities = []
  for total in sums:
    if diffs.get(total) is not None:
      sum_pairs_list = sums.get(total)
      diff_pairs_list = diffs.get(total)
      for s_pair in sum_pairs_list:
        for d_pair in diff_pairs_list:
          equalities.append((s_pair, d_pair))
  return equalities

def print_equalities(equalities):
  for equality in equalities:
    left = equality[0]
    right = equality[1]
    a, b = left.get('vals')
    c, d = right.get('vals')
    A, B = left.get('f_vals')
    C, D = right.get('f_vals')
    print(f'f({a}) + f({b}) = f({c}) - f({d})\t{A} + {B} = {C} - {D}')

# q = set(range(1, 10))
# q = set(range(1, 200))
q = (1, 3, 4, 7, 12)

def f(x):
  return x * 4 + 6

# Your code here
def find_sets(num_set):
  sums = {}
  diffs = {}
  _populate_maps(sums, diffs, tuple(num_set))
  equalities = _find_equalities(sums, diffs)
  return equalities

print_equalities(find_sets(q))
