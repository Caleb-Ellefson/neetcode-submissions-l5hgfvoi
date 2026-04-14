class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        curr = 0
        max_val = 0

        for i in range(len(nums)):
            if  nums[i] == 1:
                curr+=1
                if curr > max_val:
                    max_val = curr
            else:
                curr = 0
        return max_val