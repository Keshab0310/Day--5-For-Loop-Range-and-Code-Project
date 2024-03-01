fruits = ["Apple","Banana","Cherry"] #This is the list of items in fruits
for fruit in fruits:      #For loop  to iterate through each item in the list.
    print(fruit)
    print(fruit + " pie") #This will print  out the name of the fruit followed by "pie".


print("------------------------------------------------------------------------------------------")
student_height = [156, 178, 165, 171, 187]


total_height = 0
for height in student_height:
    total_height += height #Looping each height  value and adding it to the variable total_height
print(f"Total height of student = {total_height}")

number_of_students = 0
for student in  student_height:
    number_of_students += 1     #Looping and Adding one for every iteration so we get the correct count.
print(f"The number of students = {number_of_students}")

average_height = total_height / number_of_students
print(f"Average Height of all students = {average_height}")

