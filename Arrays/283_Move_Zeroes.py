LeetCode 283 - Move Zeroes

Pattern:
Builder + Scanner (Two Pointers)

Difficulty:
Easy

Time Complexity:
O(n)

Space Complexity:
O(1)

Algorithm:
1. Keep a builder pointer for the next non-zero position.
2. Traverse the array using a scanner pointer.
3. Whenever a non-zero element is found, swap it with the builder position.
4. Move the builder pointer forward.

Key Learning:
Move all non-zero elements to the front while maintaining their relative order, then all zeroes naturally shift to the end.
"""
  
