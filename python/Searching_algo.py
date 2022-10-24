#Linear Search
def LinearSearch(array,value):
    for i in range(len(array)):
        if array[i]==value:
            return i
    return -1

#print(LinearSearch([20,19,67,45,56],67))

#Binary Search
import math
def binarySearch(array, value):
    start = 0
    end = len(array)-1
    middle = (start+end)//2
    print(start, middle, end)
    while array[middle]!=value and start<=end:
        if value < array[middle]:
            end = middle - 1
        else:
            start = middle + 1 
        middle = (start+end)//2
        # print(start, middle, end)
    if array[middle] == value:
        return middle
    else:
        return -1
        



custArray = [8, 9, 12, 15, 17, 19, 20, 21, 28]
print(binarySearch(custArray, 15))