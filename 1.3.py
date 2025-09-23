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


class Search:
    def __init__(self, string_list):
        self.string_list = sorted(string_list)  
        self.data = None
        self.position = None 

    def input_word(self):
        self.data = input("Enter word to be searched: ")

    def bin_search(self):
        low = 0
        high = len(self.string_list) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.data == self.string_list[mid]:
                self.position = mid
                return
            elif self.data < self.string_list[mid]:
                high = mid - 1
            else:
                low = mid + 1
         

    def output(self):
        return self.position


n = int(input("Enter number of strings: "))
words = []
for i in range(n):
    s = input("Enter string: ")
    words.append(s)
sorter = sort(words)
sorter.select_sort()

words=sorter.newlist()

bsearch = Search(words)
bsearch.input_word()
bsearch.bin_search()


print("Your word is at position:", bsearch.output())
