class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elements = {}
        result = []
        for i in nums:
            if i not in elements:
                elements[i] = 0
            elements[i] += 1
        for i in range(k):
            max_key = max(elements, key=elements.get)
            result.append(max_key)
            del elements[max_key]
        return result