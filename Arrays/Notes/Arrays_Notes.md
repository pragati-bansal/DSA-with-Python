# 📚 Arrays Notes

## Time Complexity

Access Element:
O(1)

Traversal:
O(n)

Search:
O(n)

Insertion:
O(n)

Deletion:
O(n)

---

## Patterns

### Builder + Scanner

Used in:
- Remove Duplicates
- Remove Element
- Move Zeroes

Template:

```python
i = 0

for j in range(len(nums)):
    if condition:
        nums[i] = nums[j]
        i += 1
```

---

### Left + Right

Used in:
- Reverse Array
- Reverse String
- Two Sum II
- Valid Palindrome

Template:

```python
left = 0
right = len(nums) - 1

while left < right:
    # Action

    left += 1
    right -= 1
```
