path = "rareLetters.txt"

s = open(path).read()

letterMap = {}
for c in s:
	if not (c in letterMap):
		letterMap[c] = 1
	else:
		letterMap[c] += 1

print "Occurances of each character:"	
for kv in letterMap:
	print (kv, letterMap[kv])

print "\n"
print "Rare letters:"
rareLetters = [x for x in s if letterMap[x] == 1]

print rareLetters
print "".join(rareLetters)