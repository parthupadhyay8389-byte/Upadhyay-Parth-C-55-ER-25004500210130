class Student:
    def display(self):
        print("Name:", self.person_name)
        print("Roll number:", self.roll_id)

learner = Student()
learner.person_name = "Karan"
learner.roll_id = 108
learner.display()
