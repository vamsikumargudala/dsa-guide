# Day 0: Two Sum (LeetCode #1)

def two_sum_bruteforce(nums, target):
    """
    Naïve Approach: Check every pair
    Time: O(n²), Space: O(1)
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

def two_sum_hashmap(nums, target):
    """
    Optimized Approach: Single pass with hash map
    Time: O(n), Space: O(n)
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

if __name__ == "__main__":
    example = [2, 7, 11, 15]
    print("Brute Force:", two_sum_bruteforce(example, 9))    # [0, 1]
    print("Hash Map:   ", two_sum_hashmap(example, 9))      # [0, 1]
