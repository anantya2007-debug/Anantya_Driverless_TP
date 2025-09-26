from collections import defaultdict
num_map = defaultdict(list)

intnums=[]

n =int(input("Enter number of integers: "))
for i in range(n):
    intnums.append(int(input(f"Enter integer {i+1}: ")))


for i in range(n):
    n=intnums[i] % 10
    num_map[n].append(intnums[i])


for i in range(10):
    if num_map[i]!=[]:
     a=num_map.get(i)
     print("Reminder ",i,":",a)