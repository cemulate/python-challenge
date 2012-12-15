import this

print "\nRot13 message:"
string = 'va gur snpr bs jung?'
print string, "\n"

string = string.encode("rot13")
print string

print "\nambiguity"

print "Apologizing to Leopold..."

#import smtplib
#server = smtplib.SMTP('smtp.gmail.com:587')
#server.starttls()
#server.login("c.ed.mead@gmail.com", raw_input("Enter password: "))
#server.sendmail("c.ed.mead@gmail.com", ["leopold.moz@pythonchallenge.com"], "sorry")
#server.quit()