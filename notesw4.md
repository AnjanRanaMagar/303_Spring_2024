## Notes for Week4 

## Function

Few Notes for function assignment:

- In order to get the list of lowercase letter we use the code:
```
import string
sting.ascii_lowercase 
```
- We need to make sure we check for several condition before encoding or decoding the test by shift. It includes, wherether the character is alphabet or not? if the character shift index (> 25) then we circle back to index 0, etc.

Overall the function assignment is fun and easy.

## Class

## Challanges and Resolution

Challanges: My pytes ran into issue for the Saving Acccount and Checking Account. 

Original code:
```
class SavingsAccount(BankAccount):
    .... (super) inherientance
    
    def withdraw(self, amount):

        # check for sufficient balanc:
        if amount > self.balance:
            print("Insufficient funds in your account. Overdraft are not permitted in Saving Account.")
        # check if account is at least 180 days:
        if date.today() < self.creation_date + timedelta(days=180):
            print("The withdrawls are not permitted until the account has been active for at least for 180 days.")
        # if there is enough funds
        self.balance -= amount
        print(f'Withdrawl successful. New balance: ${self.balance:.2f}')
```
This code has issue. The code is correctly done and for the condution of not sufficient fund as well as date creation. However, the function is still moving forward with the withdraw. In real world, if you don't have money your account indicates that you should not be able towithdraw. So, solution was to use return function to exit out of the function if the condition were true for above scenario.

Soltion code:
```
class SavingsAccount(BankAccount):
    .... (super) inherientance
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient ....")
            return 

        if date.today() < self.creation_date + timedelta(days=180):
            print("The....")
            return
        self.balance -= amount
        print(..)

```
Furthermore, the <strong> return </strong>syntax was also used in the deposit function to handle deposit of negative amounts.

- Anjan and Roberta