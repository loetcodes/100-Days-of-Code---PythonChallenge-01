"""
Day 60 - Jumping on the Clouds

HackerRank

Description:
Emma is playing a new mobile game that starts with consecutively numbered clouds. Some of the clouds are thunderheads and others are cumulus. She can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus 1 or 2. She must avoid the thunderheads. Determine the minimum number of jumps it will take Emma to jump from her starting position to the last cloud. It is always possible to win the game.

For each game, Emma will get an array of clouds numbered 0 if they are safe or 1 if they must be avoided. For example, c=[0, 1, 0, 0, 0, 1, 0] indexed from 0...6. The number on each cloud is its index in the list so she must avoid the clouds at indexes 1 and 5. She could follow the following two paths: 0 -> 2 -> 4 -> 6 or 0 -> 2 -> 3 -> 4 -> 6 . The first path takes 3 jumps while the second takes 4.


Function Description:
Complete the jumpingOnClouds function in the editor below. It should return the minimum number of jumps required, as an integer.

jumpingOnClouds has the following parameter(s):
    c: an array of binary integers


Constraints:
    2 <= n <= 100
    c[i] member {0,1}
    c[0] = c[n - 1] = 0

Output Format:
Print the minimum number of jumps needed to win the game.

Sample Input 0:
    7
    0 0 1 0 0 1 0

Sample Output 0:
    4

Explanation 0:
    Emma must avoid c[2] and c[5]. She can win the game with a minimum of 4 jumps

Sample Input 1:
    6
    0 0 0 0 1 0

Sample Output 1:
    3

Explanation 1:
    The only thundercloud to avoid is c[4]. Emma can win the game in 3 jumps.

"""


#!/bin/python3


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    if (len(c) < 2) or (c[-1] != 0):
        return 0
    moves = 0
    i = 0
    last_cloud = len(c) - 1
    while (last_cloud - i > 1):
        if (c[i + 2] == 0):
            i += 2
        elif (c[i + 1] == 0):
            i += 1
        moves += 1
    if i != last_cloud:
        moves += 1 
    return moves



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
