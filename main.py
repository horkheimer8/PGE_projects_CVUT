# author : Jiyeong Chae (Mrs.)
# creation date : 03/03/2020-
# Underground Mine Robot Training : Homework 1

# -------------------------------------------------------------------------------#
# consider ...
#   the case bar size is over the corridor length
#   
# -------------------------------------------------------------------------------#


### dealing with inputs following the given condition
from typing import List, Any, Union

'''print("""Len, Rad, Sec1, Sec2, Sec3,
              a list of Len positive integers
              comm(# of commands) and commands: (after typing all press ctrl+d)
              """)'''
input_list = []
while True:
    line = input()
    if line:
        input_list.append(line)
    else:
        break
text = '\n'.join(input_list)

# use split after and distribute to each variables

[Len, Rad, Sec1, Sec2, Sec3] = [int(x) for x in input_list[0].split()]
"""
Len : length of the corridor
Rad : length of the bar over each robot's head
Sec1, Sec2, Sec3 : are the initial positions of the robots
"""
corridor = [int(x) for x in input_list[1].split()]  # required time in each section of corridor
comm = int(input_list[2].strip('\n').strip(" "))  # comm : the number of commands
commands: List[str] = [x for x in input_list[3:3 + int(comm)]]
'''
# printing out to check if everything's going alright
print("input_list : ", input_list)
print("Len, Rad, Sec1, Sec2, Sec3 : ", Len, Rad, Sec1, Sec2, Sec3)
print("corridor : ", corridor)
print("possible  position of  robot is from 0 to", len(corridor) - 1)
print("comm : ", comm)
print("commands : ", commands)

'''
### making class Robot
def finalTimeSum():
    return r1.rt + r2.rt + r3.rt


class Robot:
    position: int

    def __init__(self, num: int, position: int):

        self.num = num  # number of the robot
        self.position = position  # current position of the robot
        self.rt = 0  # time duration (sum of corridor's nums)

    def oneMoveTime(self, moveDir: int, moveLen: int):
        # print("@@ start of oneMoveTime @@")
        startPos = self.position  # save the start position before the move
        endPos = 0
        # print('start', startPos)
        sumOfTimes: int = 0  # initialize the value of sum to 0

        if moveDir == 1:  # right
            self.position = self.position + moveLen  # renew the position along the move
            if self.position > len(corridor) - 1:  # adjust the position considering the corridor
                self.position = len(corridor) - 1
            endPos = self.position

        elif moveDir == 0:  # left
            self.position = self.position - moveLen  # renew the position along the move
            if self.position < 0:  # adjust the position considering the corridor
                self.position = 0
            endPos = self.position  # save the end position after the move

        # print('end', endPos)

        # reset robot's position into startPos
        current = startPos
        # moving right
        if startPos < endPos:
            for x in range(startPos + 1, endPos + 1):
                current += 1
                self.position = current
                doubleOrNot_ = calcDouble(Rad)
                # print('###', doubleOrNot_)
                sumOfTimes = sumOfTimes + corridor[x] * doubleOrNot_[x]
        # moving left makes startPos bigger than endPos so gonna switch those for calculation
        elif startPos > endPos:
            temp_list: List[int] = [0] * Len
            for x in range(endPos, startPos):
                temp_list[x] = corridor[x]
            for x in range(endPos, startPos):
                self.position -= 1
                # print('double list at every moment', calcDouble(Rad))
                doubleOrNot_ = calcDouble(Rad)
                sumOfTimes = sumOfTimes + temp_list[x] * doubleOrNot_[x]
        else:  # when startPos == endPos
            sumOfTimes = sumOfTimes

        # update robot's consumed time
        self.rt = self.rt + sumOfTimes
        return sumOfTimes

    ### end of oneMoveTime


r1: Robot = Robot(1, Sec1)
r2: Robot = Robot(2, Sec2)
r3: Robot = Robot(3, Sec3)


# function that switches comm and commands into 'oneMoveTime' function
def autoCommands(comm_, commands_):
    # lst = []  # lst would be accummulated - have to deal with all the command at once
    for x in range(comm_):
        lst = []  # renew lst each time so only deal with one command at a time
        for y in commands_[x].strip('\n').split():
            lst.append(int(y))
        # print("one Command ", lst)
        if lst[0] == 1:  # r1
            # print("r1's sumOfTimes", r1.oneMoveTime(lst[1], lst[2]))
            r1.oneMoveTime(lst[1], lst[2])
        elif lst[0] == 2:  # r2
            # print("r2's sumOfTimes", r2.oneMoveTime(lst[1], lst[2]))
            r2.oneMoveTime(lst[1], lst[2])
        elif lst[0] == 3:  # 3
            # print("r3's sumOfTimes", r3.oneMoveTime(lst[1], lst[2]))
            r3.oneMoveTime(lst[1], lst[2])


    # print("end of autoCommands \n")


def calcDouble(rad_):  # rad_ is Rad in outerscope which is the bar length)
    """
    :type rad_: Int
    """
    doubleOrNot_: List[int] = [1] * Len  # list to check if there's bar or not

    rlist: List[Robot] = [r1, r2, r3]
    for robot in rlist:
        startIndex = robot.position - rad_
        if startIndex < 0:
            startIndex = 0
        endIndex = robot.position + rad_ + 1  # +1 is due to 'range'
        if endIndex > Len:
            endIndex = Len
        for z in range(startIndex, endIndex):
            doubleOrNot_[z] = 2

    return doubleOrNot_
# -------------------------------------------------------------------------------#
# initial doubleOrNot!
doubleOrNot: List[int] = calcDouble(Rad)
'''
#print("\nINITIAL VALUES")
#print("Robot1 num, position, runtime : ", r1.num, r1.position, r1.rt)
#print("Robot2 num, position, runtime : ", r2.num, r2.position, r2.rt)
#print("Robot3 num, position, runtime : ", r3.num, r3.position, r3.rt)

#print('\nrun autoCommands')
print(autoCommands(comm, commands))

print('finished! now sumOfTimes of each robot : ', r1.rt, r2.rt, r3.rt)
print('let\'s see where\'s should be doubled: ', calcDouble(Rad))
'''
print(finalTimeSum())
