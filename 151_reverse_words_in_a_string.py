
#Time: O(n) — split, reverse, and join each pass through all n characters once.
#Space: O(n) — each step creates a new list/string holding roughly all n characters.

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        words.reverse()
        return " ".join(words)
        
