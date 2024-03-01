#for loop with rrange
total = 0
for number in range(1, 101): #Range  is exclusive of the end value so we use  101 instead of 100. to get the value from 1-100
    total += number #here total = 0 and  it is added to itself for each iteration.
print(f"The sum of the numbers is  {total}")
