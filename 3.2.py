import csv
from collections import defaultdict
csv_map = defaultdict(list)
name=[]
num=[]
with open('3.2.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
       if row==['Num','Name']:
              continue
       csv_map[float(row[0])].append(row[1])

dist_list=sorted(csv_map.items())

print("Sorted list: ",dist_list)

new_list = [] 

for item in dist_list:
    if item[0] % 2 == 0:  
        new_list.append(item)  

dist_list = []

for key, values in new_list:
    stripped_values = []  
    for value in values:
        stripped_values.append(value.strip())  
    dist_list.append((key, stripped_values))

names = ""
for key, values in dist_list:
    names += "".join(values)

print(names)

min_diff=None
for i in range(len(names)-1):
        diff = abs(ord(names[i])-ord(names[i+1]))
        if min_diff is None or diff < min_diff:
            min_diff = diff

print("Odd rows removed:", new_list)
print("Minimum difference between adjacent characters:", min_diff)
