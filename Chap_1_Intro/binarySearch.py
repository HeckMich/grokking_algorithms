def binary_search(list, item):
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None



def search_number():
    number = input("Which number do you want to search for? ")
    return int (number)

my_list = [12, 34, 56, 78, 90, 112, 134, 156, 178, 200, 222, 244, 266,
           288, 310, 332, 354, 376, 398, 420, 442, 464, 486, 508, 530,
           552, 574, 596, 618, 640, 662, 684, 706, 728, 750, 772, 794,
           816, 838, 860, 882, 904, 926, 948, 970, 992, 1000, 1000,
           1000, 1000]

print(binary_search(my_list, search_number()))
