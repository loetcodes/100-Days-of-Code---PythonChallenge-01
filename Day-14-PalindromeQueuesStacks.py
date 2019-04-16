"""

Day 14 Palindrome checker and Queues and Stacks

A palindrome is a word, phrase, number, or other sequence of characters which reads the same backwards and forwards.

To solve this challenge, we must first take each character in s, enqueue it in a queue, and also push that same character onto a stack. Once that's done, we must dequeue the first character from the queue and pop the top character off the stack, then compare the two characters to see if they are the same; as long as the characters match, we continue dequeueing, popping, and comparing each character until our containers are empty (a non-match means  isn't a palindrome).

The solution class must incorporate the following declarations and implementations:
 1. Two instance variables: one for the stack, and one for the queue.
 2. A void pushCharacter(char ch) method that pushes a character onto a stack.
 3. A void enqueueCharacter(char ch) method that enqueues a character in the queue instance variable.
 4. A char popCharacter() method that pops and returns the character at the top of the stack instance variable.
 5. A char dequeueCharacter() method that dequeues and returns the first character in the queue instance variable.


Input Format:
string s

Constraints:
s is composed of lowercase english letters.

Output Format:
When correct should print: The word, s, is a palindrome.
otherwise: The word, s, is not a palindrome.

Sample Input:
racecar

Sample Output:
The word, racecar, is a palindrome.

"""
#!/bin/python3

class Solution:
    def __init__(self):
        self.queue_var = list()
        self.stack_var = list()
     
    def pushCharacter(self,char):
        self.stack_var.append(char)
        
    def popCharacter(self):
        return self.stack_var.pop()
        
    def enqueueCharacter(self, char):
        self.queue_var.append(char)

    def dequeueCharacter(self):
        return self.queue_var.pop(0)
        

s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")