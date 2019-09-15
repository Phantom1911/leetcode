class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        ans = []
        for hrs in range(12):
            for mins in range(60):
                if bin(hrs).count('1')+bin(mins).count('1')==num:
                    if mins < 10:
                        mins = '0'+str(mins)
                    time = str(hrs)+":"+str(mins)
                    ans.append(time)
        return ans