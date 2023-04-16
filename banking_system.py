class Bank:
    def __init__(self):
        self.client_details_list = []
        self.logged_in = False
        #self.cash = 100
        self.Transfer_cash = False

    def register(self, name, ph, username, password, cash):
        condition = False
        if len(str(ph)) > 10 or len(str(ph)) < 10:
            print("invalid phone number")
            condition = False

        if len(password) < 5 or len(password) > 18:
            print("Invalid password")
            condition = False

        if condition:
            print("Account created")
            self.client_details_list = [name, ph, username, password, cash]
            with open(f'{name}.txt', "w") as f:
                for details in self.client_details_list:
                    f.write(str(details) + "\n")

    def login(self, name, ph, username, password):
        with open(f'{name}.txt', 'r') as f:
            details = f.read()
            self.client_details_list = details.split("\n")
            if str(ph) in str(self.client_details_list):
                if str(password) in str(self.client_details_list):
                    if str(username) in str(self.client_details_list):
                        self.logged_in = True

            if self.logged_in:
                print(f'{name} logged in')
                self.cash = self.client_details_list[4]
            else:
                print("Wrong Details")

    def add_cash(self, amount):
        if amount > 0:
            self.cash += amount
            with open(f'{name}.txt', 'r') as f:
                details = f.read()
                self.client_details_list = details.split("\n")

            with open(f'{name}.txt', "w") as f:
                f.write(details.replace(str(self.client_details_list[4]), str(self.cash)))

            print("Amount added successfully")

        else:
            print("Enter correct value of amount")

    def Transfer_cash(self, amount, name, ph):
        with open(f'{name}.txt', 'r') as f:
            details = f.read()
            self.client_details_list = details.split("\n")
            if str(ph) in self.client_details_list:
                self.Transfer_cash = True

        if self.Transfer_cash:
            total_cash = int(self.client_details_list[4]) + amount
            left_cash = self.cash - amount
            with open(f'{name}.txt', "w") as f:
                f.write(details.replace(str(self.client_details_list[4]), str(total_cash)))

            with open(f'{self.name}.txt', "w") as f:
                f.write(details.replace(str(self.client_details_list[4]), str(left_cash)))

            print("Amount Transfer Successfully to", name, "-", ph)


if __name__ == "__main__":
    Bank_Obj = Bank()
    print("Welcome to my bank")
    print("1.login")
    print("2.Create new account")
    user = int(input("Make Decision"))
    if user == 1:
        print("logging in ")
        name = input("Enter name :")
        ph = int(input("Enter ph number :"))
        username = input("Enter Username :")
        password = input("Enter Password")
        Bank_Obj.register(name, ph, username, password)
        while True:
            if Bank_Obj.logged_in:
                print("1, Add Amount")
                print("2. check balance :")
                print("3. Transfer Amount :")
                print("4, Edit Profile :")
                print("5, Logout")
                login_user = int(input())
                if login_user == 1:
                    print("Balance :", Bank_Obj.cash)
                    amount = int(input("Enter amount :"))
                    Bank_Obj.add_cash(amount)
                    print("\n1.back menu")
                    print("2. Logout")
                    choose = int(input())
                    if choose == 1:
                        continue
                    if choose == 2:
                        break
                if login_user == 2:
                    print("balance :", Bank_Obj.cash)
                    choose = int(input())
                    if choose == 1:
                        continue
                    if choose == 2:
                        break

    if user == 2:
        print("create new account")
        name = input("Enter name :")
        ph = int(input("Enter ph number :"))
        username = input("Enter Username :")
        password = input("Enter Password")
        cash = int(input("Add Cash :"))
        Bank_Obj.register(name, ph, username, password, cash)
