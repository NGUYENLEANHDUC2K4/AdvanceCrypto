from Crypto.Util.number import *
from pwn import xor
import base64

key1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
key1_key2 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
key2_key3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
flag_all_keys = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

key1_bytes = bytes.fromhex(key1)
key1_key2_bytes = bytes.fromhex(key1_key2)
key2_key3_bytes = bytes.fromhex(key2_key3)
flag_all_keys_bytes = bytes.fromhex(flag_all_keys)
key2_bytes = bytes(a ^ b for a, b in zip(key1_bytes, key1_key2_bytes))
key3_bytes = bytes(a ^ b for a, b in zip(key2_bytes, key2_key3_bytes))
flag_bytes = xor(flag_all_keys_bytes, key1_bytes, key2_bytes, key3_bytes)
print(flag_bytes.decode().upper())