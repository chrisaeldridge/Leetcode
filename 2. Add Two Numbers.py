from collections import deque
from typing import Optional
import math

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "ListNode(val=" + str(self.val) + ", next={" + str(self.next) + "})"

def list_to_LL(arr):
    if len(arr) < 1:
        return None

    if len(arr) == 1:
        return ListNode(arr[0])
    return ListNode(arr[0], next=list_to_LL(arr[1:]))

def reverseList(head: ListNode) -> ListNode:
    prev = None
    while head:
        next_node = head.next
        head.next = prev
        prev = head
        head = next_node

    return prev

def linkedlistToDeque(head: ListNode) -> deque:
    prev = None
    dq = deque()
    while head:
        dq.append(head.val)
        next_node = head.next
        head.next = prev
        head = next_node
    return dq

class Solution:
    def addTwoNumbersDQ(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        llist = deque(l1)
        n1 = 0
        while not len(llist)==0 :
            n1 = n1*10+llist.pop()
        llist2 = deque(l2)
        n2 = 0
        while not len(llist2)==0 :
            n2 = n2*10+llist2.pop()
        n = n1+n2
        llistout = deque()
        while True :
            rightdig = int(round((n/10 - math.floor(n/10))*10))
            n = int(math.floor(n/10))
            llistout.append(rightdig)
            if n==0: 
                break
        return llistout
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1dq = linkedlistToDeque(l1)
        n1 = 0
        while not len(l1dq)==0 :
            n1 = n1*10+l1dq.pop()
        l2dq = linkedlistToDeque(l2)
        n2 = 0
        while not len(l2dq)==0 :
            n2 = n2*10+l2dq.pop()
        n = n1+n2
        llistout = deque()
        print(n)
        while n > 0:
            n, remainder = divmod(n, 10)
            llistout.append(remainder)
        return list_to_LL(list(llistout))

# answer using deque linked list
print('\nVersion 1 :\n')
l1 = deque([1,2,3])
l2 = deque([4,5,6])
print(l1)
print(l2)
print(f'answer = {Solution().addTwoNumbersDQ(l1,l2)}')


# answer using leetcode definition of linked lists
print('\nVersion 2 :\n')
l1 = list_to_LL([1, 2, 3])
l2 = list_to_LL([4, 5, 6])
print((l1))
print((l2))
#print(f'answer = {Solution().addTwoNumbers(l1,l2)}')

print('\nVersion 2, test 2 :\n')
l1 = list_to_LL([0])
l2 = list_to_LL([0])
print((l1))
print((l2))
#print(f'answer = {Solution().addTwoNumbers(l1,l2)}')

print('\nVersion 2, test 3 :\n')
l1 = list_to_LL([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])
l2 = list_to_LL([5,6,4])
print((l1))
print((l2))
print(f'answer = {Solution().addTwoNumbers(l1,l2)}')

