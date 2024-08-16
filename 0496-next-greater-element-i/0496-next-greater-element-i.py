class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numset = {}
        for i,num in enumerate(nums2):
            numset[num] = i
        stack = []
        ans= [-1]*len(nums2)
        for i,num in enumerate(nums2):
            while stack and num>stack[-1][1]:
                x,e = stack.pop()
                ans[x] = num
            stack.append((i,num))
        print(ans)
        ne = [-1]*len(nums1)
        for i,num in enumerate(nums1):
            ne[i] = ans[numset[num]] 
        return ne
