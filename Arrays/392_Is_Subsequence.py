"""
LeetCode 392 - Is Subsequence

Pattern:
Same Direction Two Pointers

Difficulty:
Easy

Time Complexity:
O(n)

Space Complexity:
O(1)

Algorithm:
1. Keep one pointer on the subsequence (s).
2. Keep another pointer on the main string (t).
3. If both characters match, move both pointers.
4. Otherwise, move only the pointer on the main string.
5. If all characters in the subsequence are matched, return True.
6. Otherwise, return False.

Key Learning:
Two pointers don't always move together. When searching for a subsequence, keep advancing through the larger string until the current character is found.

"""
class Solution(object):
    def isSubsequence(self, sub, seq):
        l=0
        r=0
        if len(sub)==0:
            return True
        while r<len(seq):                
            if sub[l] ==seq[r]:   
                l+=1
                r+=1
                if l==len(sub):
                    return True
            else:
                r+=1
        return False
        
        
     
