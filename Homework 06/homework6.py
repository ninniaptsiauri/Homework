# number 1

word_dict = {}
txt = input("Please enter a text: ")
words = txt.split()
for word in words:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1
print(word_dict)



# number 2

import operator as op
num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter a number: "))
operation = input("Choose an operator (+, -, *, /, //, **, %): ")
operator: dict = {
    '+': op.add,
    '-': op.sub,
    '*': op.mul,
    '/': op.truediv,
    '//': op.floordiv,
    '**': op.pow,
    '%': op.mod
}

if operation in operator:
    print(f'{num1} {operation} {num2} = {operator[operation](num1, num2)}')
else:
    print("Invalid operator")



# number 3
num_dict = {num : num**2 for num in range(1,11)}
print(num_dict)



# number 4

departments = {
    'it':{
        'designer': {'first_name': 'Nick', 'last_name': 'Fox', 'age': 27, 'salary': 3200},
        'developer': {'first_name': 'Ann', 'last_name': 'Summers', 'age': 24, 'salary': 2800},
        'engineer': {'first_name': 'Michel', 'last_name': 'Martin', 'age': 25, 'salary': 3000},
    },
    'marketing': {
        'manager': {'first_name': 'Mike', 'last_name': 'Jonas', 'age': 31, 'salary': 3500},
        'marketer': {'first_name': 'Emily', 'last_name': 'Dumpsy', 'age': 26, 'salary': 2400},
        'copywriter': {'first_name': 'Tom', 'last_name': 'Anderson', 'age': 24, 'salary': 2200},
    },
    'sales': {
        'specialist': {'first_name': 'Mary', 'last_name': 'Edwards', 'age': 32, 'salary': 3500},
        'representator': {'first_name': 'Tim', 'last_name': 'Holland', 'age': 25, 'salary': 2500},
        'analyst': {'first_name': 'Jane', 'last_name': 'Austin', 'age': 28, 'salary': 2800},
    }
}
average_salaries = {}
for key, value in departments.items():
    total_salary = sum(person["salary"] for person in value.values())
    average_salary = total_salary / len(value)
    average_salaries[key] = average_salary    
    
for key, salaries in average_salaries.items():
    print(f"{key} department average salary is {salaries:.2f}")