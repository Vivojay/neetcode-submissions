class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x = set()
        for num in nums:
            x.add(num)
        # print(x, nums)
        return len(x) != len(nums)
