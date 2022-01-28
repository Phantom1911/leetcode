
cycle =False
def topologicalSort(jobs, deps):
    def dfs(node, adj_list, visited, onStack, ans):
        visited[node] = True
        onStack[node] = True
        for nbr in adj_list[node]:
            if onStack[nbr] == True:
                global cycle
                cycle = True
                return
            elif visited[nbr] == False:
                dfs(nbr, adj_list, visited, onStack,  ans)
        onStack[node] = False
        ans.append(node)

    # Write your code here.
    adj_list = dict()
    for job in jobs:
        adj_list[job] = []
    for dep in deps:
        adj_list[dep[0]].append(dep[1])

    visited = dict()
    for job in jobs:
        visited[job] = False
    onStack = dict()
    for job in jobs:
        onStack[job] = False
    ans = []
    for job in jobs:
        if visited[job] is False:
            dfs(job, adj_list, visited, onStack, ans)
    print(cycle)
    if cycle:
        print("empty array")
        return []
    ans.reverse()
    print(ans)
    return ans


from collections import deque


def topologicalSort2(jobs, deps):
    adjlist = {n: [] for n in range(1, len(jobs) + 1, 1)}
    n = len(jobs)
    indegree = {i: 0 for i in jobs}
    for dep in deps:
        first, second = dep[0], dep[1]
        adjlist[first].append(second)
        indegree[second] += 1
    q = deque()
    start = -1
    for i in jobs:
        if indegree[i] == 0:
            q.append(i)
            start = i
    # if there is no node with indegree 0, we can't have a topological sort
    if start == -1:
        return []
    ans = []
    while len(q) != 0:
        currcourse = q.popleft()
        ans.append(currcourse)
        print("currcourse " + str(currcourse))
        if currcourse in adjlist:
            for nbr in adjlist[currcourse]:
                indegree[nbr] -= 1
                # append to the queue only if indegree of nbr is 0
                if indegree[nbr] == 0:
                    q.append(nbr)
    print(ans)
    if len(ans) != len(jobs):
        return []
    return ans


if __name__ == "__main__":
    jobs = [1, 2, 3, 4, 5, 6, 7, 8]
    deps = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 1]]
    topologicalSort2(jobs, deps)
