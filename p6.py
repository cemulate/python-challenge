import pickle, sys

source = "banner.p"

thing = pickle.load(open(source))

print "Pickle data structure:"
for x in thing:
	print x
	print "\n"
	
print "Intepreted banner:"

for x in thing:
	for y in x:
		sys.stdout.write(y[0]*y[1])
	sys.stdout.write("\n")