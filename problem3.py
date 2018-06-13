# Largest prime factor
# Problem 3

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

import math

n = 600851475143 
pfList = []

def checkPrime(num):
    for a in range(2, int(math.sqrt(num)) + 1):
        if num % a == 0:
            return False
    return True

# first we make a function to check if number is prime
# then apply it to all factors of n to sort out prime factors

for b in range(2, int(math.sqrt(n)) + 1):
    if n % b == 0:
        if checkPrime(b):
            pfList.append(int(b))

#then append those to a list

print(pfList[-1])
#largest prime factor will be the last appended to the list