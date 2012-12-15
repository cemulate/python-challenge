import string

path = "bodyguards.txt"

f = open(path)

def letterCase(c):
	if c.isupper():
		return "U"
	else:
		return "l"
	
print "Occurances of lUUUlUUUl in bodyguards.txt:\n"

occ = []
for line in f:
	caseString = [letterCase(x) for x in line]
	caseString = string.join(caseString,"")
	index = caseString.find("lUUUlUUUl")
	if index > -1:
		occ.append(line[index:index+9])
		print line[index:index+9]

print "\n"  
print "Key letters:"
print [s[4] for s in occ]
print ''.join([s[4] for s in occ])