from collections import defaultdict
num_map = defaultdict(list)

num_map["Sub1"]=[]
num_map["Sub2"]=[]

intnums=[]

n =int(input("Enter number of integers: "))
for i in range(n):
    intnums.append(int(input(f"Enter integer {i+1}: ")))


for i in range(n):
    if (intnums[i] % 10 == 0):
        num_map["Sub1"].append(intnums[i])
    elif (intnums[i] % 10 == 1):
       num_map["Sub2"].append(intnums[i])


print(num_map.items())