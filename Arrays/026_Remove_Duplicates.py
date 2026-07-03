"""
LeetCode 26 - Remove Duplicates from Sorted Array

Pattern:
Builder + Scanner (Two Pointers)

Difficulty:
Easy

Time Complexity:
O(n)

Space Complexity:
O(1)

Algorithm:

I keep one pointer at the last unique element.
Another pointer scans the array.
Whenever I find a new value, I overwrite the next position.
Finally, I return the count of unique elements.

Key Learning:
Instead of deleting duplicates, overwrite valid elements using two pointers.
"""

class Solution(object):
    def removeDuplicates(self, nums):
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i]=nums[j]

        return i+1
