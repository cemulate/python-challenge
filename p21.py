import binascii
import zlib, bz2
import os

pack = open("level21/package.pack", 'rb').read()
print len(pack)

#if os.path.exists("pack_log.txt"):
#	os.remove("pack_log.txt")
#log = open("pack_log.txt", 'ab')

log = []

def prettyHex(data):
	def addSpaces(s):
		return ' '.join([s[i:i+2] for i in range(0, len(s), 2)])
	
	h = binascii.b2a_hex(data)
	h = [addSpaces(h[i:i+14]) for i in range(0, len(h), 14)]
	return h

def tryZlib(data):
	i = 0
	while True:
		i += 1
		try:
			data = zlib.decompress(data)
			print "Compression " + str(i) + ".... Size was:", len(data)
			log.append(" ")
		except:
			if i is 1:
				# Didn't decompress at all
				raise("Unable to decompress anymore")
			
			return data
		
def tryBz2(data):
	i = 0
	while True:
		i += 1
		try:
			data = bz2.decompress(data)
			print "Compression " + str(i) + ".... Size was:", len(data)
			log.append("#")
		except:
			if i is 1:
				# Didn't decompress at all
				raise("Unable to decompress anymore")
			
			return data
		
def printSample(d):
	print "Data Sample:\n"
	print d[0:50], "\n"
	print prettyHex(d)[0:50], "\n"
	
	
data = pack
justReversed = False
while True:
	try:
		print "\nzlib... "
		data = tryZlib(data)
		justReversed = False
		print "\nbz2... "
		data = tryBz2(data)
	except:
		print "failed\n"
		if justReversed:
			print "Reverse fails as well... exiting"
			break
		print "REVERSING DATA!!!!"
		data = data[::-1]
		log.append("\n")
		justReversed = True

open("pack_decompressed.txt", 'wb').write(data)

print "\n\nFinal data was:"
print data

print "\n\n Logs:\n"
logString = ''.join(log)
print logString

