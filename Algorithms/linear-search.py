class LinearSearch:
    def returnIndex(self, list, target):
        for i in range(len(list)):
            if list[i] == target:
                return i
        return None

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]

testSearch1 = LinearSearch()
print(testSearch1.returnIndex(numbers, 8)) # Prints "8"

testSearch2 = LinearSearch()
print(testSearch2.returnIndex(numbers, 10)) # Prints "None"
