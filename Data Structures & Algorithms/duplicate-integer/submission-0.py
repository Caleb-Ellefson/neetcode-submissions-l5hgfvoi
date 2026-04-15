class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_list = frozenset(nums)
        if len(new_list) != len(nums):
            return True
        return False