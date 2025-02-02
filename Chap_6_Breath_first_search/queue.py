from collections import deque


def person_is_seller(name):
    return name[-1] == 'm'

graph = {}
graph["Michael"] = ["Alice", "Bob", "Claire"]
graph["Bob"] = ["Anuj", "Peggy"]
graph["Alice"] = ["Peggy"]
graph["Claire"] = ["Tom", "Jonny"]
graph["Anuj"] = []
graph["Peggy"] = []
graph["Tom"] = []
graph["Jonny"] = []



def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person_is_seller(person):
            print(person + " is MangoSalesman")
            return True
        else:
            search_queue += graph[person]
            searched.append(person)
    return False

search("Michael")



