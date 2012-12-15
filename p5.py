import urllib

template = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
newUrl = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=8022"
findStr = "nothing is "

while True:
	sock = urllib.urlopen(newUrl)
	htmlSource = sock.read()
	sock.close()
	index = htmlSource.find(findStr)
	if index == -1:
		break
	i1 = index+len(findStr)
	newNum = htmlSource[i1:len(htmlSource)]
	newUrl = template + newNum
	print newUrl
	
print "\n"
print "Final url is:"
print newUrl

