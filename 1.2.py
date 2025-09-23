class sort:
    def __init__(self, string_list):
        self.string_list = string_list

    def select_sort(self):
        n = len(self.string_list)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if self.string_list[j] < self.string_list[min_index]:
                    min_index = j
            self.string_list[i], self.string_list[min_index] = self.string_list[min_index], self.string_list[i]

    def newlist(self):
        return self.string_list

n = int(input("Enter number of strings: "))
words = []
for i in range(n):
    s = input("Enter string: ")
    words.append(s)
sorter = sort(words)
sorter.select_sort()

print("Sorted list:", sorter.newlist())
