class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc]==color:
            return image
        ogcolor = image[sr][sc]
        queue = [(sr,sc)]
        n,m = len(image), len(image[0])
        while queue:
            x,y = queue.pop(0)
            image[x][y] = color
            if x-1>=0 and image[x-1][y]==ogcolor:
                queue.append((x-1,y))
            if x+1<n and image[x+1][y]==ogcolor:
                queue.append((x+1,y))
            if y-1>=0 and image[x][y-1]==ogcolor:
                queue.append((x,y-1))
            if y+1<m and image[x][y+1]==ogcolor:
                queue.append((x,y+1))
        return image

