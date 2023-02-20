# LINK: https://leetcode.com/problems/reverse-linked-list/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def reverseList(self, head):
        prev = None
        current = head

        return current.next

# start with the head element and assign 1-pointer to 2, repeat until last element in the linked list
# return the linked list



head = [1,2,3,4,5]
print(reverseList(head))
