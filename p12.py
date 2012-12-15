from PIL import Image

#im = Image.open("C:/Users/Chase/Desktop/pythonChallenge/cave.jpg")
im = Image.open("cave.jpg")
print im

data = im.getdata()
print len(data)

print "Extracting every other pixel"

newData = list(data)[1::2]
print len(newData)

im2 = Image.new("RGB", (640,480))
print im2

im2.putdata(newData)

im2.save("cave_message.jpg")