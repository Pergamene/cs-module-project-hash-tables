# Your code here
lookup_table = {}

def exps(x, y, z):
  val = lookup_table.get((x, y, z))
  if val is None:
    if x <= 0: 
      val = y + z
    if x > 0: 
      val = exps(x-1, y+1, z) + exps(x-2, y+2, z*2) + exps(x-3, y+3, z*3)
    lookup_table[(x, y, z)] = val
  return val

def expensive_seq(x, y, z):
  return exps(x, y, z)

if __name__ == "__main__":
  for i in range(10):
    x = expensive_seq(i*2, i*3, i*4)
    print(f"{i*2} {i*3} {i*4} = {x}")

  print(expensive_seq(150, 400, 800))
