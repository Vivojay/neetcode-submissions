class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        # h = set(nums)
        d = {nums[i]:i for i in range(l)}
        if len(d) == 0 and 0 in d: return [[0, 0, 0]]
        out = set()

        for i in range(l):
            for j in range(i+1, l):
                s = nums[i] + nums[j]
                if -s in d and d[-s] > j:
                    a = nums[i]
                    b = nums[j]
                    c = -s
                    if a <= b:
                        if b <= c:
                            q = (a, b, c)
                        else:
                            if a <= c:
                                q = (a, c, b)
                            else:
                                q = (c, a, b)
                    else:
                        if a <= c:
                            q = (b, a, c)
                        else:
                            if b <= c:
                                q = (b, c, a)
                            else:
                                q = (c, b, a)


                    # print(q)
                    out.add(q)

        return list(out)

