# # Create a nested dictionary that stores information about students. 
# # Each student has a name, age, and a dictionary of subjects they are taking, with corresponding grades.
# # Output:
# student = {
#     'Alice': 
#     {'age': 20, 
#      'subjects': 
#         {
#              'Math': 85,
#              'Science': 90,
#              'English': 95,
#              'History': 90,
#              'Geography': 95,
#              'Art': 95,
#              'Music': 90
#         }
#     }
#     ,
#     'Bob': 
#     {'age': 21, 
#      'subjects': 
#         {
#              'Math': 75,
#              'Science': 80,
#              'English': 90,
#              'History': 80,
#              'Geography': 85,
#              'Art': 80,
#              'Music': 85,
#         }
#     }
#     ,
#     'Charlie': 
#     {'age': 22, 
#      'subjects': 
#         {
#              'Math': 65,
#              'Science': 70,
#              'English': 75,
#              'History': 70,
#              'Geography': 75,
#              'Art': 70,
#              'Music': 75
#         }
#     }
#     ,
#     'David': 
#     {'age': 23, 
#      'subjects': 
#         {
#              'Math': 55,
#              'Science': 60,
#              'English': 65,
#              'History': 60,
#              'Geography': 65,
#              'Art': 60,
#              'Music': 65
#         }
#     }
#     ,}

students = {}

def add_student(name, age):
    """Adds a student to the dictionary"""
    students[name] = {'age': age, 'subjects': {}}
    
def add_subject(name, subject, grade):
    """Adds a subject to a student"""
    students[name]['subjects'][subject] = grade
    
# Example usage:

add_student('Alice', 20)
add_subject('Alice', 'Math', 85)
add_subject('Alice', 'Science', 90)
add_subject('Alice', 'English', 95)
add_subject('Alice', 'History', 90)
add_subject('Alice', 'Geography', 95)
add_subject('Alice', 'Art', 95)
add_subject('Alice', 'Music', 90)

add_student('Bob', 21)
add_subject('Bob', 'Math', 75)
add_subject('Bob', 'Science', 80)
add_subject('Bob', 'English', 90)
add_subject('Bob', 'History', 80)
add_subject('Bob', 'Geography', 85)
add_subject('Bob', 'Art', 80)
add_subject('Bob', 'Music', 85)

add_student('Charlie', 22)
add_subject('Charlie', 'Math', 65)
add_subject('Charlie', 'Science', 70)
add_subject('Charlie', 'English', 75)
add_subject('Charlie', 'History', 70)
add_subject('Charlie', 'Geography', 75)
add_subject('Charlie', 'Art', 70)
add_subject('Charlie', 'Music', 75)

add_student('David', 23)
add_subject('David', 'Math', 55)
add_subject('David', 'Science', 60)
add_subject('David', 'English', 65)
add_subject('David', 'History', 60)
add_subject('David', 'Geography', 65)
add_subject('David', 'Art', 60)
add_subject('David', 'Music', 65)

# print(students)
# print(students["Alice"]["subjects"]["Science"])



print(students['David']['subjects'])