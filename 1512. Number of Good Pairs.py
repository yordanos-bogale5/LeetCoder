class Solution:
    def numIdenticalPairs(self, nums):
        count = [0] * 101  # As per the constraints, nums[i] <= 100
        result = 0

        for num in nums:
            result += count[num]
            count[num] += 1

        return result

