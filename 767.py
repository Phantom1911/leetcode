from collections import Counter
import heapq


class Solution:
    def reorganizeString(self, S: str) -> str:
        c = Counter(S)
        heap = []
        for key in c:
            heapq.heappush(heap, (-c[key], key))
        ans = ""
        while heap:
            curr = heapq.heappop(heap)
            curr_freq, curr_char = -curr[0], curr[1]
            if ans == "":
                ans += curr_char
                curr_freq -= 1
                if curr_freq != 0:
                    heapq.heappush(heap, (-curr_freq, curr_char))

            else:
                last_char = ans[-1]
                if curr_char == last_char:
                    if not heap:
                        return ""
                    curr_two = heapq.heappop(heap)
                    curr_two_freq, curr_two_char = -curr_two[0], curr_two[1]
                    ans += curr_two_char
                    curr_two_freq -= 1
                    if curr_two_freq != 0:
                        heapq.heappush(heap, (-curr_two_freq, curr_two_char))
                    heapq.heappush(heap, (-curr_freq, curr_char))
                else:
                    ans += curr_char
                    curr_freq -= 1
                    if curr_freq != 0:
                        heapq.heappush(heap, (-curr_freq, curr_char))

        return ans

if __name__=="__main__":
    print(Solution().reorganizeString("aab"))