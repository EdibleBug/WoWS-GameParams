import struct, zlib, _pickle as pickle, codecs, json

class GPEncode(json.JSONEncoder):
    def default(self, o):
        try:
            for e in ['Cameras', 'DockCamera']:
                o.__dict__.pop(e, o.__dict__)
            return o.__dict__
        except:
            return {}

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

params = open('GameParams.deflate', 'rb')
dec = zlib.decompress(params.read())
params.close()
txt = open('GameParams.txt', 'wb')
txt.write(dec)
txt.close()

original = "GameParams.txt"
destination = "GameParamsU8NB.txt"

content = ''
outsize = 0
with open(original, 'rb') as infile:
    content = infile.read()
with open(destination, 'wb') as output:
    for line in content.splitlines():
        outsize += len(line) + 1
        output.write(line + str.encode('\n'))

f = open('GameParamsU8NB.txt', 'rb')
d = pickle.load(f, encoding='latin1')
f.close()

f = codecs.open('GameParams.json', 'w', encoding='latin1')
f.write(json.dumps(d, cls=GPEncode, sort_keys=True, indent=4, separators=(',', ': ')))
f.close()
