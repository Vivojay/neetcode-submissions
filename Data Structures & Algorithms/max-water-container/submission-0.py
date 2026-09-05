class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = len(heights)
        i = 0
        j = l-1

        m = 0
        while i < j:
            a = min(heights[i], heights[j])*(j-i)
            if a > m: m = a

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return m

