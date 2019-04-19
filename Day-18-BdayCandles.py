"""

Day - 18: Birthday cake candles  Hackerrank

You are in charge of the cake for your niece's birthday and have decided the cake will have one candle for each year of her total age. When she blows out the candles, she’ll only be able to blow out the tallest ones. Your task is to find out how many candles she can successfully blow out.

For example, if your niece is turning 4 years old, and the cake will have  candles of height 4, 4, 1, 3, she will be able to blow out 2 candles successfully, since the tallest candles are of height 4 and there are 2 such candles.

Function Description:
Complete the function birthdayCakeCandles in the editor below. It must return an integer representing the number of candles she can blow out.


Constraints:
  1 <= n <= 10^5
  1 < ar[i] <= 10^7


Output Format:
Print the number of candles that can be blown out on a new line.

Sample Input 0:
  4
  3 2 1 3
Sample Output 0:
  2

"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    return ar.count(max(ar))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
