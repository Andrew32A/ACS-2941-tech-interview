# ******************************************************************************
# Question
# Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
# You should preserve the original relative order of the nodes in each of the two partitions.

# Example 1:
# Input: head = [1,4,3,2,5,2], x = 3
# Output: [1,2,2,4,3,5]

# Example 2:
# Input: head = [2,1], x = 2
# Output: [1,2]

# ******************************************************************************
# Steps
# Create two dummy nodes h1 and h2, each representing the head of the linked lists containing nodes with values less than x and greater than or equal to x, respectively.
# Create two "tail" nodes l1 and l2, each representing the last node in the respective linked list. Initially, these nodes point to the corresponding dummy nodes.
# Traverse the input linked list starting from the head. For each node:
# If its value is less than x, append it to the l1 linked list by setting l1.next to the current node and updating l1 to the current node.
# Otherwise, append it to the l2 linked list by setting l2.next to the current node and updating l2 to the current node.
# After all nodes have been processed, set l2.next to None to terminate the l2 linked list.
# Connect the two linked lists by setting l1.next to h2.next.
# Return the head of the h1 linked list.

#  Solution

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        h1 = l1 = ListNode(0)
        h2 = l2 = ListNode(0)
        
        while head:
            if head.val < x:
                l1.next = head
                l1 = l1.next
            else:
                l2.next = head
                l2 = l2.next
            head = head.next
            
        l2.next = None
        l1.next = h2.next
        
        return h1.next

# Time Complexity: O(n)