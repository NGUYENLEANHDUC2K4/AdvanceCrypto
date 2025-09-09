from pwn import *

stringCode = "label"
intCode = 13

ascii = lambda s: [ord(c) for c in s]

print(xor(ascii(stringCode), intCode))