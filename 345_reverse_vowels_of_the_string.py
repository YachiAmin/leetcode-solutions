#time complexity = O(n) => beacuse the loops are not nested, they are n+n+n = 3n but overall that will be O(n)
#space complexity = O(n) => because we created a list inside the program 


class Solution(object):
    def reverseVowels(self, s):
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        
        s_list = list(s)
        
        found_vowels = []
        positions = []
        
        for i in range(len(s_list)):
            if s_list[i] in vowels:
               found_vowels.append(s_list[i])
               positions.append(i)
        
        found_vowels.reverse()
        for k in range(len(positions)):
          s_list[positions[k]] = found_vowels[k]
        return "".join(s_list)
