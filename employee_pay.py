import csv

pay = open('employee_data.csv', 'r')

csv_file = csv.reader(pay,delimiter=',')

next(csv_file)

for row in csv_file:

    salary = float(row[3])
    bonus_multiplier = float(row[7])
    bonus = salary * bonus_multiplier
    total_salary = salary + bonus

    print(f'ID: {row[0]}')
    print(f'Name: {row[1]}')
    print(f'Age: {row[2]}')
    print(f'Salary: {row[3]}')
    print(f'Hours Worked: {row[4]}')
    print(f'Productivity: {row[5]}')
    print(f'Team: {row[6]}')
    print(f'Bonus: {bonus:,.2f}')
    print(f'Total salary: {total_salary:,.2f}')
    print()
    input()