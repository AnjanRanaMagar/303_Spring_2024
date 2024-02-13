'''
Pair Exercise: Anjan and Roberta
Date: Feb 11, 2024
Functions and Classes
'''

# imported library
import string

# Creating functions encode and decode! These functions are for the Caesar_Cipher crypographic schema

def encode(input_text="a", shift=3):
    '''
    input_text: the text to be encrypted
    shift: the number of places to shift along the alphabet to where the replacing letter resides.

    Few things to think about: 
    1. Check to see if character in input text are indeed only lowercase letter. If yes, shift and if not
    just add them as they are.
    2. Check if shifting the index will cause the index to be more than 25 ( since 15 is the last index of lowercase letter). Is so, 
    we need to go back to 0 after index 25. To do so, just substract 26 from index (i.e 26 letters in alphabet)
    '''
    
    # get all the lowercase letters from string methods.
    lower_letters = list(string.ascii_lowercase) 
    enCod = '' 
    for i in input_text.lower(): # incase user inputs uppercase letter 
        if i in lower_letters: 
            index = lower_letters.index(i)+shift 
            if index > 25:
                index = index - 26
            enCod += lower_letters[index]
        else:
            enCod += i
            
    return (lower_letters,enCod)


def decode(input_text="d",shift=3):
    '''
    input_text: the text to be decrypted
    shift: the number of places to shift along the alphabet to where the replacing letter resides.
    
    Few things to think about similar to encode function: 
    1. Check to see if character in input text are indeed only lowercase letter. If yes, shift and if not
    just add them as they are.
    2. Check if index are correctly assignged in special case such as when index is 0. the shift will make it say(-4) with shift 4. In this case
    we don't need to worry since -4 gets what we need.
    '''
    # get all the lowercase letters from string methods.
    lower_letters = list(string.ascii_lowercase)
    deCod = ''
    for i in input_text.lower(): 
        if i in lower_letters:
            index = lower_letters.index(i) - shift
            deCod += lower_letters[index]
        else:
            deCod += i
    return (deCod)



# import necessary library for class
from datetime import date, timedelta

class BankAccount:
    def __init__(self, name: str = "Rainy", id: str = "1234", creation_date: date=date.today(), balance: float=10.0):
        '''
        The BankAccount class must obey the following rules:
        - the date of creation may be a past date or today, but cannot be a future date.
        - A date supplied with a future creation date must raise an exception of class Exception.
        - negative deposit amounts are not allowed
        - withdrawal and deposit actions should display the resulting account balance
        '''
        self.name = name 
        self.id = id
        self.balance = balance
        self.creation_date = creation_date
        # check if the date is in future
        if self.creation_date > date.today():
            raise Exception("The account creation date cannot be in the future.")
        
    def deposit(self, amount):
        # negative deposits are not allowed. if negative deposits, print message and exit.
        if amount < 0:
            print("Negative deposits not allowed.")
            return
        self.balance += amount
        print(f'Thank you {self.name}. You deposit of ${amount} is successful. New balance: ${self.balance:.2f}')

    def withdraw(self,amount):
        # 1. when you withdraw more money that you have, say (200) when you have 100.
        # in this case, check acount to see if i have enough amount to withdraw.
        # 2. check if the amount requested is a valid amount
        if amount < 0:
            print("Please enter valid amount.")
        if self.balance < amount:
            print("You don't have sufficient fund to withdraw.")
        self.balance = self.balance - amount
        print(f'New balance: ${self.balance:.2f}')

    def view_balance(self):
        print("Your current balance is ${self.balance}.")


class SavingsAccount(BankAccount):

    def __init__(self, name: str = "Rainy", id: str = "1234", creation_date: date = date.today(), balance: float = 10):
        super().__init__(name, id, creation_date, balance)
    
    def withdraw(self, amount):
        ''' 
        If the date creation is less than 180 days the function raise exception. Else, 
        it passes that value(amount) to parent withdraw method.
        '''
        # check for sufficient balance:
        if amount > self.balance or self.balance < 0:
            print("Insufficient funds in your account. Overdraft are not permitted in Saving Account.")
            return 
        # check if account is at least 180 days:
        if date.today() < self.creation_date + timedelta(days=180):
            print("The withdrawls are not permitted until the account has been active for at least for 180 days.")
            return
        
        # if there is enough funds
        self.balance -= amount
        print(f'Withdrawl successful. New balance: ${self.balance:.2f}')
  

class CheckingAccount(BankAccount):
    def __init__(self, name: str = "Rainy", id: str = "1234", creation_date: date = date.today(), balance: float = 10):
        # inheritence script
        super().__init__(name, id, creation_date, balance)
    
    def withdraw(self, amount):
        ''' Unlike saving account, in checking account, overdraft is permitted.
            However, the account will incur $30 fee'''
        
        #check if withdraw will results in overdraft?
        if amount > self.balance:
            # apply overdraft fee
            self.balance -= 30
            print(f'Overdraft fee of $30 applied to your account.')
        
        # if not overdraft just withdraw
        self.balance -= amount
        print(f'Withdrawl successful. New balance: ${self.balance:.2f}')
        





