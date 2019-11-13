"""
Day 67 - Designer Door Mat

Hacker Rank - Easy

Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:
  Mat size must be NxM. (N is an odd natural number, and M is 3 times N.)
  The design should have 'WELCOME' written in the center.
  The design pattern should only use |, . and - characters.

Sample Designs

    Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
    
    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------

Input Format:
  A single line containing the space separated values of  and .

Constraints:
  5 < N < 101
  15 < M < 303

Output Format:
  Output the design pattern.

Sample Input:
  9 27
  
Sample Output:

  ------------.|.------------
  ---------.|..|..|.---------
  ------.|..|..|..|..|.------
  ---.|..|..|..|..|..|..|.---
  ----------WELCOME----------
  ---.|..|..|..|..|..|..|.---
  ------.|..|..|..|..|.------
  ---------.|..|..|.---------
  ------------.|.------------
  
"""
#!/usr/bin/python3
def createPattern(width, height):
  """ Uses a defined width and height
  Returns a string formatted with the correct layout.
  """
  pattern = ""
  
  # First Line
  pattern = pattern + ".|.".center(width, "-") + "\n"
  
  # Middle Section
  for i in range(1, height - 1):
    if i < ((height - 1) / 2):
      pattern = pattern + (".|" + ("..|" * i * 2 ) + ".").center(width, "-") + "\n"
    elif i == ((height - 1) / 2):
      pattern = pattern + "WELCOME".center(width, "-") + "\n"
    elif i > ((height - 1) / 2):
      pattern = pattern + (".|" + ("..|" * (height - 1 - i) * 2) + ".").center(width, "-") + "\n"
  # Last Line
  pattern = pattern + ".|.".center(width, "-")
  
  return pattern

if __name__ == "__main__":
    height, width = map(int, input().split(" "))
    pattern = createPattern(width, height)
    print(pattern)
