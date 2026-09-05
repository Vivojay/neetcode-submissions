class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        h = set(nums)
        m = 1 # max
        for i in nums:
            s = 0
            if (i-1) in h:
                continue

            x = i
            while x in h:
                s += 1
                x += 1
                if m < s: m = s
        return m
