class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        h = set(nums)

        m = 0
        for i in h:
            s = 0
            if i-1 not in h:
                x = i
                while x in h:
                    s += 1
                    x += 1
                # s = 5
            if m < s: m = s

        # print(m, h)

        return m


