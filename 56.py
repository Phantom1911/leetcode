# https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals):
        intervals = sorted(intervals, key=lambda x: (x[0], x[1]))
        i = 0
        while True:
            n = len(intervals)
            if i < n-1:
                self.mergeIntervals(intervals, i)
            else:
                break
            i+=1
        return intervals

    def mergeIntervals(self, intervals, idx):
        if idx == len(intervals) - 1:
            return

        new_interval = [None, None]
        try:

            while intervals[idx][1] >= intervals[idx+1][0]:
                curr_interval = intervals[idx]
                next_interval = intervals[idx + 1]
                new_interval[0] = curr_interval[0]
                new_interval[1] = max(curr_interval[1], next_interval[1])
                intervals.pop(idx)
                intervals.pop(idx)
                intervals.insert(idx, new_interval)
        except IndexError:
            return

if __name__=="__main__":
    s = Solution()
    print(s.merge([[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]))