print "We've apologized..."
print "Investigating mybroken.zip..."

import hashlib, binascii, sys
broken = open("maze_dump/mybroken.zip", 'rb').read()

correct = 'bbb8b499a0eef99b52c7f13f4e78c24b'
correct = binascii.a2b_hex(correct)
print "Correct md5 checksum: ", binascii.b2a_hex(correct)

b = hashlib.md5(broken).digest()
print "Actual zip checksum: ", binascii.b2a_hex(b)

print "\nChanging each byte until checksum is correct"

test = []
ival = len(broken)//20
sys.stdout.write("Mending file")
def fix():
	for i in range(len(broken)):
		if i % ival is 0:
			sys.stdout.write(" .")
		for char in range(256):
			test = broken[:i] + chr(char) + broken[i+1:]
			md5 = hashlib.md5(test).digest()
			if md5 == correct:
				sys.stdout.write("\n")
				print "md5 matches! Saving corrected zip"
				open("maze_dump/corrected.zip", 'wb').write(test)
				return
			
fix()