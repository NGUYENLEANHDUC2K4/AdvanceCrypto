from Crypto.Util.number import *
import base64

flag = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
codeBytes = long_to_bytes(flag)
print(codeBytes.upper())