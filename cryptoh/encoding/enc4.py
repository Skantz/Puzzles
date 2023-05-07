import os
try:
  from Crypto.Util.number import *
except ModuleNotFoundError:
  os.system("sh -c \"pip3 install PyCryptodome\"")
import base64
s = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
b = long_to_bytes(s)
print(b)

