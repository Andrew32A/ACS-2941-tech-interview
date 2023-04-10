# *******************************************************************************
# Question

# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

# You may not alter the values in the list's nodes, only nodes themselves may be changed.

# Example 1:
# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]

# Example 2:
# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]

# *******************************************************************************
# Solution 1

# 1. Create a helper function called "reverseLinkedList" that takes in a head node and returns the new head of the reversed linked list.
# 2. Create a new head node called "newHead" and set it equal to None.
# 3. Create a variable called "tail" and set it equal to None.
# 4. Create a variable called "current" and set it equal to the original head node.
# 5. Create a variable called "count" and set it equal to 0.
# 6. Loop through the linked list and perform the following steps:
    # a. Increment the "count" variable by 1.
    # b. If the count is equal to k, perform the following steps:
    # i. Call the "reverseLinkedList" helper function on the current sublist.
    # ii. Set the "newHead" variable equal to the result of the "reverseLinkedList" function if it's the first sublist being reversed, otherwise, connect the "tail" node of the previous sublist to the "newHead" of the current sublist.
    # iii. Set the "tail" variable equal to the current node.
    # iv. Reset the "count" variable to 0.
    # c. Move to the next node in the linked list.
# 7. If there are any remaining nodes in the linked list, connect the "tail" node to the "newHead" node of the last sublist.
# 8. Return the "newHead" variable.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseLinkedList(head, k):
    newHead = None
    tail = None
    current = head
    count = 0
    while current:
        count += 1
        if count == k:
            nextNode = current.next
            current.next = None
            reversedHead = reverseList(head)
            if not newHead:
                newHead = reversedHead
            else:
                tail.next = reversedHead
            tail = head
            head = nextNode
            current = nextNode
            count = 0
        else:
            current = current.next
    if tail:
        tail.next = head
    return newHead

def reverseList(head):
    if not head or not head.next:
        return head
    newHead = reverseList(head.next)
    head.next.next = head
    head.next = None
    return newHead

def reverseKGroup(head, k):
    if not head or k == 1:
        return head
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    while prev:
        prev.next = reverseLinkedList(prev.next, k)
        for i in range(k):
            if not prev.next:
                break
            prev = prev.next
    return dummy.next
