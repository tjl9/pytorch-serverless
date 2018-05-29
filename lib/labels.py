import os, json, collections

with open('lib/labels.json') as f:
	d = dict(map(lambda k: (int(k[0]), k[1]), json.loads(f.read()).items()))
	f.close()

label_dict = collections.OrderedDict(sorted(d.items(), key=lambda t: t[0]))