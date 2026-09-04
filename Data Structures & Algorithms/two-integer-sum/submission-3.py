class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {nums[i]: i for i in range(len(nums))}
        print(s)
        for j, x in enumerate(nums):
            diff = target-x
            print(diff)
            if diff in s:
                i = s[diff]
                if j == i:
                    continue
                if j < i:
                    return [j, i]
                return [i, j]

