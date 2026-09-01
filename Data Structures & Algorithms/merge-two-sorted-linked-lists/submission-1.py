# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list_one = list1
        list_two = list2
        result = ListNode()
        curr = result
        
        while list_one:
            if list_two is None:
                curr.next = list_one
                curr = curr.next
                list_one = list_one.next
            elif list_two is not None and list_one.val < list_two.val:
                curr.next = list_one
                curr = curr.next
                list_one = list_one.next
            else:
                curr.next = list_two
                curr = curr.next
                list_two = list_two.next 
        if list_two:
            curr.next = list_two
        return result.next
        