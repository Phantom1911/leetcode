class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        killed = [False for i in range(n)]
        # print(toKill(killed, [0], n, 0, k))
        return toKill(killed, [0], n, 0, k) + 1


def toKill(killed, killedNum, n, currIdx, k):
    if killedNum[0] == n - 1:
        # only one member is surviving now
        return getWinner(killed)
    killIdx = getKillIdx(currIdx, k, killed, n)
    killed[killIdx] = True
    nextIdx = getNextSurvivingIdx(killed, killIdx, n)
    killedNum[0] += 1
    return toKill(killed, killedNum, n, nextIdx, k)

def getKillIdx(currIdx, k, killed, n):
    count = 0
    nextIdx = currIdx
    while count < k-1:  # curr person is also counted
        nextIdx = (nextIdx + 1) % n
        if killed[nextIdx] == False:
            count+=1
    return nextIdx

def getNextSurvivingIdx(killed, killIdx, n):
    i = (killIdx + 1)%n
    while killed[i] == True:
        i = (i + 1) % n
    return i

def getWinner(killed):
    for i in range(len(killed)):
        if killed[i] == False:
            return i
    return -1

if __name__=="__main__":
    print(Solution().findTheWinner(6,5))