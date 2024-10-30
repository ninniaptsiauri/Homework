from multipledispatch import dispatch


class Person:
    def __init__(self, name, deposit=1000, loan=0):
        self.name = name
        self.deposit = deposit
        self.loan = loan

    def __str__(self):
        return f"Name: {self.name}, Deposit: {self.deposit}, Loan: {self.loan}"
    

class House:
    def __init__(self, ID, price, owner: Person):
        self.ID = ID
        self.price = price
        self.owner = owner
        self.status = 'For sale'
        

    @dispatch(Person)
    def sell(self, buyer):
        self.owner.deposit += self.price
        self.owner = buyer
        self.status = 'Soled'
        print(f"The house is sold. New owner is {buyer.name}.")

 
    @dispatch(Person, int)
    def sell(self, buyer, loan_amount):
        if loan_amount > 0:
            buyer.loan += loan_amount
            buyer.deposit -= loan_amount
            self.owner.deposit += self.price
            self.owner = buyer
            self.status = 'Sold with a loan.'
            print(f"The house is sold with a loan. New owner is {buyer.name}, amount of loan is {loan_amount}.")
        
        else:
            print("Loan amount must be greater than 0.")


owner = Person("John")
buyer = Person('Kate')
house = House("12345", 50000, owner)

print(owner)
print(buyer)
print(f"House status is: {house.status}")

house.sell(buyer)
print(f"House status is: {house.status}")
print(f"Information about new owner: {house.owner}")
print(f"Information about old owner: {owner}")


## Sell with loan ###
# house.sell(buyer, 20000)
# print(f"House status is: {house.status}")
# print(f"Old owner's deposit is: {owner.deposit}.")
# print(f"New owner's loan is: {buyer.loan}.")
