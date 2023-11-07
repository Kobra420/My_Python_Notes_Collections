# Dr. Lue's codes
# 154 123 156 172 182 192
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights with single space in between ").split()
for n in range(0, len(student_heights)):
   student_heights[n] = int(student_heights[n]) # type: ignore 
# 🚨 Don't change the code above 👆


##Write your code below this row 👇
total_height = 0
for height in student_heights:
    total_height = total_height + height# type: ignore
    # print(total_height)
number_of_students = 0
for student in student_heights:
    number_of_students += 1
# print(number_of_students)
average_height = total_height / number_of_students
print(f"Average Height : {round(average_height, 2)}")

# #usind sum and len only
# total_height = sum(student_heights) # type: ignore
# number_of_students = len(student_heights)
# avarage_height = total_height/number_of_students
# print(round(average_height,2))
