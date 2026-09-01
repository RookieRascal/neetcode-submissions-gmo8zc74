class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ao = 0
        co = 0
        for i in nums:
            if i == 1:
                co += 1
                ao = max(co, ao)
            else:
                co = 0
        return ao            
        