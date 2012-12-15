from __future__ import division
from PIL import Image
import sys

im = Image.open("mandelbrot.gif")
im = im.transpose(Image.FLIP_TOP_BOTTOM)
#im = im.transpose(Image.FLIP_LEFT_RIGHT)

x0, y0 = 0.34000, 0.57000
x1, y1 = 0.37600, 0.59700

diffs = []

for y in range(480):
	if y%20 == 0:
		sys.stdout.write(" .")
	for x in range(640):
		c = complex(x0 + ((x*(x1-x0))/640), y0 + ((y*(y1-y0))/480))
		z = c
		its = 0
		for i in range(0, 128):
			its += 1
			z = z*z + c
			if z.real*z.real + z.imag*z.imag > 4:
				break
		comp = im.getpixel((x, y))
		if its != comp and comp < 127:
			diffs.append(comp)
sys.stdout.write("\n")
			
print len(diffs)
print "Google it in relation with UFO's"

#print ''.join(chr(x) for x in diffs)

#import extras
#f = extras.factor(len(diffs))
#
#width, height = f[1:-1]
#print width, height
#
#out = Image.new("P", (width, height), 0)
#out.palette = im.palette
#out.putdata(diffs)
#out.save("mandelbrot_diffs.png")

print "Done!"