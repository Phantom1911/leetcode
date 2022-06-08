def main():
    n = int(input())
    k = int(input())

    # write your code here
    adjlist = {i: set() for i in range(n)}
    for i in range(k):
        a, b = input().split(" ")
        a, b = int(a), int(b)
        adjlist[a].add(b)
        adjlist[b].add(a)

    # figure out no of elements in each connected component
    seen = set()
    conCompSizes = []
    for key in adjlist:
        if key not in seen:
            currCompSize = [0]
            currSeen = set()
            dfs(key, adjlist, currCompSize, currSeen)
            conCompSizes.append(currCompSize[0])
            seen = currSeen.union(seen)

    ans = 0
    for compSize in conCompSizes:
        ans += (compSize * (n - compSize))
    return ans // 2


def dfs(node, adjlist, currCompSize, currSeen):
    currCompSize[0] += 1
    currSeen.add(node)
    for child in adjlist[node]:
        if child not in currSeen:
            dfs(child, adjlist, currCompSize, currSeen)


if __name__ == "__main__":
    print(main())