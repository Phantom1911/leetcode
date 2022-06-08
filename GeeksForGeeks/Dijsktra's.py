import threading

import heapq


class Edge:
    def __init__(self, src, nbr, wt):
        self.src = src
        self.nbr = nbr
        self.wt = wt


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

    # write your code here
    heap = []
    heapq.heappush(heap, (0, src, str(src)))  # (currdis, currnode, currpath)
    seen = set()
    while len(seen) != vtces:
        curr = heapq.heappop(heap)
        currdis, currnode, currpath = curr[0], curr[1], curr[2]
        if curr in seen:
            continue
        seen.add(currnode)
        print(str(currnode) + " via " + currpath + " @ " + str(currdis))
        for e in graph[currnode]:
            nextdis = currdis + e.wt
            nextpath = currpath + str(e.nbr)
            nextnode = e.nbr
            if nextnode not in seen:
                heapq.heappush(heap, (nextdis, nextnode, nextpath))


if __name__ == '__main__':
    main()

