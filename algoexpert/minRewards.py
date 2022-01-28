def minRewards(scores):
    ltor = [1 for i in range(len(scores))]
    rtol = [1 for i in range(len(scores))]
    for i in range(len(scores) - 1):
        if scores[i + 1] > scores[i]:
            ltor[i + 1] = ltor[i] + 1
    # print(ltor)
    for i in range(len(scores) - 1, 0, -1):
        if scores[i - 1] > scores[i]:
            rtol[i - 1] = rtol[i] + 1
    # print(rtol)
    finalCandies = [1 for i in range(len(scores))]
    for i in range(len(scores)):
        finalCandies[i] = max(ltor[i], rtol[i])
    ans = 0
    for i in range(len(finalCandies)):
        ans += finalCandies[i]
    # print("hiii")
    # print(finalCandies)
    return ans

