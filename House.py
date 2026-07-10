

class BlackJack:
    amount = 5000

    def __init__(self, balance=0):
        self.__balance = balance # private attribute so user can't change the balance

    # function for money to be deposited into the balance     
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New Balance = {self.__balance}")
        else:
            print("Deposit amount must be positive.") # error expection if deposit less than 0
    
    # function for money to be withdrawn  from the balance 
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount 
            print(f"Withdrew {amount}. New Balance = {self.__balance}")
        elif amount > self.__balance: 
            print("Insufficient balance.")
        else:
            print("Withdrawl amount must be positive.")
    
    def check_balance(self):
        print(f"House Account Balance = {self.__balance}")