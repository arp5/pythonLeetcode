class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n,m = len(matrix),len(matrix[0])
        ans = []
        rs,re = 0,n
        cs,ce = 0,m
        while len(ans)<m*n:
            for j in range(cs,ce):
                ans.append(matrix[rs][j])
                if len(ans)==m*n:
                    return ans
            rs+=1
            for i in range(rs,re):
                print(ce)
                ans.append(matrix[i][ce-1])
                if len(ans)==m*n:
                    return ans
            ce-=1
            for j in reversed(range(cs,ce)):
                ans.append(matrix[re-1][j])
                if len(ans)==m*n:
                    return ans
            re-=1
            for i in reversed(range(rs,re)):
                ans.append(matrix[i][cs])
                if len(ans)==m*n:
                    return ans
            cs+=1
        print(ans)
        return ans