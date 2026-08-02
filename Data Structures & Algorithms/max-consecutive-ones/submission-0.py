class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        co = 0
        xc = 0
        for i in nums:
            if i == 1:
                co += 1
                xc = max(xc, co)
            else:
                co = 0    
        return xc    
        