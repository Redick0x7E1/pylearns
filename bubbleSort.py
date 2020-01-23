"""
Test for bubble sort algorithm.

for i in range(arr)
Move biggest cell to the right.
Start over.
"""

def bubbleSort(arr1):
    for i in range(0, len(arr1) - 1):
        for j in range(0, len(arr1)-1-i):
            if arr1[j] > arr1[j+1]:
                arr1[j], arr1[j+1] = arr1[j+1], arr1[j]
                print(arr1) # show iterations
    return arr1


list = [8,1,4,5,6,7]
print(bubbleSort(list))