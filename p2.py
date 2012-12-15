s = "map"

alpha = "abcdefghijklmnopqrstuvwxyzab"

def decodeCharacter(c):
    if not (c.isalpha()):
        return c
    i = alpha.find(c)
    return alpha[i+2]
    
translation = [decodeCharacter(c) for c in s]

print "Translation of string:"
print s + "\n"
print ''.join(translation)