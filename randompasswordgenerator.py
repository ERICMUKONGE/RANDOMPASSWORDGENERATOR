import random
import string

def getlowercase():
    return random.choice(string.ascii_lowercase)

def getuppercase():
    return random.choice(string.ascii_uppercase)

def getsymbol():
    syms=['!','@','$','&','.']
    return str(random.choice(syms))

def getnum():
    return str(random.randint(1,20))

defs = [getlowercase,getuppercase,getsymbol,getnum]

length = random.randint(15,20)

pw = []

for x in range(length):
    index = random.randint(0,3)
    pw.append(defs[index]())

finishedpw = "".join(pw)

print(finishedpw)

