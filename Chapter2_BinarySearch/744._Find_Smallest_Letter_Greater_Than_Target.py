# LINK: https://leetcode.com/problems/find-smallest-letter-greater-than-target/

def nextGreatestLetter(letters, target):
    lowPoint = 0
    highPoint = len(letters) - 1

    while lowPoint <= highPoint:
        midPoint = (highPoint + lowPoint) // 2

        if letters[midPoint] == target:

        elif letters[midPoint] < target:
            lowPoint = midPoint + 1
        else:
            highPoint = midPoint - 1

    return -1




letters = ["c", "f", "j"]
target = "z"
print(nextGreatestLetter(letters, target))
target = "d"
print(nextGreatestLetter(letters, target))
letters = ["e","e","g","g","g","g"]
target = "g"
print(nextGreatestLetter(letters, target))
target = "e"
print(nextGreatestLetter(letters, target))


