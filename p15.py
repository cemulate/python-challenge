from PIL import Image
import itertools

im = Image.open("wire.png")
data = im.getdata()
	
i = 0
p = "wire"
s = ".png"
new = Image.new("RGB", (100, 100))

def nextTuple(previousTuple):
	return tuple((x-2 for x in previousTuple))
	
def tuples(start):
	t = start
	yield t
	while not (2 in t):
		t = nextTuple(t)
		yield t
		
def spiral(size):
	x, y = -1, 0
	for right, down, left, up in tuples((size, size-1, size-1, size-2)):
		for i in range(right):
			x += 1
			yield (x, y)
		for i in range(down):
			y += 1
			yield (x, y)
		for i in range(left):
			x -= 1
			yield (x, y)
		for i in range(up):
			y -= 1
			yield (x, y)

points = spiral(100)

print "Spiraling the wire... "
for pixel in data:
	try:
		p = points.next()
		print p
		new.putpixel(p, pixel)
	except StopIteration:
		break



new.save("wire_new.png")
print "Spiraled wire into new image"