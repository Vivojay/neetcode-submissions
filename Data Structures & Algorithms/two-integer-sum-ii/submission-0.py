class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = len(numbers)
        i = 0
        j = l - 1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
            if numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1

        return [i+1, j+1]
