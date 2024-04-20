import math
import time

def gcd_normal(a,b):

     while b != 0:

        a, b = b, a % b

     return a


def get_e (eul):

    e = 5

    while True:

        if gcd_normal(e,eul)==1:

            return e
        
        else:

            e += 1


def is_prime(a):
    
    
    if a <= 1:

        print("The number entered is not prime")
        raise ValueError("The number entered is not prime")

    elif a <= 3:

        print("The number entered is prime")

    elif a % 2 == 0 or a % 3 == 0:

        print("The number entered is not prime")
        raise ValueError("The number entered is not prime")

    else:

        b = 5 

        while b**2 <= a:

            if a % b == 0 or a % (b + 2) == 0:

                print("The number entered is not prime")
                
                raise ValueError("The number is not prime")

                return
            b+=6


        print("The no. entered is prime") 

bits = int(input("Will you use 8 or 16 bits? "))

while bits:

    if bits in [8,16]:

        break
    
    else:

        raise ValueError("Bits can be 8 or 16 only")

p = int(input("Enter the first prime number "))

is_prime(p)

q = int(input("Enter the second prime number "))

is_prime(q)

n = p*q

if n > 256 and bits == 8:
    
    print("n should be less than 256 since it's an 8-bit number")
    
    
    raise ValueError
elif n > 65536 and bits == 16:

    print("n should be less than 65536 since it's a 16-bit number")

    
    raise ValueError
elif n > 255 and bits == 16:

    print("You are using a 16-bit number")

eul = (p-1)*(q-1)

e = get_e(eul)

m = int(input(f"Enter the no. that neeads to be encrypted, make sure it is less than {n-2} "))

if m > n-2:
    print("The m shouldn't be greater than n ")
    raise ValueError(f"{m} is greater than {n-2}")
if m <= e:
    print("The m shouldn't be less than e ")
    raise ValueError(f"{m} is greater than {e}")
# eul = (p-1)*(q-1)

# def gcd_normal(a,b):

#      while b != 0:

#         a, b = b, a % b

#      return a
    
# def get_e (eul):

#     e = 7

#     while True:

#         if gcd_normal(e,eul)==1:

#             return e
        
#         else:

#             e += 1

# e = get_e(eul)

def extended_gcd(a,b):

    s1, s2, t1, t2 = 1, 0, 0, 1

    while b:

        q, a, b = a//b, b, a%b

        s1, s2 = s2, s1-q*s2

        t1, t2 = t2, t1-q*t2

    return a, s1, t1
start_time = time.perf_counter()
gcd, s, t = extended_gcd(e, eul)

d = s % eul

end_time = time.perf_counter()

run_time = end_time - start_time

print(f"The public key is is {n,e}")

print(f"The private key is is {n,d}")

c = pow(m, e, n)

M = pow(c, d, n)

print(f"The original number is {m}\nThe encrypted message is {c}\nThe decrypted message is {M}")

print(f"The runtime of the factorization function is {run_time}")