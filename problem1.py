# Problem 1 - multiples of 3 and 5

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

x = 0 # this variable will be the sum of our multiples

for num in range(3,1000):   # we check the range 3 to 1000 as we know 1 and 2 are not multiples of 3 or 5
    if num % 3 == 0 or num % 5 == 0:	# if the numbers in the range divided by 3 or 5 leave a remainder of 0, we know they are multiples
        x += num						# so we add them to our variable x

print(x)								# finally we print that variable to return our answer