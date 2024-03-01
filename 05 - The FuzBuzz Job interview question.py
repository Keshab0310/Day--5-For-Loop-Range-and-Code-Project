#The interviewer asked the person to print the solution of FizzBuzz game
#The rules are as follows:
#1. The number divided by 3 is printed then print  "Fizz".
#2. If the number is divisible by 5 is printed then  print "Buzz" instead.
#3. For numbers which are multiples of both 3 and 5, print "FizzBuzz".
#4. Print all other numbers in their original form.
#Write a program that prints this for numbers from 1 to 100.
#Here is the best solution
num = 100
for i in range (1, num + 1):
    if i % 3 == 0 and i  % 5 != 0:
        print("Fizz")
    elif i % 5 == 0 and i % 3 != 0:
        print ("Buzz")
    elif  i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    else:
        print(i)