# Day 0: Two Sum (LeetCode #1)

## 🎯 Today’s Focus
- **Problem**: Two Sum  
- **Goal**: Compare naïve vs. optimized solutions  

## 📚 Learn (15 min)
1. **Brute-Force**  
   - Check each pair `(i,j)` for sum == target  
   - Time: O(n²), Space: O(1)

2. **Hash Map**  
   - Store seen values and look up complement  
   - Time: O(n), Space: O(n)

## 🔧 Patterns (30 min)
```python
def has_duplicate(arr):
    seen = set()
    for x in arr:
        if x in seen:
            return True
        seen.add(x)
    return False
```

- **When to use**: Large n, need O(n) performance  
- **Key insight**: Trade extra space for constant-time lookup  

## 🎬 Resource (20 min)
- **Watch**: NeetCode “Two Sum”  
- **Read**: Python dict docs on docs.python.org  
- **Practice**: LeetCode #1  

## 💼 Interview Key (5 min)
- **Q**: “What’s the time/space trade-off between approaches?”  
- **A**:  
  - Brute-force: O(n²) time, O(1) space  
  - Hash map: O(n) time, O(n) space  

## ✅ Done
- [ ] Implement both functions  
- [ ] Run example tests  
- [ ] Commit changes  

## Notes
for the general Two Sum problem (with arbitrary unsorted input) the two-pointer technique alone can’t be applied without additional work, because it requires a sorted array or two ends you can move inward.

Here’s the rundown:
1. Two Pointers only works if the array is sorted
2. After sorting, you lose the original indices.
3. You could sort a list of (value,index) pairs, but that adds O(n log n) time and still uses O(n) extra space to track indices.

### Trade-offs
1. Brute-force: O(n²) time, O(1) extra space
2. ash-map: O(n) time, O(n) space
3. Sort + Two pointers: O(n log n) time, O(n) space

When Two Pointers Is Viable
If the input is already sorted (or if you only need to know the values, not the original indices), you can do:

```python
def two_sum_sorted(nums, target):
    # nums is sorted
    left, right = 0, len(nums)-1
    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            return [left, right]
        if s < target:
            left += 1
        else:
            right -= 1
    return []
```
But for LeetCode #1 you must return the original positions in the unsorted list, so this isn’t directly applicable unless you track indices through sorting.

### Conclusion
Hash-map approach remains the optimal O(n) time, O(n) space solution for the general Two Sum problem.

Two pointers help only when the array is already sorted or if you’re allowed to return sorted indices rather than original positions.
