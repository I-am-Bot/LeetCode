"""
Given an integer array nums, return the number of elements that have both a strictly smaller and a strictly greater element appear in nums.

 

Example 1:

Input: nums = [11,7,2,15]
Output: 2
Explanation: The element 7 has the element 2 strictly smaller than it and the element 11 strictly greater than it.
Element 11 has element 7 strictly smaller than it and element 15 strictly greater than it.
In total there are 2 elements having both a strictly smaller and a strictly greater element appear in nums.
Example 2:

Input: nums = [-3,3,3,90]
Output: 2
Explanation: The element 3 has the element -3 strictly smaller than it and the element 90 strictly greater than it.
Since there are two elements with the value 3, in total there are 2 elements having both a strictly smaller and a strictly greater element appear in nums.
"""
class Solution:
    def countElements(self, nums) -> int:
        return max(0, len(nums) - nums.count(min(nums)) - nums.count(max(nums)))


"""
Time O(N)
Space O(1)
"""

