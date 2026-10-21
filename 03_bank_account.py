class BankAccount:
    def __init__(self, person_name, funds):
        self.person_name = person_name
        self.funds = funds

    def deposit(self, cash):
        if cash > 0:
            self.funds = self.funds + cash
            print("Deposit successful.")
        else:
            print("Enter a positive amount.")

    def display(self):
        print("Account holder:", self.person_name)
        print("Balance:", self.funds)

bank_user = BankAccount("Mira", 1600)
bank_user.deposit(600)
bank_user.display()
