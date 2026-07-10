

#time complexity = O(n) =>because we went through the list of flowerbed
#space complexity = O(1) =>because we did not create any array, list or anything as the result

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        count  = 0
        length = len(flowerbed)
        for i in range(length):
            if flowerbed[i] == 0:
                left_empty = (i== 0) or (flowerbed[i-1] == 0 )
                right_empty = (i == length-1) or (flowerbed[i+1] == 0)
                if left_empty and right_empty:
                   flowerbed[i] = 1
                   count += 1
                
        return count >= n
# here n is the number of flowers given to us and count is the number of flowers we could plant.
# if we could place flowers less than given to us then return False otherwise True. 


