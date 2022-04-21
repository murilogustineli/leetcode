"""
https://leetcode.com/problems/add-two-numbers/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Converting a list to a linked list
def lst2link(lst):
    cur = dummy = ListNode(0)
    for e in lst:
        cur.next = ListNode(e)
        cur = cur.next
    return dummy.next


# Adding numbers of two linked lists
def addTwoNumbers(l1, l2):
    ans = []
    dummy = cur = ListNode(0)
    carry = 0
    while l1 or l2 or carry:
        if l1:
            carry += l1.val
            l1 = l1.next
        if l2:
            carry += l2.val
            l2 = l2.next
        cur.next = ListNode(carry % 10)
        cur = cur.next
        carry //= 10
        ans.append(cur.val)
    return dummy.next, ans


def main():
    test_cases = [
        [[2, 4, 3], [5, 6, 4]],
        [[0], [0]],
        [[9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]]
    ]
    for i, j in test_cases:
        l1 = lst2link(i)
        l2 = lst2link(j)

        # Print results
        obj, ans = addTwoNumbers(l1, l2)
        print(ans)


if __name__ == '__main__':
    main()
