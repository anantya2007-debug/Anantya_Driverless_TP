from collections import defaultdict

num_map = defaultdict(list)
num_map["Sub1"] = []
num_map["Sub2"] = []

intnums = []
n = int(input("Enter number of integers: "))
for i in range(n):
    intnums.append(int(input(f"Enter integer {i+1}: ")))

for num in intnums:
    if num % 10 == 0:
        l = num_map["Sub1"]
        low, high = 0, len(l)
        while low < high:
            mid = (low + high) // 2
            if l[mid] < num:
                low = mid + 1
            else:
                high = mid
        l.insert(low, num)

    elif num % 10 == 1:
        l = num_map["Sub2"]
        low, high = 0, len(l)
        while low < high:
            mid = (low + high) // 2
            if l[mid] < num:
                low = mid + 1
            else:
                high = mid
        l.insert(low, num)

print(num_map.items())
