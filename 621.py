from collections import Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # take the task with the most frequency
        # lets say its A
        # A ...gap of n secs.. A ...gap of n secs.. A ...
        # in gap between each A, we can fill it with N unique tasks
        #         c = Counter(tasks)
        #         mostFreqTask = c.most_common()[0][0]
        #         freqOfMostFreqTask = c.most_common()[0][1]
        #         emptySpaces = (freqOfMostFreqTask-1)*n
        #         del c[mostFreqTask]
        #         otherTasksTotal = sum(c.values())
        #         timeStretchOfMostFreqTask = freqOfMostFreqTask + emptySpaces
        #         if otherTasksTotal <= emptySpaces:
        #             return timeStretchOfMostFreqTask
        #         else:

        numberOfTimesToSchedule = Counter(tasks)
        lastScheduled = Counter(tasks)
        # sort last scheduled by frequency
        for key in lastScheduled:
            lastScheduled[key] = None
        t = 1
        while len(numberOfTimesToSchedule) > 0:
            toSchedule = None
            for key in lastScheduled:
                if (lastScheduled[key] == None) or (key in numberOfTimesToSchedule and lastScheduled[key] + n < t):
                    toSchedule = key
                    break
            if toSchedule is None:
                t += 1
                continue
            lastScheduled[toSchedule] = t
            numberOfTimesToSchedule[toSchedule] -= 1
            if numberOfTimesToSchedule[toSchedule] == 0:
                del numberOfTimesToSchedule[toSchedule]
            t += 1
        return t-1

if __name__=="__main__":
    print(Solution().leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"],2))