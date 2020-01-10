def powerset(array):
    # Write your code here.
    ans = [[]]
    for ele in array:
        n = len(ans)
        for i in range(n):
            arr = ans[i]
            temp = arr[::]
            temp.append(ele)
            ans.append(temp)
    return ans


if __name__ == "__main__":
    print(powerset([1, 2, 3]))



