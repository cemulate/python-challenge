from PIL import Image

im = Image.open("mozart.gif")
print im

data = im.getdata()
import itertools

newData = []

def findEndpoint(row):
    test = lambda i, data: data[i:i+5] == [195]*5
    results = [test(i, row) for i in range(len(row))]
    return results.index(True)

data = list(data)
data = [data[i:i+640] for i in range(0, 640*480,640)]
for n in range(len(data)):
    row = data[n]
    i = findEndpoint(row)
    print ("Row " + str(n), "Position " + str(i))
    newData.extend(row[i:] + row[:i])
    
im.putdata(newData)
im.save("mozart_message.gif")
print "Wrote straightened image"