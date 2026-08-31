class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        i = set()
        for n in nums:
            if n in i:
                return True
            else:
                i.add(n)  
        return False            
        