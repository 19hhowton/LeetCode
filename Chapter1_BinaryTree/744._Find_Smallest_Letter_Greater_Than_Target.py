# LINK: https://leetcode.com/problems/find-smallest-letter-greater-than-target/

def nextGreatestLetter(letters, target):
    lowPoint = 0
    highPoint = len(letters) - 1

    while lowPoint <= highPoint:
        midPoint = (highPoint + lowPoint) // 2
        letters_midPoint = letters[midPoint]

        if letters[midPoint] == target:

            # return f"The smallest character that is lexicographically greater than '{target}' in letters is '{letters[midPoint]}'."
            counter = 0
            for i in letters[midPoint + 1:]:
                # see if there are more of the same letter
                if i == target:
                    counter += 1
            midPoint = counter + midPoint

            #if this new midPoint is the highest number, then return letter[0]
            if letters[midPoint] == len(letters) - 1:
                return letters[0]
            #otherwise, return this midPoint +1
            return letters[midPoint + 1]


        elif letters[midPoint] > target:
            highPoint = midPoint - 1
        else:
            lowPoint = midPoint + 1

    if lowPoint == len(letters):
        # then there is no letter higher than the target
        return letters[0]
    else:
        # lowPoint = highpoint meaning the letter would be inbetween
        return letters[lowPoint]


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


