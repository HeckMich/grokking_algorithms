def sum(arr):
    total = 0
    for x in arr:
        total += x
    return total

def user_array():
    user_input = input("Please input numbers, seperated with a space: ")
    numbers_as_string = user_input.split()
    numbers_as_int = [int(number) for number in numbers_as_string]
    return numbers_as_int

get_array  = user_array()

print(sum(get_array))