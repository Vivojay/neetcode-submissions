class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        h = len(nums) - 1
        min_idx = 0 # min idx

        while True:
            m = l + (h - l) // 2

            # print(nums[l], nums[m], nums[h])
            # print(nums[l:h], nums[l], nums[m], nums[h])

            if nums[l] == nums[m]:
                break

            if nums[m] > nums[h]:
                l = m

            elif nums[m] < nums[h]:
                h = m

            if nums[l] < nums[min_idx]:
                min_idx = l

        # print(nums[l:h], nums[l], nums[m], nums[h])

        if nums[l] > nums[h]:
            min_idx = h
        else:
            min_idx = l

        l = 0
        h = len(nums) - 1

        if target == nums[h]:
            # print(h, nums[h])
            return h
        elif target > nums[h]:
            h = min_idx
        else:
            l = min_idx

        # print()
        while l < h:
            m = l + (h - l) // 2
            if target < nums[m]:
                h = m
            elif target > nums[m]:
                l = m + 1
            else:
                return m

            # k -= 1
            # print(nums[l:h], l, m, h)

        return -1


