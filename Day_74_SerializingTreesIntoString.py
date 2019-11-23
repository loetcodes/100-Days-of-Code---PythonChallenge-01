"""
Day 74 - Serializing and Deserializing A Tree into A String

Source: Daily Coding Problem

Level: Medium

Task:
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserializes(s), which deserializes the string back into the tree.

Example:
Given the following Node class
	class Node:
		def __init__(self, val, left=None, right=None):
			self.val = val
			self.left = left
			self.right = right

The following test should pass:
	node = Node('root', Node('left', 
			Node('left.left')), Node('right'))
	assert deserialize(serialize(node)).left.left.val == 'left.left'


"""
#!/usr/bin/python3
def serialize(root):
	if root is None:
		return '#'
	return '{} {} {}'.format(root.val, serialize(root.left), serialize(root.right))

def deserialize(data):
	def helper():
		val = next(vals)
		if val == '#':
			return None
		node = Node(int(val))
		node.left = helper()
		node.right = helper()
		return node
	vals = iter(data.split())
	return helper()		


if __name__ == "__main__":
	node = Node('root', Node('left', 
			Node('left.left')), Node('right'))
	assert deserialize(serialize(node)).left.left.val == 'left.left'
	print('Run 1 tests with 0 failures.')