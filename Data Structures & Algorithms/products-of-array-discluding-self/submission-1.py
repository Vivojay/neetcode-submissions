class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        pre = [1]*l
        post = [1]*l

        pre[0] = nums[0]
        post[l-1] = nums[l-1]

        for i in range(1, l):
            pre[i] = pre[i-1] * nums[i]
            # print(' ', pre, i, pre[i-1], nums[i])
            post[l-i-1] = post[l-i] * nums[l-i-1]

        out = [post[1]] + [0]*(l-1)
        for i in range(1, l):
            if i == 0:
                out[i] = post[i+1]
            elif i == l-1:
                out[i] = pre[i-1]
            else:
                out[i] = pre[i-1] * post[i+1]

        return out
