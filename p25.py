#import urllib
#
#lakes = []
#for i in range(25):
#	print "Lake " + str(i+1)
#	l = urllib.urlopen("http://butter:fly@www.pythonchallenge.com/pc/hex/lake" + str(i+1) + ".wav")
#	lakes.append(l.read())
#	open("lakewavs/lake" + str(i+1) + ".wav", 'wb').write(lakes[-1])

import binascii, wave

from PIL import Image

for i in range(25):
	im = Image.new("RGB", (60, 60), 0)
	w = wave.open("lakewavs/lake" + str(i+1) + ".wav", 'rb')
	f = w.readframes(w.getnframes())
	pixels = list(f[i:i+3] for i in range(0, len(f), 3))
	pixels = list(tuple(ord(x) for x in c) for c in pixels)
	#print pixels[0:5]
	#for x in pixels: print binascii.b2a_hex(x)
	#colors = list(("#" + binascii.b2a_hex(x)) for x in pixels)
	#i = 0
	#for y in range(60):
	#	for x in range(60):
	#		im.putpixel((x, y), colors[i])
	#		i += 1
	im.putdata(pixels)
	im.save("lakepics/lake" + str(i+1) + ".png")
	


combined = Image.new("RGB", (60*5, 60*5), color=0)
images = list(Image.open("lakepics/lake" + str(i+1) + ".png") for i in range(25))
rows = list(images[i:i+5] for i in range(0, 25, 5))
i = 0
for y in range(5): # 5 pieces per column
	for x in range(5): # 5 pieces per row
		for ya in range(60): # 60 pixels per column
			for xa in range(60): # 60 pixles per row
				combined.putpixel((x*60+xa, y*60+ya), images[i].getpixel((xa, ya)))
		i += 1
		
combined.save("lakepics/combined.png")