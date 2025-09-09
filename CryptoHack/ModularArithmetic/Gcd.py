a = int(input("Enter a: "))
b = int(input("Enter b: "))
def gcd(a, b):
  if (a == 0):
    return b
  elif (b == 0):
    return a
  if (a > b):
    return gcd(b, a % b)
  else: 
    return gcd(a, b % a)

print(gcd(a, b))