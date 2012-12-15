import gzip

g = gzip.open("deltas.gz")

lines = g.read().splitlines()

lineLength = len(lines[0])

sa = [line[0:lineLength/2-1] for line in lines]
sb = [line[lineLength/2+2:] for line in lines]

print "Parsing columns..."

for i in range(len(lines)):
    print str(i) + "    |" + sa[i] + "|    |" + sb[i] + "|"

import difflib

"Comparing lists..."

diff = difflib.Differ()
delta = diff.compare(sa, sb)

print "\n--------\n"

delta = list(delta)

print "Converting to bytes and dumping each variety of line ('+', '-', ' ')..."

same = [line[2:] for line in delta if line[0] == ' ']
plus = [line[2:] for line in delta if line[0] == '+']
minus = [line[2:] for line in delta if line[0] == '-']

files = [same, plus, minus]
names = ["diff1.png", "diff2.png", "diff3.png"]
types = ["+", "-", "space"]

for i in range(3):
    print "\nDumping " + types[i] + "..."
    lineList = files[i]
    chars = []
    for line in lineList:
        a = line.strip()
        if len(a) > 0:
            b = a.split(" ")
            print b
            chars.extend([chr(int(x,16)) for x in b])
            
    writeStr = ''.join(chars)
    file = open(names[i], 'wb')
    file.write(writeStr)
    file.close()
