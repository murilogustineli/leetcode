"""
https://leetcode.com/problems/roman-to-integer/
"""


def romanToInt(s: str) -> int:
    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    # temp array to store the values of each symbol from dictionary
    values = [dict[i] for i in s]
    output, i = 0, 0

    # Loop though temp array
    while i < len(values):
        # If i == last index of elements in temp array, return total output + element
        if i == len(values)-1:
            return output + values[i]
        # If next element is greater than current element, subtract next element with current, and skip next element
        elif values[i+1] > values[i]:
            output += values[i+1] - values[i]
            i += 2
        # Otherwise, add element to output
        else:
            output += values[i]
            i += 1
    return output


if __name__ == '__main__':
    test_cases = [
        ('I'),
        ('III'),
        ('IX'),
        ('XIV'),
        ('XXIV'),
        ('LVIII'),
        ('MCMXCIV')
    ]
    for roman in test_cases:
        print(romanToInt(roman))
