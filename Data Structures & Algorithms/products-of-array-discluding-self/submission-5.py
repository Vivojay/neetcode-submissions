class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        pre = [nums[0]] + [1]*(l-1)
        post = [1]*(l-1) + [nums[l-1]]

        # pre[0] = nums[0]
        # post[l-1] = nums[l-1]

        for i in range(1, l):
            pre[i] = pre[i-1] * nums[i]
            post[l-i-1] = post[l-i] * nums[l-i-1]

        out = [post[1]] + [0]*(l-2) + [pre[i-1]]
        for i in range(1, l-1):
            out[i] = pre[i-1] * post[i+1]

        return out
