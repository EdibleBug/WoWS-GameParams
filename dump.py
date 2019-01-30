import _pickle as pickle,codecs, json

class GPEncode(json.JSONEncoder):
    def default(self, o):
        try:
            for e in ['Cameras', 'DockCamera']:
                o.__dict__.pop(e, o.__dict__)
            return o.__dict__
        except:
            return {}

f = open('GameParamsU8NB.txt', 'rb')
d = pickle.load(f, encoding='latin1')
f.close()

f = codecs.open('GameParams.json', 'w', encoding='latin1')
f.write(json.dumps(d, cls=GPEncode, sort_keys=True, indent=4, separators=(',', ': ')))
f.close()
