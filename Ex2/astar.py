[23bcs074@mepcolinux ex2]$cat astar.py
import heapq
class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self,node):
        if node not in self.graph:
            self.graph[node]=[]
            return True
        else:
            return False

    def add_edge(self,u,v,cost):
        if u in self.graph and v in self.graph:
            if not any(n == v for n,_ in self.graph[u]):
                self.graph[u].append((v,cost))
                self.graph[v].append((u,cost))
                return True
            else:
                print(f"Edge {u}-{v} is already in the graph.")
                return False
        else:
            print("one or both nodes are not found.")
            return False

    def delete_node(self,node):
        if node in self.graph:
            del self.graph[node]
            for key in self.graph:
                self.graph[key] = [(i,j) for i,j in self.graph[key] if i!=node]
            print(f"{node} is deleted.")
        else:
            print(f"{node} is not found.")

    def delete_edge(self,u,v):
        if u in self.graph and v in self.graph:
            self.graph[u] = [(i,j) for i,j in self.graph[u] if i!=v]
            self.graph[v] = [(i,j) for i,j in self.graph[v] if i!=u]
            print(f"Edge {u}-{v} is deleted.")
        else:
            print("One or both nodes are not found in the graph.")

    def A_search(self,heuristic,start,goal):
        if start not in self.graph or goal not in self.graph:
            print("Start or goal is not found in the given graph!")
            return None
        frontier = []
        heapq.heappush(frontier,(heuristic[start],0,start,[start]))
        visited = {}
        print(f"Initial Fringe: {[(start, 0)]}")
        poss_path = []
        while frontier:
            f,g,node,path = heapq.heappop(frontier)

            if node in visited and visited[node]<g:
                continue
            visited[node]=g

            print("Current Path:"," -> ".join(path))

            if node == goal:
                print("Goal Reached.\n")
                poss_path.append((path,g))
                continue

            for neighbour,edge_cost in self.graph[node]:
                 if neighbour not in path:
                    new_g = g+edge_cost
                    new_f = new_g + heuristic[neighbour]
                    if neighbour not in visited or new_g <= visited.get(neighbour, float('inf')):
                        heapq.heappush(frontier,(new_f,new_g,neighbour,path+[neighbour]))

            print(f"Visited: {visited}\n")
            print("Fringe: ",[(n,c) for _,c,n,_ in frontier])
        if poss_path:
            return poss_path
        else:
            print("Path not found.")
            return None

    def display(self):
        print("Adjacency List:")
        for node,neighbour in self.graph.items():
            print(f"{node} -> ",end="")
            for neigh,cost in neighbour:
                print(f"{neigh}({cost})",end="")
            print()

g = Graph()
n = int(input("Enter the Number of Nodes:"))
if n>50:
    print("Maximum 50 Nodes are allowed.")
    exit()
print("Enter Nodes in Graph:")
for _ in range(n):
    node = input()
    g.add_node(node)
e = int(input("Enter the Number of Edges:"))
for _ in range(e):
    u,v,c = input().split()
    g.add_edge(u,v,int(c))
g.display()
print("\n*** (Informed Search) ***\n")
print("1.Add Node\n2.Add Edge\n3.Delete Node\n4.Delete Edge\n5.A* Search\n6.Display Adjacency List\n8.Exit\n")
exit = True
while(exit):
    n = int(input("Enter the Option:"))
    if n==1:
        a = input("Enter the New Node:")
        if g.add_node(a):
            print(f"node {a} is added.")
        else:
            print(f"node {a} is already in the graph. ")
        g.display()
    elif n==2:
        print("Enter the Edges:")
        x,y = input().split()
        print("Enter the Cost:")
        c = int(input())
        if g.add_edge(x,y,c):
            print(f"Edge {x}-{y} is added with {c}.")
        g.display()
    elif n==3:
        d = input("Enter the Node to Delete:")
        g.delete_node(d)
        g.display()
    elif n==4:
        print("Enter the Edges to delete:")
        o,m = input().split()
        g.delete_edge(o,m)
        g.display()
    elif n==5:
        print("Enter the Heuristic Function for all nodes:")
        h = {}
        for node in g.graph.keys():
            print(f"{node}:",end="")
            f = int(input())
            h[node] = f
        start = input("Enter the Start Node:")
        goal =input("Enter the Goal Node:")
        lis = g.A_search(h,start,goal)
        if lis is not None:
            min = min(j for i,j in lis)
            print("Optimal Path:")
            print("Total Cost: ",min)
            for path,cost in lis:
                if cost == min:
                    print("Path:",(" -> ").join(path))
            print()
    elif n==6:
        g.display()
        print()
    elif n==7:
        exit=False
        print("Exiting from A* Search!!")
    else:
        print("Invalid option!!")
[23bcs074@mepcolinux ex2]$python3 astar.py
Enter the Number of Nodes:15
Enter Nodes in Graph:
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
Enter the Number of Edges:23
1 2 2
2 4 5
2 3 4
4 5 6
3 5 7
4 3 3
5 7 2
5 6 8
6 8 3
8 9 7
6 11 2
6 10 1
6 9 8
11 10 1
10 9 6
9 14 1
10 13 4
11 12 5
12 13 2
13 14 1
12 15 3
13 15 1
14 15 9
Adjacency List:
1 -> 2(2)
2 -> 1(2)4(5)3(4)
3 -> 2(4)5(7)4(3)
4 -> 2(5)5(6)3(3)
5 -> 4(6)3(7)7(2)6(8)
6 -> 5(8)8(3)11(2)10(1)9(8)
7 -> 5(2)
8 -> 6(3)9(7)
9 -> 8(7)6(8)10(6)14(1)
10 -> 6(1)11(1)9(6)13(4)
11 -> 6(2)10(1)12(5)
12 -> 11(5)13(2)15(3)
13 -> 10(4)12(2)14(1)15(1)
14 -> 9(1)13(1)15(9)
15 -> 12(3)13(1)14(9)

*** (Informed Search) ***

1.Add Node
2.Add Edge
3.Delete Node
4.Delete Edge
5.A* Search
6.Display Adjacency List
8.Exit

Enter the Option:5
Enter the Heuristic Function for all nodes:
1:10
2:14
3:13
4:2
5:2
6:5
7:9
8:4
9:8
10:5
11:0
12:4
13:6
14:7
15:1
Enter the Start Node:1
Enter the Goal Node:11
Initial Fringe: [('1', 0)]
Current Path: 1
Visited: {'1': 0}

Fringe:  [('2', 2)]
Current Path: 1 -> 2
Visited: {'1': 0, '2': 2}

Fringe:  [('4', 7), ('3', 6)]
Current Path: 1 -> 2 -> 4
Visited: {'1': 0, '2': 2, '4': 7}

Fringe:  [('5', 13), ('3', 6), ('3', 10)]
Current Path: 1 -> 2 -> 4 -> 5
Visited: {'1': 0, '2': 2, '4': 7, '5': 13}

Fringe:  [('3', 6), ('3', 10), ('3', 20), ('7', 15), ('6', 21)]
Current Path: 1 -> 2 -> 3
Visited: {'1': 0, '2': 2, '4': 7, '5': 13, '3': 6}

Fringe:  [('5', 13), ('3', 10), ('3', 20), ('6', 21), ('7', 15)]
Current Path: 1 -> 2 -> 3 -> 5
Visited: {'1': 0, '2': 2, '4': 7, '5': 13, '3': 6}

Fringe:  [('3', 10), ('7', 15), ('6', 21), ('6', 21), ('7', 15), ('3', 20)]
Current Path: 1 -> 2 -> 3 -> 5 -> 7
Visited: {'1': 0, '2': 2, '4': 7, '5': 13, '3': 6, '7': 15}

Fringe:  [('7', 15), ('6', 21), ('6', 21), ('3', 20)]
Current Path: 1 -> 2 -> 4 -> 5 -> 7
Visited: {'1': 0, '2': 2, '4': 7, '5': 13, '3': 6, '7': 15}

Fringe:  [('6', 21), ('6', 21), ('3', 20)]
Current Path: 1 -> 2 -> 3 -> 5 -> 6
Visited: {'1': 0, '2': 2, '4': 7, '5': 13, '3': 6, '7': 15, '6': 21}

Fringe:  [('11', 23), ('6', 21), ('8', 24), ('3', 20), ('10', 22), ('9', 29)]
Current Path: 1 -> 2 -> 3 -> 5 -> 6 -> 11
Goal Reached.

Current Path: 1 -> 2 -> 4 -> 5 -> 6
Visited: {'1': 0, '2': 2, '4': 7, '5': 13, '3': 6, '7': 15, '6': 21, '11': 23}

Fringe:  [('11', 23), ('8', 24), ('10', 22), ('9', 29), ('3', 20), ('8', 24), ('10', 22), ('9', 29)]
Current Path: 1 -> 2 -> 4 -> 5 -> 6 -> 11
Goal Reached.

Current Path: 1 -> 2 -> 3 -> 5 -> 6 -> 10
Visited: {'1': 0, '2': 2, '4': 7, '5': 13, '3': 6, '7': 15, '6': 21, '11': 23, '10': 22}

Fringe:  [('11', 23), ('8', 24), ('10', 22), ('13', 26), ('3', 20), ('9', 29), ('8', 24), ('9', 29), ('9', 28)]
Current Path: 1 -> 2 -> 3 -> 5 -> 6 -> 10 -> 11
Goal Reached.

Current Path: 1 -> 2 -> 4 -> 5 -> 6 -> 10
Visited: {'1': 0, '2': 2, '4': 7, '5': 13, '3': 6, '7': 15, '6': 21, '11': 23, '10': 22}

Fringe:  [('11', 23), ('8', 24), ('9', 28), ('8', 24), ('13', 26), ('9', 29), ('9', 29), ('13', 26), ('9', 28), ('3', 20)]
Current Path: 1 -> 2 -> 4 -> 5 -> 6 -> 10 -> 11
Goal Reached.

Current Path: 1 -> 2 -> 3 -> 5 -> 6 -> 8
Visited: {'1': 0, '2': 2, '4': 7, '5': 13, '3': 6, '7': 15, '6': 21, '11': 23, '10': 22, '8': 24}

Fringe:  [('8', 24), ('13', 26), ('9', 28), ('3', 20), ('13', 26), ('9', 29), ('9', 29), ('9', 28), ('9', 31)]
Current Path: 1 -> 2 -> 4 -> 5 -> 6 -> 8
Visited: {'1': 0, '2': 2, '4': 7, '5': 13, '3': 6, '7': 15, '6': 21, '11': 23, '10': 22, '8': 24}

Fringe:  [('13', 26), ('13', 26), ('9', 28), ('3', 20), ('9', 31), ('9', 29), ('9', 29), ('9', 28), ('9', 31)]
Current Path: 1 -> 2 -> 3 -> 5 -> 6 -> 10 -> 13
Visited: {'1': 0, '2': 2, '4': 7, '5': 13, '3': 6, '7': 15, '6': 21, '11': 23, '10': 22, '8': 24, '13': 26}

Fringe:  [('15', 27), ('13', 26), ('9', 28), ('3', 20), ('12', 28), ('9', 29), ('9', 29), ('9', 31), ('9', 28), ('9', 31), ('14', 27)]
Current Path: 1 -> 2 -> 3 -> 5 -> 6 -> 10 -> 13 -> 15
Visited: {'1': 0, '2': 2, '4': 7, '5': 13, '3': 6, '7': 15, '6': 21, '11': 23, '10': 22, '8': 24, '13': 26, '15': 27}

Fringe:  [('13', 26), ('12', 28), ('9', 28), ('3', 20), ('14', 27), ('9', 29), ('9', 29), ('9', 31), ('9', 28), ('9', 31), ('12', 30), ('14', 36)]
Current Path: 1 -> 2 -> 4 -> 5 -> 6 -> 10 -> 13
Visited: {'1': 0, '2': 2, '4': 7, '5': 13, '3': 6, '7': 15, '6': 21, '11': 23, '10': 22, '8': 24, '13': 26, '15': 27}

Fringe:  [('15', 27), ('3', 20), ('12', 28), ('9', 28), ('14', 27), ('14', 27), ('12', 28), ('9', 31), ('14', 36), ('9', 31), ('12', 30), ('9', 29), ('9', 28), ('9', 29)]
Current Path: 1 -> 2 -> 4 -> 5 -> 6 -> 10 -> 13 -> 15
Visited: {'1': 0, '2': 2, '4': 7, '5': 13, '3': 6, '7': 15, '6': 21, '11': 23, '10': 22, '8': 24, '13': 26, '15': 27}

Fringe:  [('12', 28), ('3', 20), ('12', 28), ('9', 28), ('14', 27), ('14', 27), ('12', 30), ('9', 31), ('14', 36), ('9', 31), ('12', 30), ('9', 29), ('9', 28), ('9', 29), ('14', 36)]
Current Path: 1 -> 2 -> 3 -> 5 -> 6 -> 10 -> 13 -> 12
Visited: {'1': 0, '2': 2, '4': 7, '5': 13, '3': 6, '7': 15, '6': 21, '11': 23, '10': 22, '8': 24, '13': 26, '15': 27, '12': 28}

Fringe:  [('12', 28), ('3', 20), ('14', 27), ('9', 28), ('14', 27), ('9', 28), ('12', 30), ('9', 31), ('14', 36), ('9', 31), ('12', 30), ('9', 29), ('14', 36), ('9', 29)]
Current Path: 1 -> 2 -> 4 -> 5 -> 6 -> 10 -> 13 -> 12
Visited: {'1': 0, '2': 2, '4': 7, '5': 13, '3': 6, '7': 15, '6': 21, '11': 23, '10': 22, '8': 24, '13': 26, '15': 27, '12': 28}

Fringe:  [('3', 20), ('14', 27), ('14', 27), ('9', 28), ('12', 30), ('9', 28), ('12', 30), ('9', 31), ('14', 36), ('9', 31), ('9', 29), ('9', 29), ('14', 36)]
Current Path: 1 -> 2 -> 3 -> 5 -> 6 -> 10 -> 13 -> 14
Visited: {'1': 0, '2': 2, '4': 7, '5': 13, '3': 6, '7': 15, '6': 21, '11': 23, '10': 22, '8': 24, '13': 26, '15': 27, '12': 28, '14': 27}

Fringe:  [('14', 27), ('12', 30), ('12', 30), ('9', 28), ('9', 29), ('9', 28), ('9', 29), ('9', 31), ('14', 36), ('9', 31), ('14', 36), ('9', 28)]
Current Path: 1 -> 2 -> 4 -> 5 -> 6 -> 10 -> 13 -> 14
Visited: {'1': 0, '2': 2, '4': 7, '5': 13, '3': 6, '7': 15, '6': 21, '11': 23, '10': 22, '8': 24, '13': 26, '15': 27, '12': 28, '14': 27}

Fringe:  [('12', 30), ('9', 28), ('12', 30), ('9', 28), ('9', 29), ('9', 28), ('9', 29), ('9', 31), ('14', 36), ('9', 31), ('14', 36), ('9', 28)]
Current Path: 1 -> 2 -> 3 -> 5 -> 6 -> 10 -> 13 -> 14 -> 9
Visited: {'1': 0, '2': 2, '4': 7, '5': 13, '3': 6, '7': 15, '6': 21, '11': 23, '10': 22, '8': 24, '13': 26, '15': 27, '12': 28, '14': 27, '9': 28}

Fringe:  [('9', 28), ('9', 28), ('9', 28), ('9', 31), ('9', 29), ('14', 36), ('9', 29), ('9', 31), ('14', 36)]
Current Path: 1 -> 2 -> 3 -> 5 -> 6 -> 10 -> 9
Visited: {'1': 0, '2': 2, '4': 7, '5': 13, '3': 6, '7': 15, '6': 21, '11': 23, '10': 22, '8': 24, '13': 26, '15': 27, '12': 28, '14': 27, '9': 28}

Fringe:  [('9', 28), ('9', 28), ('9', 29), ('9', 31), ('9', 29), ('14', 36), ('14', 36), ('9', 31)]
Current Path: 1 -> 2 -> 4 -> 5 -> 6 -> 10 -> 13 -> 14 -> 9
Visited: {'1': 0, '2': 2, '4': 7, '5': 13, '3': 6, '7': 15, '6': 21, '11': 23, '10': 22, '8': 24, '13': 26, '15': 27, '12': 28, '14': 27, '9': 28}

Fringe:  [('9', 28), ('9', 29), ('9', 29), ('9', 31), ('9', 31), ('14', 36), ('14', 36)]
Current Path: 1 -> 2 -> 4 -> 5 -> 6 -> 10 -> 9
Visited: {'1': 0, '2': 2, '4': 7, '5': 13, '3': 6, '7': 15, '6': 21, '11': 23, '10': 22, '8': 24, '13': 26, '15': 27, '12': 28, '14': 27, '9': 28}

Fringe:  [('9', 29), ('9', 31), ('9', 29), ('14', 36), ('9', 31), ('14', 36)]
Optimal Path:
Total Cost:  23
Path: 1 -> 2 -> 3 -> 5 -> 6 -> 11
Path: 1 -> 2 -> 4 -> 5 -> 6 -> 11
Path: 1 -> 2 -> 3 -> 5 -> 6 -> 10 -> 11
Path: 1 -> 2 -> 4 -> 5 -> 6 -> 10 -> 11

Enter the Option:7
Exiting from A* Search!!
[23bcs074@mepcolinux ex2]$exit
exit
