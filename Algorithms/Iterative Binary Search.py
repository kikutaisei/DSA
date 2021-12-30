class IterativeBinarySearch:
    def returnIndex(self, list, target, leftPointer, rightPointer):
        while leftPointer <= rightPointer:
            midpoint = (leftPointer + rightPointer) // 2

            if list[midpoint] == target:
                return midpoint
            elif list[midpoint] > target:
                rightPointer = midpoint - 1
            elif list[midpoint] < target:
                leftPointer = midpoint + 1

        return None

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]

testSearch1 = IterativeBinarySearch()
print(testSearch1.returnIndex(numbers, 8, 0, len(numbers) - 1)) # Prints "8"

testSearch2 = IterativeBinarySearch()
print(testSearch2.returnIndex(numbers, 10, 0, len(numbers) - 1)) # Prints "None"
