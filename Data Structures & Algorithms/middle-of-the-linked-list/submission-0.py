# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=head
        length=0
        while(head!=None):
            length+=1
            head=head.next
        length//=2
        length+=1
        head=l
        count=0
        while(head!=None):
            count+=1
            if count is length:
                return head
            head=head.next
        