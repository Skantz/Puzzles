from clib import cbytes
import base64
s1 = "1c0111001f010100061a024b53535009181c"
s2 = "686974207468652062756c6c277320657965"
s1 = cbytes.fromhex(s1)
s2 = cbytes.fromhex(s2)
print((s1 ^ s2).hex())
