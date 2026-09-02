class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxone = 0
        count = 0
        for i in nums:
            if i == 1:
                count += 1
                maxone = max(maxone, count)
            else:
                count = 0
        return maxone            
        