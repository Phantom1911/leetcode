# https://www.hackerrank.com/challenges/counting-valleys/problem

# careful : check for prev_current_level is necessary, otherwise you'll get total of all valleys and peaks both

def countingValleys(steps, path):
    # Write your code here
    current_level = 0
    valleys = 0
    for i in range(steps):
        prev_current_level = current_level
        if path[i] == 'U':
            current_level += 1
        else: current_level -=1
        if current_level == 0 and prev_current_level == -1:
            valleys += 1
    return valleys
