voted = {}

def check_voter(name):
    if name in voted:
        print("Throw him out!")
    else:
        voted[name] = True
        print("Allowed to vote!")

check_voter("Tom")
check_voter("Mike")
check_voter("Mike")