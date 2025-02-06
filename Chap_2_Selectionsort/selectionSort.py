def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

def user_array():
    user_input = input("Please input numbers, seperated with a space: ")
    numbers_as_string = user_input.split()
    numbers_as_int = [int(number) for number in numbers_as_string]
    return numbers_as_int

get_array  = user_array()
print(selectionSort(get_array))
