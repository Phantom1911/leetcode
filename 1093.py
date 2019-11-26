class Solution:
    def sampleStats(self, count):
        sample = []
        total_sum = 0
        for i in range(len(count)):
            curr_count = count[i]
            total_sum += curr_count * i
            while curr_count > 0:
                sample.append(i)
                curr_count -= 1
        ans = []
        ans.append(float(min(sample)))
        ans.append(float(max(sample)))
        ans.append(float(total_sum / len(sample)))
        if len(sample) % 2 != 0:
            ans.append(float(sample(len(sample) / 2)))
        else:
            index = len(sample) // 2
        index2 = len(sample) + 1 // 2
        ans.append(float((sample[index] + sample[index2]) / 2))
        max_count = max(count)
        ans.append(float(count.index(max_count)))
        return ans


