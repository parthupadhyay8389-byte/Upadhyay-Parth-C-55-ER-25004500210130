class Person:
    def __init__(self, person_name):
        self.person_name = person_name

    def show_name(self):
        print("Name:", self.person_name)

class Student(Person):
    def show_course(self):
        print("Course: BCA")

learner = Student("Tina")
learner.show_name()
learner.show_course()
