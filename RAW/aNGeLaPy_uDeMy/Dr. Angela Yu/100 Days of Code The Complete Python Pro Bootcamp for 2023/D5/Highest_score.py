# 🚨 Don't change the code below 👇
# 78 65 89 86 55 91 64 89
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n]) #type: ignore
print(student_scores)
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
# print(max(student_scores))
highest_score = 0
for single_score in student_scores:
    if single_score > highest_score: #type: ignore
        highest_score = single_score
print(f"The highest score in the class is: {highest_score}")