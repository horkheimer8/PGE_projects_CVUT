# getting index number of a list that you wanna make
def createList(x):
    time_list = []
    for i in range(int(x)): 
        time_list.append(0)
    return time_list

a = input("Enter the index of a list you want to make: ")
print(createList(a))

#-------------------------------------------------------------------------------#
# making class Robot
class Robot:
    def __init__(robot, num, position):
        robot.num = num # number of the robot
        robot.position = position # current position of the robot
        robot.rt = 0 # time duration (sum of corridor's nums)
r1 = Robot(1, 6)

print(r1.num, r1.position, r1.rt)
    
#-------------------------------------------------------------------------------#
# dealing with inputs following the given condition 
input_list = input("""Len, Rad, Sec1, Sec2, ..., SecLen
              a list of Len positive integers
              Comm(# of commands) and commands: """).split(' ')
    # use split after and distribute to each variables
    # keep the rule that 2<=Len<=10^4, 1<=

