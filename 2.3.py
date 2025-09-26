
from collections import defaultdict

num_map = defaultdict(list)


intnums = []
n = int(input("Enter number of integers: "))
for i in range(n):
    intnums.append(int(input(f"Enter integer {i+1}: ")))

for num in intnums:
    if num < 0:
        n=10 -(-num % 10)
    else:
        n=num % 10
    l = num_map[n]
    low, high = 0, len(l)
    while low < high:
        mid = (low + high) // 2
        if l[mid] < num:
            low = mid + 1
        else:
            high = mid
    l.insert(low, num)

for i in range(10):
    if num_map[i]!=[]:
     a=num_map.get(i)
     print("Reminder ",i,":",a)
