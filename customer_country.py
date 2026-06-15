import csv

with open('customers.csv','r') as infile, open('customer_country.csv','w') as outfile:

    csv_file = csv.reader(infile, delimiter = ',')

    outfile.write('Full Name, Country\n')

    next(csv_file)

    for row in csv_file:
        name = row[1] + ' ' + row[2]
        country = row[4]
     
        outfile.write(name + ', ' + country + '\n')

print('The new file has been created')

outfile.close()