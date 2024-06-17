import random

chars = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
for i in range(10):
    chars.append(i)

v = ord("A")
for _ in range(26): 
    chars.append(chr(v))
    chars.append(chr(v).lower())
    v +=1

def generatePass():
    password = []
    for _ in range(10):
        password.append(str(random.choice(chars)))
    print(''.join(password)) 

generatePass() 
    





