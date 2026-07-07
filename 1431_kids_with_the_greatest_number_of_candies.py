
#time complexity = O(n)
#space complexity = O(n)


class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        result = []
#        calculating the maximum of candies in the list
#        it is better to calulate it first than inside the for loop, this makes it efficent
        max_candies = max(candies)
        for candy in candies:
            if candy + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)
        return result
        result = []
