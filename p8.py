from PIL import Image

im = Image.open("oxygen.png")

im = im.crop((1,43,608,44))

data = im.getdata()
#data = list(set(data))
vals = [x[0] for x in data]
#vals.sort()

new = []
for i in range(0, len(vals), 7):
    new.append(vals[i])

str = [chr(x) for x in new]
str = "".join(str)

print str

i = str.find("[")
str = str[i+1:len(str)-1]

print str

newStr = [chr(int(x)) for x in str.split(", ")]
print newStr
print "".join(newStr)