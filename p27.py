from PIL import Image

#print "...just dump it?"
#
#data = ''.join(chr(x) for x in Image.open("zigzag.gif").getdata())
#print binascii.b2a_hex(data[0:50])
#open("zigzag_dump", 'wb').write(data)

zig = Image.open("zigzag.gif")

def genZigZag(size):
	x, y = 0, 0
	yield (x, y)
	dir = "downleft"
	boundHit = lambda x, y: (x == 0) or (x == size[0]-1) or (y == 0) or (y == size[1]-1)
	maxHit = lambda x, y: x == size[0]-1 and y == size[1]-1
	while True:
		if dir == "downleft":
			if x == size[0]-1:
				y += 1
			else:
				x += 1
			yield (x, y)
			if maxHit(x, y):
				return
			freePass = True
			while not boundHit(x, y) or freePass:
				freePass = False
				x -= 1
				y += 1
				yield (x, y)
			dir = "upright"
		elif dir == "upright":
			if y == size[1]-1:
				x += 1
			else:
				y += 1
			yield (x, y)
			if maxHit(x, y):
				return
			freePass = True
			while not boundHit(x, y) or freePass:
				freePass = False
				x += 1
				y -= 1
				yield (x, y)
			dir = "downleft"

def genZigZagStraight(size):
	dir = "right"
	for y in range(size[1]):
		if dir == "right":
			for x in range(0, size[0], 1):
				yield (x, y)
			dir = "left"
		elif dir == "left":
			for x in range(size[0]-1, -1, -1):
				yield (x, y)
			dir = "right"
			
def genDiags(size):
	sx, sy = 0, 0
	first = True
	hit = lambda x, y: (x > size[0]-1) or (y < 0)
	while True:
		x, y = sx, sy
		while not hit(x, y) or first:
			first = False
			yield (x, y)
			x += 1
			y -= 1
		if sx == size[0]-1:
			break
		if sy == size[1]-1:
			sx += 1
		else:
			sy += 1

#dump = []
#dumpImage = zig.copy()
#for p in genDiags((320, 270)):
#	dump.append(im.getpixel(p))
#dumpImage.putdata(dump)
#dumpImage.save("zigzag_dump_image.png")
#
#dump = ''.join(chr(x) for x in dump)
#print binascii.b2a_hex(dump[0:50])
#open("zigzag_dump", 'wb').write(dump)

import itertools, bz2
from binascii import b2a_hex as phex

p = zig.palette.getdata()[1]
p = list(p[i:i+3] for i in range(0, len(p), 3))
print len(p)

zigData = zig.tostring()
zigTrans = ''.join(p[ord(pi)][0] for pi in zigData)
print "Comparing image data points to palette data points..."
print phex(zigData[:25]) + " ...  " + phex(zigData[-25:])
print "  " +phex(zigTrans[:25]) + " ...  " + phex(zigTrans[-25:])

z = zip(zigData[1:], zigTrans[:-1])
print "Isolating bytes that != their palette entry...\n"
un = list(p[0] for p in z if p[0] != p[1])
un = ''.join(un)

print "Making 1-bit image based on data == palette"
clue = Image.new('1', zig.size, color=1)
cData = list(p[0] == p[1] for p in z)
clue.putdata(cData)
clue.save("zigzag_clue.png")

words = bz2.decompress(un)
print "bz2 decompressed message was:"
print words[0:50] + " ....... " + words[-50:] + "  (Length was " + str(len(words)) + ")\n"

wordList = words.split()
wordList.sort()
print len(wordList)
wordList = list((p[0], len(list(p[1]))) for p in itertools.groupby(wordList))
for x in wordList: print x

print "\nrepeat:switch"