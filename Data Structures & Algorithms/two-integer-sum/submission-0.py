class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_vals = {}
        result = []
        for i in range(len(nums)):
            curr = target - nums[i]
            if curr in prev_vals:
                result.append(prev_vals[curr])
                result.append(i)
                return result
            else:
                prev_vals[nums[i]] = i