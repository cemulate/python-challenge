from PIL import Image, ImageDraw

maze = Image.open("maze.png")
msolved = maze.copy()
mdraw = ImageDraw.Draw(msolved)

def enum(**enums):
	return type('Enum', (), enums)
	
Direction = enum(UP=0, DOWN=1, LEFT=2, RIGHT=3)
	
dirNames = {Direction.UP:"Up",
			Direction.DOWN:"Down",
			Direction.RIGHT:"Right",
			Direction.LEFT:"Left",
			None:"None"}

directions = [Direction.UP, Direction.LEFT, Direction.RIGHT, Direction.DOWN]

Backwards = {Direction.UP:Direction.DOWN,
			 Direction.DOWN:Direction.UP,
			 Direction.LEFT:Direction.RIGHT,
			 Direction.RIGHT:Direction.LEFT}

class PDPair():
	def __init__(self, point, direction):
		self.point = point
		self.direction = direction
		self.dirMoveMap = {Direction.UP:self._moveUp,
						   Direction.DOWN:self._moveDown,
						   Direction.LEFT:self._moveLeft,
						   Direction.RIGHT:self._moveRight}
		
	def __str__(self):
		return "PDPair: " + str(self.point) + "  " + dirNames[self.direction]
		
	def move(self, dir):
		
		"""Returns a new Point-Direction pair formed by moving the specified
		PDPair in a specified direction. The direction attribute of the new
		pair is defined to be along the vector that the PDPair just moved"""
		
		# Calls the appropriate function for the direction
		return self.dirMoveMap[dir]()
		
	def _moveRight(self):
		p = self.point
		return PDPair((p[0]+1, p[1]), Direction.RIGHT)
	def _moveLeft(self):
		p = self.point
		return PDPair((p[0]-1, p[1]), Direction.LEFT)
	def _moveDown(self):
		p = self.point
		return PDPair((p[0], p[1]+1), Direction.DOWN)
	def _moveUp(self):
		p = self.point
		return PDPair((p[0], p[1]-1), Direction.UP)
		
#def trace(seed):
#	paths = []
#	curPath = [seed.point]
#	next = [seed]
#	while len(next) < 2:
#		p = next[0]
#		curPath.append(p.point)
#		possible = [d for d in directions if not d == Backwards[p.direction]]
#		points = [p.move(d) for d in possible]
#		test = lambda pdpair: maze.getpixel(pdpair.point)[0] == 255
#		next = [point for point in points if test(point) is True]
#		if len(next) is 0:
#			return None
#		if len(next) is 1 and next[0].point[1] == 641:
#			return curPath
#	paths.append(curPath)
#	for x in next:
#		r = trace(x)
#		if not r == None:
#			paths.append(r)
#		print "HEllo"
#	return paths
	

#import sys
#sys.setrecursionlimit(1000)
#
#paths = trace(PDPair((80, 1), Direction.DOWN))
#print paths

def deadEnds(image):
	ends = []
	x, y = 0, 0
	for i in range(641-2):
		y += 1
		x = 0
		for j in range(641-2):
			x += 1
			p = image.getpixel((x, y))
			if p != (255, 255, 255, 255):
				adj = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
				adj = [image.getpixel(a) for a in adj]
				adj = filter(lambda p: p != (255, 255, 255, 255), adj)
				if len(adj) == 1:
					#print "CONFIRM!", x, y
					ends.append((x, y))
					image.putpixel((x, y), (255, 255, 255, 255))
	return ends

def trace(seed, image, dataDump=None, draw=True):
	
	"""
	Follows a path starting at seed until it hits an intersection or the end
	of the picture. If draw is True, it will fill in every pixel it passes
	over. If dataDump is non-null, it will append the chr() of the color value
	of each pixel it passes to dataDump
	"""
	
	next = [seed]
	while len(next) == 1:
		p = next[0]
		if p.direction != None:
			possible = [d for d in directions if not d == Backwards[p.direction]]
		else:
			possible = directions
		
		points = [p.move(d) for d in possible]
		test = lambda pdpair: image.getpixel(pdpair.point) != (255, 255, 255, 255)
		try:
			next = filter(test, points)
		except:
			print "Reached edge of image, ending trace"
			return
		if dataDump != None:
			dataDump.append(chr(image.getpixel(p.point)[0]))
		if len(next) == 1 and draw:
			image.putpixel(p.point, (255, 255, 255, 255))
		

import sys
print "Identifying all dead ends in the maze..."
ends = deadEnds(msolved)

sys.stdout.write("Filling dead ends back to their intersection")

# By maze theory, if you fill all dead ends back to the first intersection,
# you will reveal the correct path, assuming there is one, when done

x = int(len(ends)//20)
for i in range(len(ends)):
	end = ends[i]
	trace(PDPair(end, None), msolved)
	if i % x is 0:
		sys.stdout.write(" .")
print "\n"
	
# Now the image contains the one and only one correct path

#msolved.save("maze_solved.png")


start = PDPair((639,0), Direction.DOWN)
dump = []

# Trace the correct path now, without drawing over and with a dataDump
print "Tracing the correct path, dumping color data of red fields..."

trace(start, msolved, dump, False)

# Write every other byte (non-zero) to file
open("maze_dump.zip", 'wb').write(''.join(dump[1::2]))
print "Done."

msolved.save("maze_solved.png")
