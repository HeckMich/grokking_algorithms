def quicksort(array):
    if len(array) < 2:
        return array #Base-case: empty array or arrays with 1 element are already sorted
    else:
        pivot = array[0] # recursion-case
        less = [i for i in array[1:] if i <= pivot] #sub-array with elements smaller than pivot-element
        greater = [i for i in array[1:] if i > pivot] #sub-array with elements bigger than pivot-element
        return quicksort(less) + [pivot] + quicksort(greater)

print (quicksort([42, 342, 54, 321, 2, 435, 5]))