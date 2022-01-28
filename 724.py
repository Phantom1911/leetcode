class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        consumleft, consumright = [0 for i in range(len(nums))], [0 for i in range(len(nums))]
        consumleft[0], consumright[-1] = nums[0], nums[-1]
        for i in range(1, len(nums)):
            consumleft[i] = consumleft[i - 1] + nums[i]
        for i in range(len(nums) - 2, -1, -1):
            consumright[i] = consumright[i + 1] + nums[i]
        for i in range(0, len(nums)):
            consumleft[i] = consumleft[i] - nums[i]
            consumright[i] = consumright[i] - nums[i]
        for i in range(0, len(nums), 1):
            if consumright[i] == consumleft[i]:
                return i

        return -1