import urllib, bz2

template = "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing="
newUrl = "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=12345"
findStr = "busynothing is "

message = ''

print "Building message from cookies by following chain..."

while True:
	sock = urllib.urlopen(newUrl)
	htmlSource = sock.read()
	cookies = sock.info().getheaders("Set-Cookie")[0]
	byte = cookies.split(";")[0].split("=")[1]
	message += byte
	sock.close()
	index = htmlSource.find(findStr)
	if index == -1:
		break
	i1 = index+len(findStr)
	newNum = htmlSource[i1:len(htmlSource)]
	newUrl = template + newNum
	print newUrl


print "Got Message:"
print message
print "\nUnquoting and then bz2 decompressing...\n"
print bz2.decompress(urllib.unquote_plus(message))

print "\nFound father to be Leopold. Finding Leopold's phone number from phonebook server\n"

from extras import phonebookLookup
print phonebookLookup("Leopold")

print "\nPhoning Leopold to tell him 'the flowers are on their way'"

import urllib2

info = "the flowers are on their way"
url = "http://www.pythonchallenge.com/pc/stuff/violin.php"
req = urllib2.Request(url, headers = {'Cookie': 'info=' + urllib.quote_plus(info)})

print "\nHis response was:"
print urllib2.urlopen(req).read()