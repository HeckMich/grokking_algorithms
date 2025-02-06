def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)

number = int(input("Which number do you want to take factorial? "))
print(fact(number))