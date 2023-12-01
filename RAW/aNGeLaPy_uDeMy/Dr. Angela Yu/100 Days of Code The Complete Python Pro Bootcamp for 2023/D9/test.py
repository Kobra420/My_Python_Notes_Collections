# # Create a nested dictionary that stores information about students. 
# # Each student has a name, age, and a dictionary of subjects they are taking, with corresponding grades.

# students = {}

# def add_student(name, age):
#     """Adds a student to the dictionary"""
#     students[name] = {'age': age, 'subjects': {}}
    
# def add_subject(name, subject, grade):
#     """Adds a subject to a student"""
#     students[name]['subjects'][subject] = grade
    
# # Example usage:

# add_student('Alice', 20)

# add_subject('Alice', 'Math', 85)
# add_subject('Alice', 'Science', 90)

# print(students)
# print(students["Alice"]["subjects"]["Science"])

# Output:
student = {
    'Alice': 
    {'age': 20, 
     'subjects': 
        {
             'Math': 85,
             'Science': 90,
             'English': 95,
             'History': 90,
             'Geography': 95,
             'Art': 95,
             'Music': 90
        }
    }
    ,
    'Bob': 
    {'age': 21, 
     'subjects': 
        {
             'Math': 75,
             'Science': 80,
             'English': 90,
             'History': 80,
             'Geography': 85,
             'Art': 80,
             'Music': 85,
        }
    }
    ,
    'Charlie': 
    {'age': 22, 
     'subjects': 
        {
             'Math': 65,
             'Science': 70,
             'English': 75,
             'History': 70,
             'Geography': 75,
             'Art': 70,
             'Music': 75
        }
    }
    ,
    'David': 
    {'age': 23, 
     'subjects': 
        {
             'Math': 55,
             'Science': 60,
             'English': 65,
             'History': 60,
             'Geography': 65,
             'Art': 60,
             'Music': 65
        }
    }
    ,}

print(student['David']['subjects'])