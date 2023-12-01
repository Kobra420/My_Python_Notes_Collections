# Create a nested dictionary that stores information about students. 
# Each student has a name, age, and a dictionary of subjects they are taking, with corresponding grades.

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

print(students)
print(students["Alice"]["subjects"]["Science"])

# Output:
{'Alice': 
    {'age': 20, 
     'subjects': 
         {'Math': 85, 'Science': 90}
         }
    }

