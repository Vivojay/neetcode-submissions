class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        l = len(nums)
        nums.sort()
        # for i in range(l)

        # j = 0
        out = [nums[0]]
        for i in range(1, l):
            if nums[i] != nums[i-1]:
                out.append(nums[i])

        s = 1
        max_s = 1
        for i in range(1, len(out)):
            if out[i] == out[i-1]+1:
                s+=1
                if s > max_s: max_s = s
            else:
                s = 1

        return max_s

