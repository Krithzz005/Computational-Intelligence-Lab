[23bcs074@mepcolinux ex1]$cat menu.py
from collections import deque
import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def addNode(self, node):
        if node not in self.graph:
            self.graph[node] = []
            print("Node added successfully")
        else:
            print("Node already exists")

    def deleteNode(self, node):
        if node in self.graph:
            for neighbour, _ in self.graph[node]:
                self.graph[neighbour] = [
                    (n, c) for n, c in self.graph[neighbour] if n != node
                ]
            del self.graph[node]
            print("Node deleted successfully")
        else:
            print("Node not found")

    def addEdge(self, u, v, cost):
        if u in self.graph and v in self.graph:
            self.graph[u].append((v, cost))
            self.graph[v].append((u, cost))
            print("Edge added successfully")
        else:
            print("One or both nodes not found")

    def removeEdge(self, u, v, cost):
        if u in self.graph and v in self.graph:
            self.graph[u].remove((v, cost))
            self.graph[v].remove((u, cost))
            print("Edge removed successfully")
        else:
            print("One or both nodes not found")

    def printAdjList(self):
        print("\nAdjacency List:")
        for node in self.graph:
            print(f"{node} : {self.graph[node]}")

    def bfs(self, start, goal):
        queue = deque([start])
        visited = []

        print("\n--- BFS PROCESS ---")
        print("Initial Queue:", list(queue))

        while queue:
            node = queue.popleft()
            print("\nDequeued:", node)

            if node not in visited:
                visited.append(node)
                print("Visited:", visited)

                if node == goal:
                    print("Goal reached")
                    return visited

                for neighbour, _ in self.graph[node]:
                    if neighbour not in visited and neighbour not in queue:
                        queue.append(neighbour)
                        print("Enqueued:", neighbour)

        return visited
    def dfs(self, start, goal):
        stack = [start]
        visited = []

        print("\n--- DFS PROCESS ---")
        print("Initial Stack:", stack)

        while stack:
            node = stack.pop()
            print("\nPopped:", node)

            if node not in visited:
                visited.append(node)
                print("Visited:", visited)

                if node == goal:
                    print("Goal reached")
                    return visited

                for neighbour, _ in reversed(self.graph[node]):
                    if neighbour not in visited and neighbour not in stack:
                        stack.append(neighbour)
                        print("Pushed:", neighbour)

        return visited
g = Graph()
print("\n----- MENU -----")
print("1. Add Node")
print("2. Remove Node")
print("3. Add Edge (with cost)")
print("4. Remove Edge")
print("5. Print Adjacency List")
print("6. BFS")
print("7. DFS")
print("8. UCS")
print("9. Exit")

while True:

   choice = int(input("Enter your choice: "))

   if choice == 1:
        node = input("Enter node name: ")
        g.addNode(node)

   elif choice == 2:
        node = input("Enter node name: ")
        g.deleteNode(node)

   elif choice == 3:
        u = input("Enter first node: ")
        v = input("Enter second node: ")
        cost = int(input("Enter edge cost: "))
        g.addEdge(u, v, cost)

   elif choice == 4:
        u = input("Enter first node: ")
        v = input("Enter second node: ")
        cost = int(input("Enter edge cost: "))
        g.removeEdge(u, v, cost)

   elif choice == 5:
        g.printAdjList()
   elif choice == 6:
        start = input("Enter start node: ")
        goal = input("Enter goal node: ")
        print("\nBFS Traversal:", g.bfs(start, goal))

   elif choice == 7:
        start = input("Enter start node: ")
        goal = input("Enter goal node: ")
        print("\nDFS Traversal:", g.dfs(start, goal))

   elif choice == 8:
        start = input("Enter start node: ")
        goal = input("Enter goal node: ")
        print("\nUCS Traversal:", g.ucs(start, goal))

   elif choice == 9:
        print("Exiting program")
        break

   else:
        print("Invalid choice")
[23bcs074@mepcolinux ex1]$python3 menu.py

----- MENU -----
1. Add Node
2. Remove Node
3. Add Edge (with cost)
4. Remove Edge
5. Print Adjacency List
6. BFS
7. DFS
8. UCS
9. Exit
Enter your choice: 1
Enter node name: A
Node added successfully
Enter your choice: 1
Enter node name: B
Node added successfully
Enter your choice: 1
Enter node name: C
Node added successfully
Enter your choice: 1
Enter node name: D
Node added successfully
Enter your choice: 1
Enter node name: E
Node added successfully
Enter your choice: 1
Enter node name: F
Node added successfully
Enter your choice: 1
Enter node name: G
Node added successfully
Enter your choice: 1
Enter node name: H
Node added successfully
Enter your choice: 1
Enter node name: I
Node added successfully
Enter your choice: 1
Enter node name: J
Node added successfully
Enter your choice: 3
Enter first node: A
Enter second node: B
Enter edge cost: 1
Edge added successfully
Enter your choice: 3
Enter first node: A
Enter second node: C
Enter edge cost: 1
Edge added successfully
Enter your choice: 3
Enter first node: C
Enter second node: D
Enter edge cost: 1
Edge added successfully
Enter your choice: 3
Enter first node: D
Enter second node: E
Enter edge cost: 1
Edge added successfully
Enter your choice: 3
Enter first node: B
Enter second node: E
Enter edge cost: 1
Edge added successfully
Enter your choice: 3
Enter first node: B
Enter second node: G
Enter edge cost: 1
Edge added successfully
Enter your choice: 3
Enter first node: E
Enter second node: H
Enter edge cost: 1
Edge added successfully
Enter your choice: 3
Enter first node: E
Enter second node: F
Enter edge cost: 1
Edge added successfully
Enter your choice: 3
Enter first node: D
Enter second node: F
Enter edge cost: 1
Edge added successfully
Enter your choice: 3
Enter first node: G
Enter second node: H
Enter edge cost: 1
Edge added successfully
Enter your choice: 3
Enter first node: H
Enter second node: F
Enter edge cost: 1
Edge added successfully
Enter your choice: 3
Enter first node: G
Enter second node: I
Enter edge cost: 1
Edge added successfully
Enter your choice: 3
Enter first node: I
Enter second node: J
Enter edge cost: 1
Edge added successfully
Enter your choice: 3
Enter first node: F
Enter second node: J
Enter edge cost: 1
Edge added successfully
Enter your choice: 6
Enter start node: A
Enter goal node: J

--- BFS PROCESS ---
Initial Queue: ['A']

Dequeued: A
Visited: ['A']
Enqueued: B
Enqueued: C

Dequeued: B
Visited: ['A', 'B']
Enqueued: E
Enqueued: G

Dequeued: C
Visited: ['A', 'B', 'C']
Enqueued: D

Dequeued: E
Visited: ['A', 'B', 'C', 'E']
Enqueued: H
Enqueued: F

Dequeued: G
Visited: ['A', 'B', 'C', 'E', 'G']
Enqueued: I

Dequeued: D
Visited: ['A', 'B', 'C', 'E', 'G', 'D']

Dequeued: H
Visited: ['A', 'B', 'C', 'E', 'G', 'D', 'H']

Dequeued: F
Visited: ['A', 'B', 'C', 'E', 'G', 'D', 'H', 'F']
Enqueued: J

Dequeued: I
Visited: ['A', 'B', 'C', 'E', 'G', 'D', 'H', 'F', 'I']

Dequeued: J
Visited: ['A', 'B', 'C', 'E', 'G', 'D', 'H', 'F', 'I', 'J']
Goal reached

BFS Traversal: ['A', 'B', 'C', 'E', 'G', 'D', 'H', 'F', 'I', 'J']
Enter your choice: 7
Enter start node: A
Enter goal node: J

--- DFS PROCESS ---
Initial Stack: ['A']

Popped: A
Visited: ['A']
Pushed: C
Pushed: B

Popped: B
Visited: ['A', 'B']
Pushed: G
Pushed: E

Popped: E
Visited: ['A', 'B', 'E']
Pushed: F
Pushed: H
Pushed: D

Popped: D
Visited: ['A', 'B', 'E', 'D']

Popped: H
Visited: ['A', 'B', 'E', 'D', 'H']

Popped: F
Visited: ['A', 'B', 'E', 'D', 'H', 'F']
Pushed: J

Popped: J
Visited: ['A', 'B', 'E', 'D', 'H', 'F', 'J']
Goal reached

DFS Traversal: ['A', 'B', 'E', 'D', 'H', 'F', 'J']
Enter your choice: 9
Exiting program

[23bcs074@mepcolinux ex1]$ls
bfs.py  ex1.prn  menu.py  ucs.py
[23bcs074@mepcolinux ex1]$cat ucs.py
from collections import deque
class Graph:
    def __init__(self):
        self.wgraph = {}
    def add_node(self, node):
        if node not in self.wgraph:
            self.wgraph[node] = []
        else:
            print("Node already exists")
    def del_node(self, node):
        if node in self.wgraph:
            self.wgraph.pop(node)
            for n in self.wgraph:
                self.wgraph[n] = [(neigh, cost) for neigh, cost in self.wgraph[n] if neigh != node]
        else:
            print("Node doesn't exist")
    def add_edge(self, u, v, w=1):
        if u in self.wgraph and v in self.wgraph:
            if not any(neigh == v for neigh, _ in self.wgraph[u]):
                self.wgraph[u].append((v, w))
            if not any(neigh == u for neigh, _ in self.wgraph[v]):
                self.wgraph[v].append((u, w))
    def del_edge(self, u, v):
        if u in self.wgraph and v in self.wgraph:
            self.wgraph[u] = [(neigh, cost) for neigh, cost in self.wgraph[u] if neigh != v]
            self.wgraph[v] = [(neigh, cost) for neigh, cost in self.wgraph[v] if neigh != u]
    def display(self):
        print("\nWeighted Adjacency List:")
        for node in self.wgraph:
            print(node, "->", self.wgraph[node])
    def ucs(self, start, goal):
        front = [(0, start, [start])]
        explore = set()

        print("\n    UCS Traversal Started    ")
        print(f"Start Node: {start}")
        print(f"Goal Node: {goal}\n")

        step = 0
        while front:
            front.sort(key=lambda x: x[0])

            step += 1
           # print(f"    Step {step}    ")
            print(f"Frontier: {[(cost, node) for cost, node, _ in front]}")
            print(f"Explored: {explore}")

            curr_cost, curr_node, path = front.pop(0)

            print(f"Expanding:['{curr_node}',{curr_cost}]")
            print(f"Current Path: {' -> '.join(map(str, path))}")

            if curr_node == goal:
                print("\n")
                print("Goal Reached..")
                print(f"Optimal Path: {' -> '.join(map(str, path))}")
                print(f"Total Cost: {curr_cost}")
                print("\n")
                return

            explore.add(curr_node)

            neighbors_info = []
            for neigh, step_cost in self.wgraph.get(curr_node, []):
                if neigh not in explore:
                    new_cost = curr_cost + step_cost
                    new_path = path + [neigh]
                    in_front = False
                    for i, (cost, node, old_path) in enumerate(front):
                        if node == neigh:
                            in_front = True
                            if new_cost < cost:
                                neighbors_info.append(f"{neigh} (cost: {new_cost}, updated from {cost})")
                                front[i] = (new_cost, neigh, new_path)
                            else:
                                neighbors_info.append(f"{neigh} (cost: {new_cost}, not updated)")
                            break
                    if not in_front:
                        neighbors_info.append(f"{neigh} (cost: {new_cost}, added)")
                        front.append((new_cost, neigh, new_path))

            if neighbors_info:
                print("Neighbors processed")
#                print(f"Neighbors processed: {', '.join(neighbors_info)}")
            else:
                print("No unvisited neighbors")
            print()

        print(f"\nGoal node {goal} not found. No path exists.")

g = Graph()
print("\n1. Add Node\n2. Delete Node\n3. Add Edge\n4. Delete Edge\n5. Display Graph\n6. UCS Traversal\n7. Exit")
while True:
    ch_input = input("\nEnter your choice: ")
    if not ch_input.strip():
        continue
    try:
        ch = int(ch_input)
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    if ch == 1:
        num = int(input("Enter no.of nodes: "))
        for i in range(num):
            node = input(f"Enter node {i}: ")
            g.add_node(node)
    elif ch == 2:
        node = input("Enter node to delete: ")
        g.del_node(node)
    elif ch == 3:
        no = int(input("Enter no.of edges: "))
        for i in range(no):
            print(f"Edge {i}:")
            u = input("source node: ")
            v = input("destination node: ")
            weight = int(input("weight :"))
            g.add_edge(u, v, weight)
    elif ch == 4:
        u = input("source node: ")
        v = input("destination node: ")
        g.del_edge(u, v)
    elif ch == 5:
        g.display()
    elif ch == 6:
        start = input("start node: ")
        goal = input("goal node: ")
        g.ucs(start, goal)
    elif ch == 7:
        print("End of code")
        break
    else:
        print("Invalid choice")
[23bcs074@mepcolinux ex1]$python3 ucs.py

1. Add Node
2. Delete Node
3. Add Edge
4. Delete Edge
5. Display Graph
6. UCS Traversal
7. Exit

Enter your choice: 1
Enter no.of nodes: 8
Enter node 0: A
Enter node 1: B
Enter node 2: C
Enter node 3: D
Enter node 4: E
Enter node 5: F
Enter node 6: G
Enter node 7: H

Enter your choice: 3
Enter no.of edges: 10
Edge 0:
source node: G
destination node: A
weight :3
Edge 1:
source node: B
destination node: G
weight :4
Edge 2:
source node: D
destination node: G
weight :7
Edge 3:
source node: F
destination node: A
weight :8
Edge 4:
source node: F
destination node: E
weight :1
Edge 5:
source node: E
destination node: B
weight :1
Edge 6:
source node: B
destination node: C
weight :5
Edge 7:
source node: B
destination node: C
weight :6
Edge 8:
source node: C
destination node: H
weight :1
Edge 9:
source node: E
destination node: H
weight :3

Enter your choice: 5

Weighted Adjacency List:
A -> [('G', 3), ('F', 8)]
B -> [('G', 4), ('E', 1), ('C', 5)]
C -> [('B', 5), ('H', 1)]
D -> [('G', 7)]
E -> [('F', 1), ('B', 1), ('H', 3)]
F -> [('A', 8), ('E', 1)]
G -> [('A', 3), ('B', 4), ('D', 7)]
H -> [('C', 1), ('E', 3)]

Enter your choice: 6
start node: A
goal node: H

    UCS Traversal Started
Start Node: A
Goal Node: H

Frontier: [(0, 'A')]
Explored: set()
Expanding:['A',0]
Current Path: A
Neighbors processed

Frontier: [(3, 'G'), (8, 'F')]
Explored: {'A'}
Expanding:['G',3]
Current Path: A -> G
Neighbors processed

Frontier: [(7, 'B'), (8, 'F'), (10, 'D')]
Explored: {'A', 'G'}
Expanding:['B',7]
Current Path: A -> G -> B
Neighbors processed

Frontier: [(8, 'F'), (8, 'E'), (10, 'D'), (12, 'C')]
Explored: {'B', 'A', 'G'}
Expanding:['F',8]
Current Path: A -> F
Neighbors processed

Frontier: [(8, 'E'), (10, 'D'), (12, 'C')]
Explored: {'B', 'A', 'G', 'F'}
Expanding:['E',8]
Current Path: A -> G -> B -> E
Neighbors processed

Frontier: [(10, 'D'), (11, 'H'), (12, 'C')]
Explored: {'B', 'A', 'G', 'F', 'E'}
Expanding:['D',10]
Current Path: A -> G -> D
No unvisited neighbors

Frontier: [(11, 'H'), (12, 'C')]
Explored: {'B', 'A', 'G', 'D', 'F', 'E'}
Expanding:['H',11]
Current Path: A -> G -> B -> E -> H


Goal Reached..
Optimal Path: A -> G -> B -> E -> H
Total Cost: 11



Enter your choice: 7
End of code
[23bcs074@mepcolinux ex1]$exit
exit

