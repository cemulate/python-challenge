import string
from PIL import Image, ImageDraw

f1 = open("firstpic.txt")
f2 = open("secondpic.txt")

im = Image.new("RGB", (640,487), color="white")
print im
draw = ImageDraw.Draw(im)

print "Connecting the dots specified in firstpic.txt and secondpic.txt"

for f in [f1, f2]:

	s1 = f.read()
	s1 = string.replace(s1, "\n", "")
	s1vals = s1.split(",")
	vals = [int(x) for x in s1vals]
	points = [(vals[i],vals[i+1]) for i in range(0, len(vals), 2)]
	print "Points:"
	print points
	print "\n\n"
	
	for i in range(1, len(points)):
		p1 = points[i-1]
		p2 = points[i]
		print (p1, p2)
		draw.line([p1, p2], fill="black")

	
im.save("good2.png")
print "Saved imaged of connected dots"