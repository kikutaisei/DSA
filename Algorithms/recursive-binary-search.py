class RecursiveBinarySearch:
    def returnIndex(self, list, target, leftPointer, rightPointer):
        if leftPointer <= rightPointer:
            midpoint = (leftPointer + rightPointer) // 2

            if list[midpoint] == target:
                return midpoint
            elif list[midpoint] > target:
                return self.returnIndex(list, target, leftPointer, midpoint - 1)
            elif list[midpoint] < target:
                return self.returnIndex(list, target, midpoint + 1, rightPointer)

        else:
            return None

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]

testSearch1 = RecursiveBinarySearch()
print(testSearch1.returnIndex(numbers, 8, 0, len(numbers) - 1)) # Prints "8"

testSearch2 = RecursiveBinarySearch()
print(testSearch2.returnIndex(numbers, 10, 0, len(numbers) - 1)) # Prints "None"
