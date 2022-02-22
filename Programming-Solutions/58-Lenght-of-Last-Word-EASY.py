"""
https://leetcode.com/problems/length-of-last-word/
"""


def lengthOfLastWord(s: str) -> int:
    # Split string by blank spaces and reverse string
    split = s.split(' ')[::-1]

    # Iterate over the string list
    for i in range(len(split)):
        # Keep iterative over blank space until find a word
        if len(split[i]) < 1:
            continue
        # Return length of the word
        else:
            return len(split[i])


# Simple solution using strip()
def lengthOfLastWordSimple(s: str) -> int:
    s = s.strip().split()
    return len(s[-1])


# Main function with test cases
def main():
    strings = [
        'Hello World',
        "   fly me   to   the moon  ",
        "luffy is still joyboy"
        ]
    for s in strings:
        print(lengthOfLastWord(s), lengthOfLastWordSimple(s))


# Call main function
if __name__ == '__main__':
    main()
    
