class Solution:
    def firstDayBeenInAllRooms(self, nextVisit):
        n = len(nextVisit)
        numOfTimesVisited = [0 for i in range(n)]
        # on 0th day, you visit 0th room
        currDay = 0
        numOfTimesVisited[0] = 1
        nextRoom = nextVisit[0]
        while (not self.hasVisitedAllRooms(numOfTimesVisited)):
            currDay += 1
            numOfTimesVisited[nextRoom] += 1
            if numOfTimesVisited[nextRoom] % 2 == 1:
                nextRoom = nextVisit[nextRoom]
            else:
                nextRoom = (nextRoom + 1) % n

        return currDay

    def hasVisitedAllRooms(self, numOfTimesVisited):
        for i in range(len(numOfTimesVisited)):
            if numOfTimesVisited[i] < 1:
                return False

        return True

if __name__ == "__main__":
    print(Solution().firstDayBeenInAllRooms([0,1,2,0]))