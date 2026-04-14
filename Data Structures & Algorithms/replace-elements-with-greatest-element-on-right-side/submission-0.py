class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        max_len = len(arr)

        for i in range(max_len - 1):
            curr_max = -1
            for j in range(i + 1, max_len):
                if curr_max < arr[j]:
                    curr_max = arr[j]

                arr[i] = curr_max

        arr[max_len - 1] = -1
        return arr
