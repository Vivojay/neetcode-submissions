class Solution:
    def trap(self, height: List[int]) -> int:
        l = len(height)
        lmax = [0]*l
        rmax = [0]*l
        lmax[0] = height[0]
        rmax[l-1] = height[l-1]
        for i in range(1, l):
            j = l - i - 1
            lmax[i] = max(height[i], lmax[i - 1])
            rmax[j] = max(height[j], rmax[j + 1])
            # print(i, j)

        tot = 0
        for i in range(l):
            # if lmax[i] < rmax[i] and height[i] < lmax[i]:
            lowest_max = min(lmax[i], rmax[i])
            a = lowest_max - height[i]
            tot += a

        return tot

