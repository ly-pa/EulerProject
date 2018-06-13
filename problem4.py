listA = []
listB = []

def palindrome(x):
    return (str(x)[::1] == str(x)[::-1])

# first we make a function to check if palindrome
# by converting to a string, going through 1 char
# at a time forwards and backwards and matching

for a in range(900, 999):
    for b in range (900, 999):
        listA.append(a * b)

# making the assumption we can start checking at 900 but as long as
# we get some value we know we didn't undershoot

for c in listA:
    if palindrome(c):
        listB.append(c)
        
print(listB[-1])
# last one added will be the largest