from collections import deque
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        # print(id)
        idMap = {e.id : e for e in employees}
        node = idMap[id]
        ans = 0
        q = deque()
        q.append(node)
        while q:
            curr = q.popleft()
            ans += curr.importance
            for child in curr.subordinates:
                childNode = idMap[child]
                q.append(childNode)
        return ans