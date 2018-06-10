# Problem 2 - Even Fibonacci numbers

# By considering the terms in the Fibonacci sequence
# whose values do not exceed four million, find the
# sum of the even-valued terms.

F = [1, 1] 					     # we create a list with seed values which for the Fibonacci sequence are 0,1 or 1,1
prod = 0					     # variable where we will store our Fibonacci numbers

while prod < 4000000:                        # Halts once the Fibonacci product hits 4 million
    prod = F[-1] + F[-2]                     # prod is the sum of the previous 2 terms in the sequence
    F.append(prod)			                     # adds prod to the list of Fibonacci numbers we are bulding in F

print(sum(num for num in F if num % 2 == 0))	# this prints the sum of the even terms in F