class Employee:
    def __init__(self, person_name, monthly_pay):
        self.person_name = person_name
        self.monthly_pay = monthly_pay

    def display(self):
        print("Name:", self.person_name)
        print("Salary:", self.monthly_pay)

staff_one = Employee("Dev", 22000)
staff_two = Employee("Anjali", 26000)
staff_one.display()
staff_two.display()
