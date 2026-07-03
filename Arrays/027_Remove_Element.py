"""
LeetCode 27 - Remove Element

Pattern:
Builder + Scanner (Two Pointers)

Difficulty:
Easy

Time Complexity:
O(n)

Space Complexity:
O(1)

Algorithm:
1. Keep a builder pointer (i) at the beginning.
2. Traverse the array using a scanner pointer (j).
3. If nums[j] is not equal to val, overwrite nums[i] with nums[j].
4. Move the builder pointer forward.
5. Return the count of remaining elements.

Key Learning:
Instead of deleting elements from the array, overwrite the valid elements while scanning the array.
"""

class Solution(object):
    def removeElement(self, nums, val):
        i=0
        for j in range(0,len(nums)):
            if nums[j]!=val:
                nums[i]=nums[j]
                i+=1
        return i
