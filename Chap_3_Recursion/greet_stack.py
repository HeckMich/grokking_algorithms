def greet(name):
    print("Hello, " + name + "!")
    greet2(name)
    print("Soon I'll say bye....")
    bye()

def greet2(name):
    print("How are you doin, " + name + "?")

def bye():
    print("Bye")

name = input("Who do you want to greet? ")
greet(name)