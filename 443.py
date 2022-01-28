from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        i,s = 0,""
        while i < len(chars):
            currchar = chars[i]
            j = i+1
            while j<len(chars) and chars[j] == currchar:
                j += 1
            occ = j - i
            if occ > 1:
                s += (currchar+str(occ))
            else:
                s += currchar
            i = j
        for i in range(len(s)):
            chars[i] = s[i]
        return len(s)