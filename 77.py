class Solution:
    def combine(self, n: int, k: int) :
        arr = [i for i in range(1, n + 1, 1)]
        return self.getcombinations(arr, k)

    def getcombinations(self, arr, k):
        if len(arr) == 0:
            return []
        if k == 1:
            return [[arr[i]] for i in range(len(arr))]
        currcombns = []
        for i in range(len(arr)):
            remcombns = self.getcombinations(arr[:i] + arr[i + 1:], k - 1)
            for comb in remcombns:
                if sorted([arr[i]]+(comb)) not in currcombns:
                    currcombns.append(sorted([arr[i]]+(comb)))
        return currcombns

if __name__=="__main__":
    print(Solution().combine(4,2))