from pwn import *

input = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
hexCode = bytes.fromhex(input)
flagFormat1 = "crypto{"
flagFormat2 = "}"
firstKey = xor(flagFormat1.encode(), hexCode[:7])
secondKey = xor(flagFormat2.encode(), hexCode[-1:])
key = firstKey + secondKey
print(xor(hexCode, key).upper())