import math

int_list = [14, 6, 11]
p = 29

def find_answer(lst, p):
  result = []
  lst.sort() 
  for i in range(p - 1):
    if pow(i, 2) % p in lst:
      result.append(i)
  return result

print(find_answer(int_list, p))
