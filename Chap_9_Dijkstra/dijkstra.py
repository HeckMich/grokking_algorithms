

graph = {}

graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}

infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs)     #searches for cheapest node that wasn't processed yet
while node is not None:                 #loop finishes when all nodes are processed
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():           #goes through all neighbors of node
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:         # if it is cheaper to reach the neighbor over this node...
            costs[n] = new_cost         #... the costs for the node will be updated
            parents[n] = node           #this node becomes new parent of this neighbor
    processed.append(node)              # mark node as processed
    node = find_lowest_cost_node(costs) #look for the next node to be processed





print(graph["start"].keys())
print(graph["start"]["a"])
print(graph["start"]["b"])