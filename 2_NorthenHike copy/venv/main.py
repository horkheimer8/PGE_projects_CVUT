# author : Jiyeong Chae
# creation date : 11/Mar/2020
# finishing date :
# homework 2 : " Northen Hike "

### dealing with inputs following the given condition
from typing import List, Any, Union

input_list = []
while True:
    line = input()
    if line:
        input_list.append(line)
    else:
        break
text = '\n'.join(input_list)

# use split after and distribute to each variables

one_section_limits = input_list[0].strip(" ").strip("\n")  # use int() later
hike_limits = input_list[1].strip("\n").strip(' ')  # use int() later
N: int = int(input_list[2].strip("\n").strip(' '))
# make rest of them into one array and seperate them into isCampSite, elevation, distance, time
all = []
for i in range(3, 2 + N + 1):
    all.extend(input_list[i].split(' '))
# and seperate them into isCampSite, elevation, distance, time
isCampSite = []
elevation = []
distance = []
time = []
endPoint = [0] * N

for i in range(0, len(all)):
    if i % 4 == 0:
        isCampSite.append(int(all[i]))
    elif i % 4 == 1:
        elevation.append(int(all[i]))
    elif i % 4 == 2:
        distance.append(int(all[i]))
    elif i % 4 == 3:
        time.append(int(all[i]))

# STEP1. calculate elevation difference and update elevation array checking uphill parts
for i in range(0, len(elevation) - 1):
    elevation[i] = elevation[i + 1] - elevation[i]
    if elevation[i] < 0:
        elevation[i] = 0
elevation[-1] = 0  # elevation difference of last element is anyway 0.

# STEP2. find camp sites and update E, D, T with accumulated values.
# and eliminate values in non-camp-sites for later loops.

for i in range(0, N):
    if isCampSite[i] == 0:
        continue
    if isCampSite[i] == 1:
        # !! try to make this part into a function too with hint !!
        j = i + 1
        try:
            while isCampSite[j] == 0:
                elevation[i] = elevation[i] + elevation[j]  # accumulating values only to camp sites
                distance[i] = distance[i] + distance[j]
                time[i] = time[i] + time[j]
                j += 1
        except IndexError:
            break
for i in range(0, N):
    if isCampSite[i] == 0:
        elevation[i] = 0
        distance[i] = 0
        time[i] = 0

# now every non-camp-sites are empty, and only camp sites are filled
# with continuous sum of values between camp sites.

# trial for using hint and make another function for STEP2.
'''
def accOnlyCampSite( arr ):
    #echo input values
    print(arr)
    print("gonna only leave values of camp sites with accumulated values.")

    # the window starts as very small, it contains  only
    # the first element of the array

    begin, end = 0, 0  # begin and end of the sliding window
    currSum = arr[0]  # initial sum in window

    # best values were not found yet:
    bestBegin, bestEnd, bestSum = -1, -1, -1

    # run sliding window
    while end < len(arr):
        # echo current status
        print("sum from", begin, "to", end, "is", currSum)
        # register the continuous sum right before the next camp site
        if arr[end]
'''


# STEP3. find possible sections considering one-section limit.
# accumulate values (it's time to add 'endPoint' values!) from the start to end of each section.

# !!!! you need to understand the hint first !!!!
def findPossibleSection(isCampSite_, elevation_, distance_, time_):
    """

    :type elevation_: list
    """
    print("\nthis is to find possible sections")
    '''
    # echo input values
    print(isCampSite_, "\n")
    print(elevation_, "\n")
    print(distance_, "\n")
    print(time_, "\n") to '''

    # the window starts as very small, it contains only
    # the first element of the array
    begin, end = 0, 0  # begin and end of the sliding window
    currSumE = elevation_[0]  # initial sum in window
    currSumD = distance_[0]
    currSumT = time_[0]

    # best values were not found yet:
    bestBegin, bestEnd, bestSumE, bestSumD, bestSumT = -1, -1, -1, -1, -1

    # run sliding window
    while end < N:
        # echo current status
        print("sum from", begin, "to", end, "is", currSumE, currSumD, currSumT)

        # register the best result when it is encountered
        if int(one_section_limits[0]) < currSumD < int(one_section_limits[1]) \
                and int(one_section_limits[2]) < currSumT < int(one_section_limits[3]) \
                and int(one_section_limits[4]) < currSumE < int(one_section_limits[5]) \
                and end - begin > bestEnd - bestBegin:
            bestBegin, bestEnd, bestSumT, bestSumD, bestSumE = begin, end, currSumT, currSumD, currSumE

        # try to expand the window to the right
        if currSumD < int(one_section_limits[1]) and currSumT < int(one_section_limits[3])\
                and currSumE < int(one_section_limits[5]):
            end += 1
            if end < N:
                currSumD += distance_[end]
                currSumT += time_[end]
                currSumE += elevation_[end]

        # else shrink the window from the left
        else:
            currSumD -= distance_[begin]
            currSumT -= time_[begin]
            currSumE -= elevation_[begin]
            begin += 1
    return bestBegin, bestEnd, bestSumE, bestSumD, bestSumT


# 확인
print("input_list\n", input_list, "\n")
print("one_section_limits\n", one_section_limits + "\n")
print("hike_limits\n", hike_limits + "\n")
print("N : ", N, "\n")
print("all \n", all, "\n", len(all))

print("isCampSite\n", isCampSite, "\n", len(isCampSite))
print("elevation\n", elevation, "\n", len(elevation))
print("distance\n", distance, "\n", len(distance))
print("time\n", time, "\n", len(time))
print("endPoint\n", endPoint, "\n", len(endPoint))
findPossibleSection(isCampSite, elevation, distance, time)
