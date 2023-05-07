from clib import cbytes
import base64
s1 = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
s1 = cbytes.fromhex(s1)
ascii_ = ''.join(chr(i) for i in range(128))
for s2 in ascii_:
  s2 = cbytes(s2*len(s1), encoding="ascii")
  print((s1 ^ s2).decode())
