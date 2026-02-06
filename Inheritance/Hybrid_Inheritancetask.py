# Base Class
class Person:
    def __init__(self, name, **kwargs):
        super().__init__(**kwargs)
        self.name = name

    def display_person(self):
        print("Name:", self.name)


# Derived Class 1
class Student(Person):
    def __init__(self, student_id, **kwargs):
        super().__init__(**kwargs)
        self.student_id = student_id

    def display_student(self):
        print("Student ID:", self.student_id)


# Derived Class 2
class SportsPlayer(Person):
    def __init__(self, sport_name, **kwargs):
        super().__init__(**kwargs)
        self.sport_name = sport_name

    def display_sports_player(self):
        print("Sport Name:", self.sport_name)


# Hybrid Class
class CollegeStudent(Student, SportsPlayer):
    def __init__(self, name, student_id, sport_name, college_name):
        super().__init__(name=name, student_id=student_id, sport_name=sport_name)
        self.college_name = college_name

    def display_college_student(self):
        print("College Name:", self.college_name)


# Creating Object
cs = CollegeStudent("Riya", "CSE123", "Badminton", "XYZ Engineering College")

# Display All Details
cs.display_person()
cs.display_student()
cs.display_sports_player()
cs.display_college_student()
