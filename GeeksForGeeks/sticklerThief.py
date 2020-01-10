def maxLoot(array, index, memoize):
    n = len(array)
    if memoize[index] != -1:
        return memoize[index]
    memoize[index] =  max(array[index]+maxLoot(array,index-2,memoize), maxLoot(array,index-1,memoize))
    return memoize[index]

if __name__=="__main__":
    array = [5,5,10,100,10,5]
    memoize = [-1 for i in range(6)]
    memoize[0] = array[0]
    memoize[1] = max(array[0], array[1])
    n = len(array)
    print(maxLoot(array, n-1, memoize ))