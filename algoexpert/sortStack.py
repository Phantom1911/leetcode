def sortStack(stack):
    if len(stack) <= 1:
		return stack
	top = stack[-1]
	remSorted = sortStack(stack[:-1])
	removed = []
	while len(remSorted) > 0 and top < remSorted[-1]:
		removed.append(remSorted[-1])
		del remSorted[-1]
	remSorted.append(top)
	return (remSorted + list(reversed(removed)))
