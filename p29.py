import urllib, bz2
from binascii import b2a_hex as bth

u = urllib.urlopen("http://repeat:switch@www.pythonchallenge.com/pc/ring/guido.html")

data = u.read()
i = data.find("</html>\n") + len("</html>\n")

silence = data[i:]
lines = silence.split("\n")
message = ''.join(chr(len(x)) for x in lines)
print bz2.decompress(message)
