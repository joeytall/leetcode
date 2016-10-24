# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution(object):
  def addTwoNumbers(self, l1, l2):
    dummyHead = ListNode(0)
    current = dummyHead
    carry = 0
    while l1 or l2:
      x = l1.val if l1 else 0
      y = l2.val if l2 else 0
      sumVal = x + y + carry
      carry = sumVal / 10
      current.next = ListNode(sumVal % 10)
      current = current.next
      if l1:
        l1 = l1.next
      if l2:
        l2 = l2.next
    if carry:
      current.next = ListNode(1)
    result = dummyHead.next
    self.printList(result)
    return result

  def printList(self, nodeList):
    while nodeList:
      print nodeList.val
      nodeList = nodeList.next

a = ListNode(2)
b = ListNode(4)
c = ListNode(3)
a.next = b
b.next = c

d = ListNode(5)
e = ListNode(6)
f = ListNode(4)
d.next = e
e.next = f

Solution().addTwoNumbers(a,d)
