from PIL import Image, ImageDraw
import pprint

gif = Image.open("white.gif")

pos = []
for i in range(133):
	gif.seek(i)
	pos.append(list(gif.getdata()).index(8))
	
print "Indexes of the key pixel in all frames:\n"
print pos, "\n"
	
posSet = list(set(pos))
posSet.sort()

print "Distinct locations of key pixel:"
print posSet, "\n"

vectors = [(-1, 1), (0, 1), (1, 1), (-1, 0), (0, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]
vectors = list((v[0], -1*v[1]) for v in vectors)

vmap = dict(zip(posSet, vectors))

print "Map from index to unit vector:"
pprint.pprint(vmap)


canvas = Image.new("RGB", (500, 200), color="#FFFFFF")
canvasDraw = ImageDraw.Draw(canvas)
	
def generatePaths(start):
	letters = []
	cLetter = []
	xOffset = 0
	cur = start
	cLetter.append(cur)
	for p in pos[1:]:
		v = vmap[p]
		if v == (0, 0):
			letters.append(cLetter)
			cLetter = []
			xOffset += 100
			cur = (xOffset, start[1])
			cLetter.append(cur)
		else:
			cur = tuple(cur[comp] + 3*v[comp] for comp in range(2))
			cLetter.append(cur)
	letters.append(cLetter)
	letters = [word for word in letters if len(word) > 1]
	return letters
		
path = generatePaths((25, 100))

print "Generating point-path for each letter... (separated by a (0, 0))"

print "Connecting the dots..."
for word in path:
	lpairs = list(word[i:i+2] for i in range(len(word)))
	for pair in lpairs:
		canvasDraw.line(pair, 0)
	
canvas.save("joystick_emulation.png")
