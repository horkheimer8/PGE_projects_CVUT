# author : Jiyeong Chae (Mrs.)
# creation date : 03/03/2020-
# Underground Mine Robot Training : Homework 1

# -------------------------------------------------------------------------------#
# consider ...
#   the case bar size is over the corridor length
#   
# -------------------------------------------------------------------------------#
import sys

### dealing with inputs following the given condition 
print("""Len, Rad, Sec1, Sec2, Sec3,
              a list of Len positive integers
              comm(# of commands) and commands: (after typing all press ctrl+d)
              """)
input_list = sys.stdin.readlines()
# use split after and distribute to each variables

Len, Rad, Sec1, Sec2, Sec3 = [int(x) for x in input_list[0].split()]
"""
Len : length of the corridor
Rad : length of the bar over each robot's head
Sec1, Sec2, Sec3 : are the initial positions of the robots
"""
corridor = [int(x) for x in input_list[1].split()]
# corridor : required time in each section of corridor
comm = int(input_list[2].strip('\n').strip(" "))  # comm : the number of commands
commands = [x for x in input_list[3:3 + int(comm)]]
print("input_list : ", input_list)
print("Len, Rad, Sec1, Sec2, Sec3 : ", Len, Rad, Sec1, Sec2, Sec3)
print("corridor : ", corridor)
print("doubleOrNot : ", doubleOrNot)
print("possible  position of  robot is from 0 to", len(corridor) - 1)
print("comm : ", comm)
print("commands : ", commands)


### making class Robot
class Robot():

    def __init__(self, num, position):

        self.num = num  # number of the robot
        self.position = position  # current position of the robot
        self.rt = 0  # time duration (sum of corridor's nums)

    def oneMoveTime(self, moveDir, moveLen):
        print("@")
        print('moveDir, moveLen', moveDir, moveLen)
        startPos = self.position  # save the position before the move
        print('start', startPos)
        sumOfTimes = 0  # initialize the value of sum to 0

        if (moveDir == 1):  # right
            self.position = self.position + moveLen
            if self.position > len(corridor) - 1:
                self.position = len(corridor) - 1
            endPos = self.position
            print('^', endPos)
            # getting sumOfTimes in case of moves toward right
            for x in range(startPos + 1, endPos + 1):
                sumOfTimes = sumOfTimes + corridor[x]
                print("%")
        return sumOfTimes

        if (moveDir == 0):  # left
            self.position = self.position - moveLen
            if self.position < 0:
                self.position = 0
            endPos = self.position  # save the position after the move
            print('^', endPos)
            # getting sumOfTimes in case of moves toward left
            for x in range(endPos + 1, startPos + 1):
                sumOfTimes = sumOfTimes + corridor[x]
                print("%")
            return sumOfTimes
        print("$")

    # function that calculates the "double" sections of corridor
    def calcDouble(self, Rad):
        doubleOrNot = [int(1) for x in range(Len)]  # to check if there's bar or not
        startIndex = self.position - Rad
        if (startIndex < 0):
            startIndex = 0
        endIndex = self.position + Rad + 1
        if (endIndex > len(Len) - 1):
            endIndex = len(Len) - 1
        for x in range(startIndex, endIndex):
            doubleOrNot[x] = int(2)
        print(doubleOrNot)


# function that switches comm and commands into 'oneMoveTime' function
def autoCommands(comm, commands):
    for x in range(comm):
        lst = [int(x) for x in commands[x].strip('\n').split()]
        print("goodmorning", lst)
        if (lst[0] == 1):  # r1
            r1.oneMoveTime(lst[1], lst[2])
        elif (lst[0] == 2):  # r2
            r2.oneMoveTime(lst[1], lst[2])
        elif (lst[0] == 3):  # 3
            r3.oneMoveTime(lst[1], lst[2])


# -------------------------------------------------------------------------------#
### printing out to check if everything's going alright            
r1 = Robot(1, Sec1)
r2 = Robot(2, Sec2)
r3 = Robot(3, Sec3)
print("Robot1 num, position, runtime : ", r1.num, r1.position, r1.rt)
print("Robot2 num, position, runtime : ", r2.num, r2.position, r2.rt)
print("Robot3 num, position, runtime : ", r3.num, r3.position, r3.rt)
# print(r1.oneMoveTime(0, 3))
print("Robot1 num, position, runtime : ", r1.num, r1.position, r1.rt)

'''           
   # 2. produce the sum of all elements in T between
   # startPos and endPos, including startPos and endPos.
   sumOfTimes = # your calculation here
   # 3. return the calculated value
   return sumOfTimes'''
print(commands[0].strip('\n').split())
print('329485308549702372849653184')
print(autoCommands(comm, commands))
r1.calcDouble(2)
