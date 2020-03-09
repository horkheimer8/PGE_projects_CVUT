# [7 1 3 2 5 2 4 6 1]
# Given:
# s:    start position:6
# d:    direction of movement 0... left 1...right
# n:    num of visited positions in the move.
# Goal: total sum of all visited values in one move.
# More commands of the same format

def moveValueGetSum(s, d, n):
    arr = [7, 1, 3, 2, 5, 2, 4, 6, 1]
    sum = 0
    
    # move left, extract index values and add it to the sum 
    for i in range(s, s-n):
        sum = sum + arr[i]
        
    # move right, extract index values and add it to the sum
    for i in range(s, s+n):
        sum = sum + arr[i]         

    # make if for exception that is out of range of index
    if ((s<0) || (s>=9)):
        print("wrong index. try it again:)
              
    # what if the move required  exceed the index?

    # in case of the array values that I put in doens't fit into the array size

    # in case of 
