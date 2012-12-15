s = open("yankeedoodle.csv", 'rb').read()
s = s.replace(",", "")

#lines = s.split("\n")
#lines = list(l for l in lines if len(l) > 0)
#lines = list(list(float(x) for x in s.split(" ")) for s in lines)

s = s.replace("\n", " ")
strVals = s.split(" ")
strVals = list(x for x in strVals if len(x) > 0)

#lines = list(list(float(x) for x in lines[i].split(" ")) for i in range(len(lines)))
#for i in range(len(lines)):
#	print list(float(x) for x in lines[i].split(" "))

#vals = []
#for x in lines: vals.extend(float(x))

vals = list(float(x) for x in strVals)

#vals = list(int(v*100000) for v in vals)
#print vals[0:5]

def factor(n):
	factors = []
	for x in range(1, int(n**0.5)+1):
		for y in range(1, n+1):
			if x*y == n:
				factors.extend((x, y))
	factors = list(set(factors))
	factors.sort()
	return factors

f = factor(len(vals))
print f
#f = f[1:3]
#print list(vals[i] for i in f)

w, h = f[1:3]
print w, h
#rows = list(vals[i:i+w] for i in range(0, len(vals), w))

from PIL import Image
im = Image.new("F", (w, h), 0)

im.putdata(vals)
im = im.rotate(270)
im = im.transpose(Image.FLIP_LEFT_RIGHT)
im.save("csv_test.tiff")

def formula(x, i):
	#print x, i
	return str(x[i])[5] + str(x[i+1])[5] + str(x[i+2])[6]

threes = list(strVals[i:i+3] for i in range(0, len(strVals), 3) if not i+3 > len(strVals))
answer = list(formula(threes[i], 0) for i in range(len(threes)))
print ''.join(chr(int(x)) for x in answer)