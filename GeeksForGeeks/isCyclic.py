class Edge:
    def __init__(self, src, nbr):
        self.src = src
        self.nbr = nbr


from collections import deque


def main():
    vtces = int(input())
    edges = int(input())
    graph = {}
    for i in range(vtces):
        graph[i] = []

    for i in range(edges):
        lines = input().split(" ")
        v1 = int(lines[0])
        v2 = int(lines[1])
        e1 = Edge(v1, v2)
        e2 = Edge(v2, v1)
        graph[e1.src].append(e1)
        graph[e2.src].append(e2)

    # write your code here
    # q = deque()
    seen = set()
    flag = False
    for key in graph:
        if key not in seen:
            flag = bfs(key, graph, seen) or flag

    if flag:
        print("true")
    else:
        print("false")
    # return flag


def bfs(src, adjlist, seen):
    q = deque()
    q.append(src)
    while q:
        curr = q.popleft()
        seen.add(curr)
        if curr in adjlist:
            for e in adjlist[curr]:
                if e.nbr in q:
                    return True
                if e.nbr not in seen:
                    q.append(e.nbr)
    return False


if __name__ == "__main__":
    main()