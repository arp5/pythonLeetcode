class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        start,end = 0,n-1
        while start<end:
            cursum = numbers[start]+numbers[end]
            if cursum==target:
                return [start+1,end+1]
            elif cursum>target:
                end-=1
            else:
                start+=1
        return [-1,-1]