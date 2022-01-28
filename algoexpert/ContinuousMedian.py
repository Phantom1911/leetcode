# Do not edit the class below except for
# the insert method. Feel free to add new
# properties and methods to the class.

'''
This is insertion sort based approach (which is still O(n) for the insert method, so it's quite good).
Algoexpert has a heap based approach which we will need to check, and also identify if it does any better than linear time.
'''

class ContinuousMedianHandler:
    def __init__(self):
        # Write your code here.
        self.median = None
		self.nums = []

    def insert(self, number):
		n = len(self.nums)
        if n == 0:
			self.nums.append(number)
			self.median  = number
		else:
			i = n-1
			while i>=0 and self.nums[i] >= number:
				i-=1
			self.nums.insert(i+1, number)
			print("nums is now " ,  self.nums )
			newlen = n+1
			if newlen == 2:
				self.median = (self.nums[0] + self.nums[1]) /2
			elif (newlen) %2==0:
				print("new len is " + str(len(self.nums)))
				self.median = (self.nums[newlen//2] + self.nums[newlen//2 - 1] ) / 2
			else:
				print("in odd block, median " + str(self.nums[newlen//2]))
				self.median = self.nums[newlen//2]

    def getMedian(self):
        return self.median
