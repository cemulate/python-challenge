from PIL import Image
from matplotlib import pyplot as plot

im = Image.open("bell.png")
data = list(im.getdata())

#pix = list(x for x in data if x[1] == 3 or x[1] == 45)
#print len(list(x for x in data if x[1] == 3))
#print len(list(x for x in data if x[1] == 45))

#print data[0:50]

#pix = list(x for x in data if x[1] == 42)
#for x in pix[0:50]: print list(chr(y) for y in x)
#print len(pix)

#print pix[0:5]
##plot.plot(list(x[0] for x in pix), 'ro')
##plot.plot(list(x[2] for x in pix), 'bo')
#plot.plot(list(x[1] for x in pix), 'go')
#plot.plot(list(x[0] + x[2] for x in pix), 'yo')
#plot.show()

pairs = list(list(y[1] for y in data[i:i+2]) for i in range(0, len(data), 2))
print pairs[0:5]

diff = list(x[1] - x[0] for x in pairs)
#pv = set(diff)
#d = {}
#for v in pv:
#	d[v] = len(list(x for x in diff if x == v))
#	
#import pprint
#pprint.pprint(d)

message = ''.join(chr(abs(x)) for x in diff if abs(x) != 42)
print message