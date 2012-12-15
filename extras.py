from __future__ import division

# Level 30
def factor(n):
	factors = []
	for x in range(1, int(n**0.5)+1):
		for y in range(1, n+1):
			if x*y == n:
				factors.extend((x, y))
	factors = list(set(factors))
	factors.sort()
	return factors

# Level 31
def renderMandelbrot(point, size, outputFile):
	
	from PIL import Image
	import sys
	out = Image.new("P", (640, 480), 0)
	
	x0, y0 = point[0], point[1]
	x1, y1 = x0 + size[0], y0 + size[1]
	
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
					out.putpixel((x, y), its)
					break
				
	out.save(outputFile)

# Level 14 and 17
def phonebookLookup(name):
	import xmlrpclib
	
	print "Establishing connection with phonebook server"
	r = xmlrpclib.Server("http://www.pythonchallenge.com/pc/phonebook.php")
	
	print "Listing capablilites"
	print r.system.listMethods()
	
	print "Finding phone number for " + name + ":"
	num = r.phone(name)
	print num
	
	
def picToSound(picFile, outputFile=None):

	from PIL import Image
	import wave
	import sys, os
	
	try:
		im = Image.open(picFile)
	except:
		print "File does not exist"
		return False
	
	data = im.getdata()
	frames = []
	for t in data: frames.extend(chr(x) for x in t)
	frames = ''.join(frames)
	
	if outputFile == None:
		o = os.path.splitext(os.path.split(sys.argv[1])[-1])[0] + "_output.wav"
	else:
		o = outputFile
	w = wave.open(o, 'wb')
	w.setnchannels(1)
	w.setnframes(1)
	w.setframerate(9600)
	w.setsampwidth(1)
	
	w.writeframes(frames)
	
	w.close()