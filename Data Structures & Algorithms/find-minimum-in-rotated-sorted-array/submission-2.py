class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        h = len(nums)-1

        while True:
            m = l+(h-l)//2

            if nums[m] == nums[l]:
                break

            if nums[m] < nums[h]:
                h = m
            elif nums[m] > nums[h]:
                l = m

        out = nums[h]
        if nums[h] > nums[l]:
            out = nums[l]
        return out
