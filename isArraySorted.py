class isArraySorted:
    def isSorted(self, arr,i):
        if i == len(arr)-1:
            return True
        elif arr[i] <= arr[i+1]:
            return self.isSorted(arr, i+1)
        else:
            return False

if __name__=="__main__":
    s = isArraySorted()
    print(s.isSorted([1,2,0], 0))