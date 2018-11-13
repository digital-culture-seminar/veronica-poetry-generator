print ("Dark Cloud")
print ("\n")

# Strings in single quotes.
s1 = 'When shadows hang overhead,'

# Double quotes are the same.  You just have to end with the same character
# you started with, and you don't have to escape the other one.
s2 = "darkness falls."

# You can create multi-line strings with triple quotes (triple double quotes
# work, too.)  The newlines stay in the string.
s3 = "A heaviness slows his breathing and his body,"
s4 = "And his mind screams obstructive, cynical thoughts."
s5 = "Attempting to reject the fateful calls,"
s6 = "He fill his head with reminders of those he holds dear."
s7 = "Sadness engulfs deep within his soul."
s8 = "Latching onto him and not letting him go."

list = [s1, s2, s3, s4, s5, s6, s7, s8]

with open("poem.md", "w") as p:
    for i in range(0,8):
        poem = list[i]
        print poem
        p.write(poem)
        p.write("\n")

#with open ("poem.md","w") as p:
#    p.write("## Dark Cloud")
#    p.write("```")
#    p.write(poem)
#    p.write("```")
#    p.write("\n")
#    p.write(poem)
#    p.write("\n")
#    p.write("```")
#    p.write(poem)
#    p.write("\n")
#    p.write("```")

    
#with open("poem.md","w") as p:
#    p.write("""
## Dark Cloud
#```
#{poem}
#```
#""".format(poem=poem))
        
#mylist = []
#for i in range(0,10):
#   mylist.append("dark cloud" + str(i))
#   print mylist
#   print mylist[i]

    
