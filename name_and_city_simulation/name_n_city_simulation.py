import random
import csv

# generate first_name list and last name list(according to countries)
# we choose 5 countries to simulate:"United Kingdom","France","Germany","Spain","Italy"
with open("name.txt") as f:
    first_name = f.readlines()
first_name = [x.strip() for x in first_name]

with open("france.txt") as f2:
    france_name = f2.readlines()
france_name = [x.strip() for x in france_name]

with open("italy.txt") as f3:
    italy_name = f3.readlines()
italy_name = [x.strip() for x in italy_name]

with open("spain.txt",encoding='utf-8') as f4:
    spain_name = f4.readlines()
spain_name = [x.strip() for x in spain_name]

with open("germany.txt",encoding='utf-8') as f5:
    germany_name = f5.readlines()
germany_name = [x.strip() for x in germany_name]

with open("uk.txt") as f6:
    uk_name = f6.readlines()
uk_name = [x.strip() for x in uk_name]

# generate country list and city list according to country
country = ["United Kingdom","France","Germany","Spain","Italy"]
city = [["London","Manchester"],["Paris", "Lyon"],["Berlin", "Munich"],["Madrid", "Barcelona"],["Milan", "Rome"]]

# store the simulation records of names, country and city
temp_result = []
title = ["First name","Last name", "Country", "City"]
temp_result.append(title)

# simulate the names, country and city for the 250 results
for index in range(0,5):
    country_sample = country[index]
    for k in range(2):
        city_sample = city[index][k] # select 25 records for each city
        for i in range(25):
            random.seed(i) # ensure the reproducibility of each run of 250 records
            fname = random.sample(first_name,1)

            if index == 0:
                last_name = random.sample(uk_name,1)
            elif index == 1:
                last_name = random.sample(france_name, 1)
            elif index == 2:
                last_name = random.sample(germany_name, 1)
            elif index == 3:
                last_name = random.sample(spain_name, 1)
            else:
                last_name = random.sample(italy_name, 1)

        # generate one record and add to list
            temp = [fname[0],last_name[0],country_sample,city_sample]
            temp_result.append(temp)

# print(temp_result)

with open('result.csv', 'w+',newline='',encoding="utf-8") as f7:
    writer = csv.writer(f7)
    writer.writerows(temp_result)