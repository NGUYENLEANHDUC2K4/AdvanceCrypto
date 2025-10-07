from pwn import * # pip install pwntools
import json
from Crypto.Util.number import bytes_to_long, long_to_bytes
import base64
import codecs

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


for i in range(101):
    received = json_recv()

    content = received["encoded"]

    if received["type"] == "base64":
        decoded = (base64.b64decode((content.encode()))).decode()
    elif received["type"] == "hex":
        decoded = bytes.fromhex(content.replace('0x', '')).decode()
    elif received["type"] == "rot13":
        decoded = codecs.decode(content, 'rot_13')
    elif received["type"] == "bigint":
        decoded = bytes.fromhex(content.replace("0x", "")).decode()
    elif received["type"] == "utf-8":
        decoded = ''.join([chr(c) for c in content])
    print("Received type: ")
    print(received["type"])
    print("Received encoded value: ")
    print(received["encoded"])

    to_send = {
        "decoded": decoded
    }
    json_send(to_send)
