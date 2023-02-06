# LINK: https://leetcode.com/problems/search-insert-position/

def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int

    What did I learn?
    How do I set up code when I want to check again? Iteration bb :)

    # find the index of the item in the middle of the list
    # if idx number == target, return idx
    # if idx number > target, get new idx by dividing the current idx by 2 and start from beginning
    # if idx number < target, get new idx by dividing the current idx by 2 and adding with the previous idx and start from beginning

    """
    # binary tree
    stillChecking = True
    # idx is middle number. If no middle, upper middle number
    idx = int((len(nums) // 2))

    while stillChecking:

        if nums[idx] == target:
            return idx

        if idx == len(nums) - 1:
            return len(nums)

        if target > nums[idx] and target < nums[idx + 1]:
            return idx + 1

        if idx == 0:
            return idx

        # > then LowMidPoint
        elif target < nums[idx]:
            idx = int(len(nums[:idx]) // 2)

        # < then HighMidPoint
        elif target > nums[idx]:
            idx = int(len(nums[idx:]) // 2) + idx


nums = [1, 3, 5, 7]
target = 2
print(searchInsert(nums, target))