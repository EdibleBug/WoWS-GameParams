import struct

f = open('GameParams.data', 'rb')
b = []
while 1:
  z = f.read(1)
  if not z:
    break
  b.append(z[0])

f.close()
f = open('GameParams.deflate', 'wb')
f.write(struct.pack('B'*len(b), *b[::-1]))
f.close()
