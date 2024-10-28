# Bank Account deposit and withdrawal

class BankAccount:
    def __init__(self, account_number, account_holder, balance) -> None:
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
            print(f"Deposit of {amount}$ was successful. Your balance is {self.balance:.2f}$")
        
        else:
            print("Invalid deposit amount. Please enter a positive value.")



    def withdrawal(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"{amount}$ was successfully withdrawn. Your balance is {self.balance:.2f}$")
            else:
                print("Your balance is not enough for withdrawal.")

        else:
            print("Invalid withdrawal amount. Please enter a positive value.")



account1 = BankAccount("243294380", "Anna Miles", 1000)
account2 = BankAccount("750384379", "Tom Hanks", 2000)

account1.deposit(500)
account1.withdrawal(300)

account2.deposit(1000)
account2.withdrawal(1500)






# Student info an courses

class Student:
    def __init__(self, name, student_id, courses=None):
        self.name = name
        self.student_id = student_id
        self.courses = courses if courses is not None else []

    def choose_course(self, course_name):
        if course_name not in self.courses:
            self.courses.append(course_name)
        
        else:
            print(f"{self.name} has already chosen {course_name}")


    def student_info(self):
        print(f"Student Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print("Courses:")
        if self.courses:
            for course in self.courses:
                print(f"{course}")
        
        else:
            print("No courses chosen.")


student1 = Student("John Doe", "S12345", ['Art', 'History'])
student2 = Student("Jane Smith", "S67890", ['Python', 'English'])

student1.choose_course("Math")
student1.choose_course("Science")
student1.student_info()

student2.choose_course("History")
student2.student_info()


