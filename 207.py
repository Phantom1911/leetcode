class Solution:
    def canFinish(self, numCourses, prerequisites) :
        # build a adj list from the input
        # adj list has node's value as the key and the set of nodes that it has outgoing edges to as the value
        adjlist = {}
        for prereq in prerequisites:
            firstcourse, secondcourse = prereq[1], prereq[0]
            if firstcourse not in adjlist:
                adjlist[firstcourse] = set()
            adjlist[firstcourse].add(secondcourse)
        cycle = False
        for src in adjlist:
            seen = set()
            cycle = cycle or self.hascycle(src, seen, adjlist)
        if cycle:
            return False
        else:
            return True
    # the below method of detecting cycle without .copy() would have worked in case of an undirected graph - since it establishes that you are able to visit a node by two differennt paths from the source
    # however this is not the correct inference for a directed graph, example [[1,4],[2,4],[3,1],[3,2]]
    # in order to tackle this, each of the different paths that emerge out of the src should be stored separately
    # if you encounter a node that you have already met in the currentPath - that means that there is a cycle
    # the below code passes 46/51 TCs in LC - gives TLE, so is most probably logically correct but not the most optimal

    # an optimization can be done where we store the path if that node has already been considered as a src before, so that we don't process it again
    def hascycle(self, src, currPath, adjlist):
        # this if check is necessary since it is possible that src doesn't have any outgoing edges
        if src in currPath:
            return True
        currPath.add(src)
        ans = False
        if src in adjlist:
            nbrs = adjlist[src]
            for nbr in nbrs:
                ans = ans or self.hascycle(nbr, currPath.copy(), adjlist)
        return ans


'''
obvious way to solve this to keep a track of the nnumber of parents of each node,
which means the indegree of each node
a node with indegree 0 essentially means that it doesn't have any prereqs, and can be taken up immediately
keep on reducing the indegrees of nodes as and when you process the nodes
'''


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {n: [] for n in range(numCourses)}
        parent_count = {n: 0 for n in range(numCourses)}
        for prerequisite in prerequisites:
            graph[prerequisite[1]].append(prerequisite[0])
            parent_count[prerequisite[0]] += 1

        q = deque()
        for node in graph:
            if parent_count[node] == 0:
                q.append(node)
        res = []
        while len(q) > 0:
            cur = q.popleft()
            res.append(cur)
            for child in graph[cur]:
                parent_count[child] -= 1
                if parent_count[child] == 0:
                    q.append(child)
        if len(res) != numCourses:
            return False
        else:
            return True

if __name__=="__main__":
    print(Solution().canFinish(5,[[1,4],[2,4],[3,1],[3,2]]))