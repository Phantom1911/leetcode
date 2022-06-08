import threading, queue


class Edge:
    def __init__(self, src, nbr, wt):
        self.src = src
        self.nbr = nbr
        self.wt = wt


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
        wt = int(lines[2])
        e1 = Edge(v1, v2, wt)
        e2 = Edge(v2, v1, wt)
        graph[e1.src].append(e1)
        graph[e2.src].append(e2)

    src = int(input())
    t = int(input())
    # Write your code here
    q = deque()
    q.append((src, 0))
    count = 0
    seen = set()
    while q:
        curr = q.popleft()
        currnode, currtime = curr[0], curr[1]
        if currtime < t:
            count += 1
        else:
            break
        seen.add(currnode)
        for n in graph[currnode]:
            nbr = n.nbr
            if nbr not in seen:
                q.append((nbr, currtime + 1))
    print(count-1)


if __name__ == "__main__":
    main()