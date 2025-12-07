
# PART 1 -> The Student Class

# 1st: Creating a class named Student with its related attributes


class Student:
    def __init__(self, name:str, student_id:str, courses_and_grades:dict):
        self.name = name
        self.student_id = student_id
        self.courses_and_grades = courses_and_grades

# 2nd: Implement the functions

    def get_average_grade(self):
        grades = self.courses_and_grades.values()
        return sum(grades) / len(grades) # Gets all the grades from the dictionary using .values() and compute the avg.
    
    def add_course_and_grade(self, course_name, grade):
        self.courses_and_grades[course_name] = grade # Adds a new course + grade to the student’s dictionary

    def get_honors_courses(self, threshold=90):
        honors = []
        for course, grade in self.courses_and_grades.items():
            if grade >= threshold:
                honors.append(course)
        return honors # Goes through all courses and grades and keeps only the ones ≥ threshold (90). It returns a list of course names, not grades.
    
    def get_unique_grades(self):
        return set(self.courses_and_grades.values()) # Gets all grades from the dictionary and converts them to a set, which removes duplicates.


# TEST the functions

courses= {'Math': 85, 'Science': 92, 'History': 78}
s1 = Student('Luca', 'S01', courses)

print("Average grade", s1.get_average_grade())
s1.add_course_and_grade("Sociology", 92)
print("Honors:", s1.get_honors_courses())
print("Unique grades:", s1.get_unique_grades())


# PART 2 -> The Manager Logic

# 1st: Initialize Data 

class Student:
    def __init__(self, name:str, student_id:str, courses_and_grades):

        if isinstance(courses_and_grades, dict):
            self.courses_and_grades = courses_and_grades
        else:
            self.courses_and_grades = dict(courses_and_grades) # This change in the __init__ allows to handle either a dict or tuple/list   
        self.name = name
        self.student_id = student_id  
        
    def get_average_grade(self):
        grades = self.courses_and_grades.values()
        return sum(grades) / len(grades) # Gets all the grades from the dictionary using .values() and compute the avg.
    
    def add_course_and_grade(self, course_name, grade):
        self.courses_and_grades[course_name] = grade # Adds a new course + grade to the student’s dictionary

    def get_honors_courses(self, threshold=90):
        honors = []
        for course, grade in self.courses_and_grades.items():
            if grade >= threshold:
                honors.append(course)
        return honors # Goes through all courses and grades and keeps only the ones ≥ threshold (90). It returns a list of course names, not grades.
 
# Create all_student list

all_students = []

s1 = Student("Luca", "S01", {"Math": 85, "History": 97})
s2 = Student("Maria", "S02", {"Sociology": 92, "Chemistry": 59})

# Create a Tuple pairs of course
tuple_courses = [("Art", 95), ("PE", 88)]
s3 = Student("Karl", "S03", tuple_courses)

# Add them to the all_student list
all_students.append(s1)
all_students.append(s2)
all_students.append(s3)


# !! I was not sure if I should rewrite the whole class + functions code (as I did) or just add the change (in this case, the part to allow Tuples) in the original code.

# 2nd: Apply logic

for student in all_students:
    avg = student.get_average_grade()

    if avg > 80:
        honors = student.get_honors_courses()
        print(student.name, "has an excellent average of", avg, "and the following honor courses:", honors)
    else:
        student.add_course_and_grade("Study skills", 100)
        print(student.name, "had an average of", avg, "so 'Study Skills' was added with a grade of 100.")


