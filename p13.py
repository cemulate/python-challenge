f = open("evil2.gfx", "rb")

s = f.read()
print len(s)

print "Deshuffling mashup..."

prefix = "evil_decoded"
suffix = ".jpg"
for i in range(5):
    sout = s[i::5]
    fout = open(prefix+str(i)+suffix, 'wb')
    fout.write(sout)

print "Deshuffled mashup into 5 images"
    
print "Reading additional message:"
f = open("evil4.jpg")
s = f.read()
print s
    