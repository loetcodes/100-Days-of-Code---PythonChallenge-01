"""
Day 57 - Call Python List commands from input text file

Hackerrank

Consider a list (list = []). You can perform the following commands:
  insert i e: Insert integer  at position .
  print: Print the list.
  remove e: Delete the first occurrence of integer .
  append e: Insert integer  at the end of the list.
  sort: Sort the list.
  pop: Pop the last element from the list.
  reverse: Reverse the list.
  
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. 
Iterate through each command in order and perform the corresponding operation on your list.

Input Format:
  The first line contains an integer, , denoting the number of commands. 
  Each line  of the  subsequent lines contains one of the commands described above.

Constraints:
  The elements added to the list must be integers.
  
Output Format:
  For each command of type print, print the list on a new line.

Sample Input 0:
  12
  insert 0 5
  insert 1 10
  insert 0 6
  print
  remove 6
  append 9
  append 1
  sort
  print
  pop
  reverse
  print
  
Sample Output 0:
  [6, 5, 10]
  [1, 5, 9, 10]
  [9, 5, 1]

"""
#!/bin/python3

if __name__ == '__main__':
    N = int(input())
    call_func = {
        "insert": lambda a , x : a.insert(x[0], x[1]),
        "remove" : lambda a, x : a.remove(x[0]),
        "append" : lambda a, x : a.append(x[0]),
        "print" : lambda a : print(a),
        "sort" :  lambda a : a.sort(),
        "pop" : lambda a : a.pop(),
        "reverse" :  lambda a : a.reverse()
    }

    list_result = []
    for i in range(N):
        line = input().split(" ", 1)
        command = line[0]
        func = call_func[command]
        if len(line) > 1:
            int_params = [int(e) for e in line[1].split(" ")]
            func(list_result, int_params)
        else:
            func(list_result)
