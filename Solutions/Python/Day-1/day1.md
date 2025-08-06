# 📅 Day 1: Contains Duplicate (LeetCode #217)

## 🎯 Today's Focus
- **Problem:** Contains Duplicate (#217)
- **Pattern:** Detecting duplicates — from brute-force to hashing
- **Key Goals:** Learn multiple approaches (naïve, sorting, hashing)

## 📚 Learn (Brief Theory)

- **Duplicates**: The classic check — “Is there a repeated number in this list?”
- **Brute-force**: Just compare all pairs. Works but slow: O(n²) time, O(1) space.
- **Sorting**: If sorted, duplicates are adjacent! O(n log n) time for sorting, and O(1) space.
- **Hash Set**: Hash sets store seen elements for O(1) average lookup, giving O(n) time and O(n) space.

## 🔧 Patterns & Solution Approaches

### 1. Brute-Force (Nested Loops)
```python
def contains_duplicate_bruteforce(nums):
    """
    O(n^2) time, O(1) space.
    Compares each pair of elements.
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True
    return False
```
- **When to use:** Very small datasets or for understanding baseline.

### 2. Sorting & Adjacent Scan
```python
def contains_duplicate_sorted(nums):
    """
    O(n log n) time, O(1) extra space (not counting sort).
    Sort, then compare neighbors.
    """
    nums = sorted(nums)  # don't modify input!
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return True
    return False
```
- **Pro:** No extra set/dict needed.
- **Con:** Destroys input or needs to copy; O(n log n) time.

### 3. Hash Set (Optimal for Interview)
```python
def contains_duplicate_set(nums):
    """
    O(n) time, O(n) space.
    Track 'seen' elements in a set.
    """
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
```
- **When to use:** Most practical and expected in interviews[1][2][3].
- **Key insight:** Set lookup/add is O(1) on average.

### 4. Pythonic One-Liner
```python
def contains_duplicate_oneliner(nums):
    return len(set(nums)) < len(nums)
```
- **Pro:** Simple and elegant for real-world code reviews[2].

## 🎬 Resources

- **Explainer Video:** [NeetCode LeetCode 217: Contains Duplicate (Python)](https://www.youtube.com/watch?v=3OamzN90kPg)[4]
- **In-depth Written Walkthrough:** [AlgoMonster Explanation](https://algo.monster/liteproblems/217)[2]
- **Extra:** [NeetCode 150 Day 1 Walk-along](https://www.youtube.com/watch?v=nPbIbXdZJjk)[5]

## 💼 Interview Key

- “Start with the brute-force; then how do you optimize?”
- Use the hash set to bring O(n^2) → O(n) time at the cost of O(n) space.
- “What if you can’t use extra space?” → Sort and compare adjacent elements.

**Edge Cases to Test:**
- Empty list, all unique, all same, only two elements, negative numbers.

## ✅ Done Checklist

- [ ] Implemented all three approaches (brute-force, sorted, set) in `day-1-contains-duplicate.py`
- [ ] Explained tradeoffs in `day-1.md`
- [ ] Watched explainer video
- [ ] Committed code & notes

