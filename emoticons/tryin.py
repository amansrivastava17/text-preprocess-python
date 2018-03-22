from emo import emo
from emoticons import emoticons

for k in emo:
	if k not in emoticons:
		emoticons[k] = 1

fout = open("emoticons.txt", "w")

for k in emoticons:
	print str(k)
	# fout.write(str(k) + "\n")