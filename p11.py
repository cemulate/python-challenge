import itertools

def next_morris(ns):
	s = [str(len(list(group))) + digit for digit, group in itertools.groupby(ns)]
	return ''.join(s)

def morris(n):
	num = '1'
	yield num
	for i in range(1, n):
		num = next_morris(num)
		yield num
	
print "Generating morris to 30th number..."
a = list(morris(31))
for x in a:
	print x
	print "-----\n"

print "Length of the 30th element of the morris sequence is:"
print len(a[30])

	