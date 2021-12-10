import random
import csv
from numpy import random as np_random
import numpy as np

#read age, bmi and height
with open('result.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    age = [row[5] for row in reader]
    age.remove("age")
with open('result.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    height = [row[6] for row in reader]
    height.remove("height")
with open('result.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    bmi = [row[7] for row in reader]
    bmi.remove("BMI")

# generate country list and case status
country = ["United Kingdom","France","Germany","Spain","Italy"]
city = [["London","Manchester"],["Paris", "Lyon"],["Berlin", "Munich"],["Madrid", "Barcelona"],["Milan", "Rome"]]
case_status = [[1]*12 + [0]*13] * 10
case_status=sum(case_status,[])
education_list = []

temp_result = []
title = ["Country", "Education","Case Status","Gene1","Gene2","Gene3","Gene4","Gene5","Gene6","Gene7","Gene8","Gene9","Gene10","SNP1","SNP2","SNP3","SNP4","SNP5"]
temp_result.append(title)
Education = ["primary", "high_school","bachelor", "master", "phD"]

# simulate the country and education level for the 250 results
for index in range(0,5):
    country_sample = country[index]
    for k in range(2):
        city_sample = city[index][k] # select 25 records for each city
        for i in range(25):
            random.seed(i+index*5+k*2) # ensure the reproducibility of each run of 250 records
            education = random.sample(Education,1)
        # generate one record and add to list
            temp = [country_sample,education[0]]
            temp_result.append(temp)
            education_list.append(education)

#simulate the gene expression and SNP data

#gene1: hskp1
gene1 = [random.uniform(0, 0.3) for i in age]

#gene2: hskp2
gene2 = [random.uniform(0.5, 0.7) for i in age]

#gene3: country
t1 = []
t2 = []
t3 = []
t4 = []
t5 = []

#5 countries have different gene3 expression. Consider also random variation during simulation.
for i in range(50):
    t1.append(random.uniform(0.7, 1))
for i in range(50):
    t2.append(random.uniform(0.4, 0.7))
for i in range(50):
    t3.append(random.uniform(0.1, 0.4))
for i in range(50):
    t4.append(random.uniform(-0.2, 0.1))
for i in range(50):
    t5.append(random.uniform(-0.5, -0.2))

gene3 = t1+t2+t3+t4+t5

#gene4: age
#norm function to limit data to [0,1]
def MaxMinNormalization(x,Max,Min):
	x = (x - Min) / (Max - Min);
	return x;

age = [float(i) for i in age]
gene4= [i * random.uniform(0.8, 1) for i in age]

gene4= [MaxMinNormalization(i,np.max(age),np.min(age))for i in age]

#gene5: bmi
bmi = [float(i) for i in bmi]
gene5= [i * random.uniform(0.5, 0.85) for i in bmi]
gene5 = [MaxMinNormalization(i,np.max(bmi),np.min(bmi))for i in bmi]

#gene6: height
height = [float(i) for i in height]
gene6 = [i * random.uniform(0.5, 0.85) for i in height]

gene6 = [MaxMinNormalization(i,np.max(height),np.min(height))for i in height]

#gene7: cases or not
#1 if case
gene7 = [int(i) * random.uniform(0.9,1) for i in case_status]

#gene8: metrics of cases
gene8 = [float(i) * random.uniform(0.8, 1) for i in gene7]

#gene9: education
gene9 = []
print(len(temp_result))
for i in range(250):
    if education_list[i] == "primary":
        gene9.append(random.uniform(-0.5, -0.4))
    elif education_list[i] == "high_school":
        gene9.append(random.uniform(-0.2, 0.2))
    elif education_list[i] == "bachelor":
        gene9.append(random.uniform(0.2, 0.4))
    elif education_list[i] == "master":
        gene9.append(random.uniform(0.4, 0.7))
    elif education_list[i] == "phD":
        gene9.append(random.uniform(0.7, 1))
    else:
        gene9.append(random.uniform(-1,1))

#gene10: a random gene
gene10= [random.uniform(-1, 1) for i in age]


#SNP1:0,1 according to case status (gene7)
SNP1 = [int(i) for i in case_status]

#SNP2:0,1,2 according to gene8
SNP2 = []
for i in range(250):
    if gene8[i] > 0.3:
        SNP2.append(2)
    elif gene8[i] < -0.3:
        SNP2.append(0)
    else:
        SNP2.append(1)

#SNP3:0,1,2 according to gene9
SNP3 = []
for i in range(250):
    if gene8[i] > 0.5:
        SNP3.append(2)
    elif gene8[i] < -0.5:
        SNP3.append(0)
    else:
        SNP3.append(1)

#SNP4:0,1,2 randomly assigned
SNP4 = []
SNP_value = [0,1,2]

for i in range(250):
    random.seed(i)  # ensure the reproducibility of each run of 250 records
    SNP4.append(random.sample(SNP_value, 1)[0])

#SNP5:0,1,2 according to gender(all female in this simulation case)
SNP5 = [1]*250

#silly code for merging records
for i in range(250):
    temp_result[i+1].append(case_status[i])
for i in range(250):
    temp_result[i+1].append(gene1[i])
for i in range(250):
    temp_result[i+1].append(gene2[i])
for i in range(250):
    temp_result[i+1].append(gene3[i])
for i in range(250):
    temp_result[i+1].append(gene4[i])
for i in range(250):
    temp_result[i+1].append(gene5[i])
for i in range(250):
    temp_result[i+1].append(gene6[i])
for i in range(250):
    temp_result[i+1].append(gene7[i])
for i in range(250):
    temp_result[i+1].append(gene8[i])
for i in range(250):
    temp_result[i+1].append(gene9[i])
for i in range(250):
    temp_result[i+1].append(gene10[i])
for i in range(250):
    temp_result[i+1].append(SNP1[i])
for i in range(250):
    temp_result[i + 1].append(SNP2[i])
for i in range(250):
    temp_result[i + 1].append(SNP3[i])
for i in range(250):
    temp_result[i + 1].append(SNP4[i])
for i in range(250):
    temp_result[i + 1].append(SNP5[i])

#save file
with open('result2.csv', 'w+',newline='',encoding="utf-8") as f7:
    writer = csv.writer(f7)
    print(temp_result)
    writer.writerows(temp_result)