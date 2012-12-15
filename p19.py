import mimetools as mt
import wave, array

f = open("indian.txt", 'rb')

print "Writing initial indian.wav from email text file..."

input = ''.join([x.rstrip("\n") for x in f])
#input = [[x for x in reversed(input[i:i+8])] for i in range(0, len(input), 8)]
#input = sum(input, [])
#input = ''.join(input)

inputFile = open("indian.in", 'wb')
inputFile.write(input)
inputFile.close()

out = open("indian.wav", 'wb')

mt.decode(open("indian.in", 'rb'), out, 'base64')

print "Byteswapping the audio of indian.wav...."

a = array.array('i')
w = wave.open("indian.wav", 'rb')
wout = wave.open("final_indian.wav", 'wb')
a.fromstring(w.readframes(w.getnframes()))
a.byteswap()

wout.setparams(w.getparams())
wout.writeframes(a.tostring())
w.close()
wout.close()

print "Wrote byteswapped file to final_indian.wav"


print "\n\nApologizing to Leopold..."

import urllib, urllib2

info = "sorry"
url = "http://www.pythonchallenge.com/pc/stuff/violin.php"
req = urllib2.Request(url, headers = {'Cookie': 'info=' + urllib.quote_plus(info)})

print "\nHis response was:"
print urllib2.urlopen(req).read()

print "\nHmmmm...."