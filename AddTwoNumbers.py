# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        num1=''
        num2=''
        num = []
        itr = l1
        while itr:
            num.append(itr.val)
            itr = itr.next
        num = num[::-1]
        for i in num:
            num1 = num1+str(i)
        itr = l2
        num = []
        while itr:
            num.append(itr.val)
            itr = itr.next
        num = num[::-1]
        for i in num:
            num2 = num2+str(i)
        ans=0
        ans= list(str(int(num1)+int(num2))[::-1])
        print(ans) 
        lf = l = ListNode(int(ans[0]))
        for i in range(1,len(ans)):
            l.next = ListNode(int(ans[i]))
            l = l.next
        return(lf)
