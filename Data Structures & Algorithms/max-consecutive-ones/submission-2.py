class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        a = 0
        ca = 0
        for i in nums:
            if i == 1:
                ca += 1
                a = max(ca, a)
            else:
                ca = 0    
        return a