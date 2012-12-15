import urllib, urllib2, os

import string
def isPrintable(s):
	return set(s) <= set(string.printable)

url = "http://butter:fly@www.pythonchallenge.com/pc/hex/unreal.jpg"

website = urllib.urlopen(url)
print website.info()

max = 2123456789
step = 50000000

if os.path.exists("htmlPull.dat"):
	os.remove("htmlPull.dat")

fp = open("htmlPull.dat", 'ab')

def rangeEnd(s):
	i = s.find("-") + 1
	i2 = s.find("/", i)
	return int(s[i:i2])

def doNextPull(byte, dest):
	opener = urllib.FancyURLopener({})
	opener.addheader("range", "bytes=%d-%d" % (byte, byte+1))
	print "Pulling range starting with byte " + str(byte) + "..."
	result = opener.open(url)
	data = result.read()
	dest.append(data)
	s = result.info().getheader("content-range")
	if s is None:
		print "content-range was 0, stopping...\n"
		raise('spam', 'eggs')
	print "content-range was: " + s
	print "content-type was: " + result.info().getheader("content-type")
	if isPrintable(data):
		print "Data was: ----------\n" + data + "\n--------------------\n"
	else:
		print "Data was: ----------\n" + "<Non-text data>" + "\n-------------------\n"
	next = rangeEnd(s) + 1
	return next
	

print "Trying sequential back-to-back reads starting with the range at 0..."

seed = 0
dest = []
jumped = False
while True:
	try:
		seed = doNextPull(seed, dest)
	except:
		break

try:
	seed = pow(2, 31)
	print "Trying to read range at 2^31..."
	seed = doNextPull(seed, dest)
	print "Trying to read range at 2 123 456 712 ... however the hell you were supposed to guess that...."
	seed = 2123456712
	seed = doNextPull(seed, dest)
	
	print "Trying to read range at 1 152 983 631..."
	seed = 1152983631
	seed = doNextPull(seed, dest)
	
	print "Writing the hidden data to a zip file..."
	open("level21.zip", 'wb').write(dest[-1])
	print "done"
	
	
except:
	pass
