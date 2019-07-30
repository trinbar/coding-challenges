"""
You are given two linked-lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

    Example:
    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    
    Explanation: 342 + 465 = 807.
"""

#Function signature (given)

# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None
    self.head = None

class Solution:
  def addTwoNumbers(self, l1, l2, c = 0):
    
    #Initialize two variables where I will 'catch' the nums in linked list
    num1 = []
    num2 = []

    #Assign pointers to heads of l1 and l2
    current1, current2 = l1.head, l2.head
    
    #Traverse through LinkedList
    while current1:
        #Reassign next to None in case it has later implications
        current1.next = None
        num1.append(current1.val)
        #Move current one node forward such that 'head' is reassigned
        current1 = current1.next

    while current2:
        current2 = l2.head
        num2.append(current2.val)
        current2 = current2.next

    #Reverse and stringify num1 and num2 lists and change to int type
    num1.reverse()
    num2.reverse()
    num1 = "".join(str(x) for x in num1)
    num2 = "".join(str(y) for y in num2)
    num1 = int(num1)
    num2 = int(num2)


    return (num1 + num2)

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

# result = Solution().addTwoNumbers(l1, l2)
# while result:
#   print(result.val,
#   result = result.next)
# # 7 0 8
