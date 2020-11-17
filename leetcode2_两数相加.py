class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        co=0 #记录相加之后的进位
        res=ListNode(-1)
        cur=res
        while l1 or l2:
            l1num=0 if l1==None else l1.val
            l2num = 0 if l2==None else l2.val
            sum=co+l1num+l2num
            co=sum/10
            cur.next=ListNode(sum%10)
            cur=cur.next
            l1=None if l1==None else l1.next
            l2=None if l2==None else l2.next
        return res.next
