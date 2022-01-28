# same as : https://www.lintcode.com/problem/872/

class Solution:
    """
    @param pid: the process id
    @param ppid: the parent process id
    @param kill: a PID you want to kill
    @return: a list of PIDs of processes that will be killed in the end
    """

    def killProcess(self, pid, ppid, kill):
        adjlist = {}
        for p in pid:
            adjlist[p] = []
        for i in range(len(ppid)):
            if ppid[i] not in adjlist:
                adjlist[ppid[i]] = []
            adjlist[ppid[i]].append(pid[i])
        return dfs(adjlist, kill)


def dfs(adjlist, node):
    if node is None:
        return []
    ans = [node]
    for child in adjlist[node]:
        ans += dfs(adjlist, child)
    return ans


