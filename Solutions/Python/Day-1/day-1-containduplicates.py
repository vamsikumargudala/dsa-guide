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

def contains_duplicate_oneliner(nums):
    return len(set(nums)) < len(nums)

if __name__ == "__main__":
    example = [1, 2, 3, 4, 5, 1]
    print("Brute Force: ", contains_duplicate_bruteforce(example))  # True
    print("Sorted:      ", contains_duplicate_sorted(example))      # True
    print("Set:         ", contains_duplicate_set(example))         # True
    print("One-liner:   ", contains_duplicate_oneliner(example))     # True

    example_no_duplicates = [1, 2, 3, 4, 5]
    print("Brute Force: ", contains_duplicate_bruteforce(example_no_duplicates))  # False
    print("Sorted:      ", contains_duplicate_sorted(example_no_duplicates))      # False
    print("Set:         ", contains_duplicate_set(example_no_duplicates))         # False
    print("One-liner:   ", contains_duplicate_oneliner(example_no_duplicates))     # False