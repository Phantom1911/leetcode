def getPermutations(array):
    # Write your code here.
    if array is None or len(array) == 0:
        return array
    if len(array) == 1:
        return [[array[0]]]
    first_ele = array[0]
    print("first el is ", first_ele)
    roa = array[1:]
    print("roa is ", roa)
    rec_res = getPermutations(roa)
    print("rec res is ", rec_res)
    ans = []
    for item in rec_res:
        my_item = [item[i] for i in range(len(item))]
        print("my item is ", my_item)
        for i in range(len(item)+1):
            print("i is ", i)
            my_item.insert(i, first_ele)
            print("my item is now ", my_item)
            ans.append(my_item)
    return ans


if __name__ == "__main__":
    print(getPermutations([1, 2]))
