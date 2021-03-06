
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None



class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None




import heapq
import operator


def my_lt (self, other):
	'''
	create my own lt function
	'''
	return operator.lt(self.val, other.val)

class Solution:
	def mergeKLists(self, lists):
		"""
		:type lists: List[ListNode]
		:rtype: ListNode
		"""

		ListNode.__lt__ = my_lt # let ListNode cmp function to be my_lt

		# create head node and let current be head
		head = ListNode(None)
		current = head

		# q is heapq list
		q = []

		# push all nodes into q 
		for anode in lists:
			node = anode
			while(node):
				heapq.heappush(q,node)
				node = node.next
		
		# pop min val's node, and assign current's next to it
		while(q):
			current.next = heapq.heappop(q)
			current = current.next

		current.next = None

		return head.next



if __name__ == '__main__':
	a1 = ListNode(-1)
	a2 = ListNode(-1)
	a3 = ListNode(-1)
	a1.next = a2
	a2.next = a3

	b1 = ListNode(-2)
	b2 = ListNode(-2)
	b3 = ListNode(-1)
	b1.next = b2
	b2.next = b3

	c1 = ListNode(1)
	c2 = ListNode(2)
	c3 = ListNode(9)
	c1.next = c2
	c2.next = c3

	re = Solution().mergeKLists([a1,b1])

	while(re):
		print(re.val)
		re = re.next








