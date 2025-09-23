n = int(input("Enter number of strings: "))

words = []

for i in range(n):
    s = input("Enter string: ")
    words.append(s)

occurance = {}


for word in words:
    for char in word.lower():  
        if char.isalpha():     
            occurance[char] = occurance.get(char, 0) + 1

print(occurance)
