import math
p = int(input("Enter the first prime number"))

q = int(input("Enter the second prime number"))

n = p*q

eul = (p-1)(q-1)

def gcd(a,b):

    while b != 0:
        
        a =  b

        b = a % b

    return a
    
def get_e (eul):

    e = 2

    while True:

        if gcd(e,eul):

            return e
        
        else:

            e += 1
        


