target = int(100)
even_sum = 0
for number in range (2,  target+1, 2):
    even_sum += number
print(even_sum)
#or below code is used if we can't understand the upper code

new_sum =0
for num in range (1,target+1):
    if num % 2 == 0:
        new_sum+=num
print(f"The sum of all even numbers from 1 to 100 is {new_sum}")

