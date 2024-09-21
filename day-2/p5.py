# # differentiating states and capitals

# import sys
#method-1-------------------------------------------
# states=[]
# capitals=[]
# for i in range(1,len(sys.argv),2):
#     states.append(sys.argv[i])
#     capitals.append(sys.argv[i+1])

# print("States:", states)
# print("Capitals:", capitals)

#method-2------------------------------------------

# import sys

# states=[]
# capitals=[]
# for i in range(1,len(sys.argv)):
#     arguments=sys.argv[i].split()
#     states.append(arguments[0])
#     capitals.append(arguments[1])
# print(states)
# print(capitals)

#method-3---------------------------------

import sys
def split_states_capitals():
    states=[]
    capitals=[]
    for i in range(1,len(sys.argv)):
        argument = sys.argv[i]
        index_of_space = argument.find('')
        states.append(argument[:index_of_space])
        capitals.append(argument[:index_of_space+1:])
    print('%-15s %s'%("states","capitals"))
    print("-" * 27)
    i = 0
    while states: