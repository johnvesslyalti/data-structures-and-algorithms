# question: Contains Duplicate
# difficulty: Easy
# links: [LeetCode](https://leetcode.com/problems/contains-duplicate/), [NeetCode](https://neetcode.io/problems/contains-duplicate)
# tags: [Arrays & Hashing]

# Problem Statement
# Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.
# Example:
# Input: nums = [1,2,3,1]
# Output: true

def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False