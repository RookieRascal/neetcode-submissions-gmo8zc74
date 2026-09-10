class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        aone = 0
        ount = 0
        for i in nums:
            if i == 1:
                ount += 1
                aone = max(aone, ount)
            else:
                ount = 0    
        return aone    


        