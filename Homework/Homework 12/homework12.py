import csv

# Titanic Survivors 

headers = ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']

with open('titanic.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('survived.csv', 'w', newline='') as survived_file:
        csv_writer = csv.DictWriter(survived_file, fieldnames=headers)
        csv_writer.writeheader()

        for row in csv_reader:
            if row['Survived'] == '1':
                csv_writer.writerow(row)





# Sorted information from organizations

import csv

headers = ['Index', 'Organization Id', 'Name', 'Industry', 'Number of employees', 'Founded']

with open('organizations-100.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    sorted_data = sorted(csv_reader, key=lambda x: int(x['Number of employees']))

    with open('sorted_csv.csv', 'w', newline='') as sorted_file:
        csv_writer = csv.DictWriter(sorted_file, fieldnames=headers)
        csv_writer.writeheader()  
        
        for row in sorted_data:
            filtered_row = {key: row[key] for key in headers}
            csv_writer.writerow(filtered_row)  




# Companies with ssl

headers = ['Organization Id', 'Name', 'Website', 'Industry', 'Number of employees']

ssl_lst = []

with open('organizations-100.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    for row in csv_reader:
        if row['Website'].startswith('https'):

            info = {
                 'Organization Id': row['Organization Id'], 'Name': row['Name'], 'Website': row['Website'], 'Industry': row['Industry'], 'Number of employees': row['Number of employees']
                 }
        
            ssl_lst.append(info)

            with open('ssl_companies.csv', 'w', newline='') as ssl_file:
                    csv_writer = csv.DictWriter(ssl_file, fieldnames=headers)
                    csv_writer.writeheader()
                    csv_writer.writerows(ssl_lst)







