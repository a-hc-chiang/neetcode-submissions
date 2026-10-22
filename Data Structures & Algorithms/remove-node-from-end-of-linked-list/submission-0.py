# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        if not head.next and n: 
            return None
        res = head
        length_of_list = 0 
        while head: 
            length_of_list += 1
            head = head.next
        target = length_of_list - n 
        head = res 
        if not target: 
            return res.next
        for i in range(target): 
            if i == target - 1: 
                if head.next.next: 
                    head.next = head.next.next
                elif head: 
                    head.next = None 
                break 
            head = head.next
        return res