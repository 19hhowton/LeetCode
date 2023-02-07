# LINK: https://leetcode.com/problems/find-smallest-letter-greater-than-target/

def nextGreatestLetter(letters, target):
    lowPoint = 0
    highPoint = len(letters) - 1
    midPoint = (highPoint - lowPoint) // 2

    while lowPoint <= highPoint:
        midPoint = (highPoint + lowPoint) // 2
        letters_midPoint = letters[midPoint]
        if letters[midPoint] == target:
            midPoint = midPoint + 1
            return f"The smallest character that is lexicographically greater than '{target}' in letters is '{letters[midPoint]}'."
        elif letters[midPoint] > target:
            highPoint = midPoint - 1
        else:
            lowPoint = midPoint + 1


letters = ["c", "f", "j", "k", 'l', 'm', 'n']
target = "j"
print(nextGreatestLetter(letters, target))

