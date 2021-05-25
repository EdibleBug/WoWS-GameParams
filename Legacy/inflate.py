import zlib

params = open('GameParams.deflate', 'rb')
dec = zlib.decompress(params.read())
params.close()
txt = open('GameParams.txt', 'wb')
txt.write(dec)
txt.close()
