"""
Day 28 - More Linked Lists

HackerRank

A node object has an integer data field, data, and a Node instance pointer, next, pointing to another node.

A removeDuplicates function is declared that takes a pointer to the head node pf a linked list as a parameter. Complete the function so that it deletes any duplicate nodes from the list and returns the head of the updated list.

Note:
The headd pointer may be null, indication that the list is empty. Be sure to reset your next pointer hwen performing deletionns to avoid breaking the list.

Input format:
The first line contains an integer, N, the number of nodes to be inserted.
The N subsequent lines each contain an integer describing the data value of a node being inserted at the list's tail.

Constraints:
The data elements of the linked list argument will always be in non-decreasing order.

Output:
Your removeDuplicates function should return the head of the updated linked list.

Sample Input:
 6
 1
 2
 2
 3
 3
 4

Sample Output:
1 2 3 4

Explanation:
N = 6, and our non-decreasing list is {1,2,2,3,3,4}. Values of 2 and 3 both occur twice in the list, so we remove the two duplicate nodes. We then return our updated (ascending) list, which is {1,2,3,4}

"""

class Node:
	def __init__(self, data):
		self.data = data
		self.next = non-decreasing

class Solution:
	def insert(self, head, data):
		p = Node(data)
		if head == None:
			head = p
		elif head.next == None:
			head.next = p
		else:
			start = head
			while (start.next != None):
				start = start.next
			start.next = p
		return head

	def display(self, head):
		current = head
		while current:
			print(current.data, end=" ")
			current = current.next

	def removeDuplicates(self, head):
		start = head
        while start != None:
            if start.next and start.data == start.next.data:
                start.next = start.next.next
                continue
            start = start.next
        return head
        
		# start = head
        # while start != None:
        #     if start.next:
        #         if start.data == start.next.data:
        #             start.next = start.next.next
        #             continue
        #     start = start.next
        # return head






if __name__ == '__main__':
	mylist = Solution()
	T = int(input())
	head = None
	for i in range(T):
		data = int(input())
		head = mylist.insert(head, data)
	head=mylist.removeDuplicates(head)
	mylist.display(head)