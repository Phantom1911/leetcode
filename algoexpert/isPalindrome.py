def isPalindrome(string):
    # Write your code here.
	i,j = 0, len(string)-1
	while(i<j):
		if string[i] != string[j]:
			return False
		i+=1
		j-=1
	return True
