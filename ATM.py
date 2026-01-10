class Atm:
    def __init__(self):
        #Encapsulation
        self.__pin=""
        self.__balance=0

        self.menu()

    def menu(self):
        while True:
            user_input=input("""
Hello how would you like to proceed?
1.Enter 1 to create pin
2.Enter 2 to  deposit
3.Enter 3 to withdraw
4.Enter 4 to check balance
5.Enter 5 to exit
""")
            if user_input=="1":
                self.create_pin()
            elif user_input=="2":
                self.deposit()
            elif user_input=="3":
                self.withdraw()
            elif user_input=="4":
                self.check_balance()
            elif user_input=="5":
                print("Thank you")
                break
            else:
                print("Enter valid option.")        
    def create_pin(self):
        self.__pin=input("Enter your 6 digit pin.")
        print("Pin set successfully")
    def deposit(self):
        temp=input("Enter your pin")
        if temp==self.__pin:
            amount=int(input("Enter the amount"))
            self.__balance=self.__balance+amount
            print("deposit successfully")
        else:
            print("Invlid pin")
    def withdraw(self):
        temp=input("Enter your pin")
        if temp==self.__pin:
            amount=int(input("Enter the amount"))
            if amount<self.__balance:
                self.__balance=self.__balance-amount
            else:
                print("you don't have enough fund")
        else:
            print("Invlid pin")
    def check_balance(self):
        pin=input("Enter your pin:")
        if pin==self.__pin:
            print("Your current balance is:",self.__balance)
        else:
            print("Invalid pin")
sbi=Atm()
