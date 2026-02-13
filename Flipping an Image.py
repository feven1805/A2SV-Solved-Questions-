class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(image)
        cols = len(image[0])
        img2 = []
        for row in range(rows):
            image[row].reverse()
            img2.append(image[row])
        print(img2)
        rows2 = len(img2)
        cols2 = len(img2[0])
        for row in range(rows2):   
            for col in range(cols2):
                if img2[row][col] == 1:
                      img2[row][col] = 0
                else:
                    img2[row][col] = 1   
        return img2
        
