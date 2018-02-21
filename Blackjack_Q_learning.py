import gym
import numpy as np
from visualizeValue import visualizeValue
env = gym.make('Blackjack-v0')

#n_a = env.action_space.n
n_s = env.observation_space
print n_s

epochs = 500000 # Number of episodes/plays
epsilon = 1. # E-greedy
gamma = 1.0 # Discount factor 

qv_mc_table = np.zeros((21,10,2,2)) #This creates our Q-value look-up table
sa_count    = np.zeros((21,10,2,2)) #Record how many times we've seen a given state-action pair.
returnSum   = 0

for i in range(epochs):
    state  = env.reset() # Initialize new game; observe current state
    endsim = False
    reward = 0
   
    vs = []
    va = []
    while not endsim:
        # E-greedy policy
        if (np.random.random() < epsilon or len(vs) == 0):
            act = np.random.randint(0,2)
        else:
            act = np.argmax(qv_mc_table[state[0]-1, state[1]-1, int(state[2]),:]) #select the best action

        sa_count[state[0]-1, state[1]-1, int(state[2]),act] +=1
        vs.append(state)
        va.append(act)
        
        state, reward, endsim, info = env.step(act)
    epsilon = epsilon*0.9999
    # Update Q values of the visited states
    for s, a in zip(vs,va):
        qv_mc_table[s[0]-1, s[1]-1, int(s[2]),a] = qv_mc_table[s[0]-1, s[1]-1, int(s[2]),a]+ (1./sa_count[s[0]-1, s[1]-1, int(s[2]),a])*(reward - qv_mc_table[s[0]-1, s[1]-1, int(s[2]),a])

    returnSum = returnSum + reward
    if (i % 100 == 0 and i > 0):    
       print "Episode: ", i, "Average Return: ", returnSum/ float(i)
       returnSum = 0
    
print('____________________________________________________________')
print('|==========================================================|')
print('|=================== No Usable Ace ========================|')
print('|==========================================================|')
print('|===================    Dealer     ========================|')
print('|----------------------------------------------------------|')
print('| Player |  1 |  2 |  3 |  4 |  5 |  6 |  7 |  8 |  9 | 10 |')
print('|----------------------------------------------------------|')
for i in range(11,21):
    s = '|   '+str(i+1)+'   |'
    for j in range(10):
        a = np.argmax(qv_mc_table[i, j, 0,:]) #select the best action
        if a == 0:
            s += '  '+'\033[2;31;48mS\033[30m'+' |'
        else:
            s += '  '+'\033[2;32;48mH\033[30m'+' |'
    print s
    print('|----------------------------------------------------------|')
print('|==========================================================|')

print('____________________________________________________________')
print('|==========================================================|')
print('|===================   Usable Ace  ========================|')
print('|==========================================================|')
print('|===================    Dealer     ========================|')
print('|----------------------------------------------------------|')
print('| Player |  1 |  2 |  3 |  4 |  5 |  6 |  7 |  8 |  9 | 10 |')
print('|----------------------------------------------------------|')
for i in range(11,21):
    s = '|   '+str(i+1)+'   |'
    for j in range(10):
        a = np.argmax(qv_mc_table[i, j, 1,:]) #select the best action
        if a == 0:
            s += '  '+'\033[2;31;48mS\033[30m'+' |'
        else:
            s += '  '+'\033[2;32;48mH\033[30m'+' |'
    print s
    print('|----------------------------------------------------------|')
print('|==========================================================|')
  
visualizeValue(qv_mc_table)
