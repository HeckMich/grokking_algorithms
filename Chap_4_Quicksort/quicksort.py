def quicksort(array):
    if len(array) < 2:
        return array #Base-case: empty array or arrays with 1 element are already sorted
    else:
        pivot = array[0] # recursion-case
        less = [i for i in array[1:] if i <= pivot] #sub-array with elements smaller than pivot-element
        greater = [i for i in array[1:] if i > pivot] #sub-array with elements bigger than pivot-element
        return quicksort(less) + [pivot] + quicksort(greater)

def user_array():
    user_input = input("Please input numbers, seperated with a space: ")
    numbers_as_string = user_input.split()
    numbers_as_int = [int(number) for number in numbers_as_string]
    return numbers_as_int

get_array  = user_array()

print (quicksort(get_array))