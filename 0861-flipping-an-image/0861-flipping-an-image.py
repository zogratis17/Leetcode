class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        r = len(image)
        c = len(image[0])
        
        for i in range(r):
            for j in range(c):
                if image[i][j] == 0 :
                    image[i][j] = 1
                else:
                    image[i][j] = 0
        
        for i in range(r):
            image[i].reverse()
            
        return image