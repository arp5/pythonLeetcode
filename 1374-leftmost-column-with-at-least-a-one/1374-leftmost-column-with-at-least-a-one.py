# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        n,m = binaryMatrix.dimensions()
        mincol = float('inf')
        for i in range(n):
            #check bin search on each row
            row = i
            start,end = 0,m-1
            if not binaryMatrix.get(row,end):
                continue
            while start<=end:
                mid = (start+end)//2
                if binaryMatrix.get(row,mid):
                    end = mid
                else:
                    start = mid+1
                if start==end:
                    mincol = min(start,mincol)
                    break
        return mincol if mincol != float('inf') else -1