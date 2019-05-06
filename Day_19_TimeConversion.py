"""

Day 19 - Time conversion hacker rank

Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.

Constraints:
All input times are valid

Output Format:
Convert and print the given time in 24-hour format, where 00 <= hh <= 23

Sample Input 0:
07:05:45PM

Sample Output 0:
19:05:45

"""

#!/bin/python3

import os
import sys

def timeConversion(s):
    time = s.split(':')
    hr = int(time[0])
    meridiem = time[-1][-2:]
    time[-1] = time[-1][:-2]
    if hr < 12 and meridiem == 'PM':
        time[0] = str(hr + 12)
    elif hr == 12 and meridiem == 'AM':
        time[0] = '00'
    return ':'.join(time)
    

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
