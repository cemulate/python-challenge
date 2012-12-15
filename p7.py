import zipfile

path = "channel.zip"

z = zipfile.ZipFile(path)

def nextNothing(s):
    findStr = "nothing is "
    index = s.find(findStr)
    if index == -1:
        return None
    i1 = index+len(findStr)
    return s[i1:len(s)]

file = "90052"
ext = ".txt"
comments = []
while True:
    comments.append(z.getinfo(file+ext).comment)
    s = z.read(file+ext)
    print s
    file = nextNothing(s)
    if file is None:
        break
    
print "".join(comments)
    