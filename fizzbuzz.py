''' A program that prints numbers from 1 to 100. For
multiples of three, print "Fizz" instead of the number
, and for the multiples of five, print "Buzz". . For numbers 
which are multiples of both three and five, print "FizzBuzz".
'''

for num in range(1, 100 + 1):

    if (num % 3 == 0) and (num % 5 == 0):
        print("FizzBuzz")
        continue
    if num % 3 == 0:
        print("Fizz")
        continue
    if num % 5 == 0:
        print("Buzz")
        continue

    print(num)