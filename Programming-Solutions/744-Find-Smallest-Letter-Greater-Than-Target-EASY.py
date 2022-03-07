"""
https://leetcode.com/problems/find-smallest-letter-greater-than-target/submissions/
"""


def nextGreatestLetter(letters, target):
    if target < letters[0] or target >= letters[-1]:
        return letters[0]

    low, high = 0, len(letters)-1

    while low <= high:
        mid = (low + high) // 2
        if letters[mid] <= target:
            if letters[mid] <= target and mid+1 < len(letters):
                low = mid + 1
                continue
            return letters[mid+1]
        elif letters[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return letters[low]

def main():
    test_cases = [
        [["c", "f", "j"], "a"],
        [["c", "f", "j"], "c"],
        [["c", "f", "j"], "d"],
        [["c", "f", "j"], "j"],
        [["c", "f", "j"], "g"],
        [["e", 'e', "e", "e", "e", "e", "n", "n", "n", "n"], "e"]
    ]
    for letters, target in test_cases:
        print(nextGreatestLetter(letters, target))


if __name__ == '__main__':
    main()
