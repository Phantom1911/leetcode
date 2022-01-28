from collections import deque


def dijkstrasAlgorithm(start, edges):
    dis = [float("inf") for i in range(len(edges))]
    dis[start] = 0
    q = deque()
    # update for immediate nbrs of start
    for edge in edges[start]:
        # put the tuple (dest_node, src_dis_from_start, dis_bw_dest_and_src)
        q.append((edge[0], 0, edge[1]))
    total_edges = 0
    for e in edges:
        total_edges += len(e)
    # all the edges need to be explored to make sure that all the distances are set to min
    # the edge relaxation needs to take place as many number of times as total number of edges
    while total_edges > 0:
        curr = q.popleft()
        dis[curr[0]] = min(dis[curr[0]], curr[1] + curr[2])
        currnode = curr[0]
        for nbr in edges[currnode]:
            q.append((nbr[0], dis[currnode], nbr[1]))
        total_edges -= 1
    for i in range(len(dis)):
        if dis[i] == float("inf"):
            dis[i] = -1
    return dis


if __name__=="__main__":
    print(dijkstrasAlgorithm(0, [
  [
    [1, 7]
  ],
  [
    [2, 6],
    [3, 20],
    [4, 3]
  ],
  [
    [3, 14]
  ],
  [
    [4, 2]
  ],
  [],
  []
]))