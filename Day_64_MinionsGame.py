"""

Day 64 Minions Game

Hacker rank - medium

Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String S = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

Your task is to determine the winner of the game and their score.

Input Format:
  A single line of input containing the string S.
  Note: The string  will contain only uppercase letters: [A-Z].

Constraints:
  0 <= len(S) <= 10 ^ 6

Output Format:
  Print one line: the name of the winner and their score separated by a space.

If the game is a draw, print Draw.

Sample Input:
  BANANA
  
Sample Output:
  Stuart 12

Note :
Vowels are only defined as AEIOU. In this problem, Y is not considered a vowel.

"""
#!/bin/python3

def minion_game(string):
  vowels = 'AEIOU'
  kevin_score = 0
  stuart_score = 0
  for index, value in enumerate(string):
    if value in vowels:
      kevin_score += (len(string) - index)
    else:
      stuart_score += (len(string) - index)
  if kevin_score > stuart_score:
    print("Kevin", kevin_score)
  elif stuart_score > kevin_score:
    print("Stuart", stuart_score)
  else:
    print("Draw")
    
if __name__ == '__main__':
  s = input()
  minion_game(s)


