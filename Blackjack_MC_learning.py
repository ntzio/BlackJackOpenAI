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

qv_td_table = np.zeros((21,10,2,2)) #This creates our Q-value look-up table
returnSum   = 0

alpha = 0.1
epsilon = 1.
gamma = 1.0

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
            act = np.argmax(qv_td_table[state[0]-1, state[1]-1, int(state[2]),:]) #select the best action

        state_new, reward, endsim, info = env.step(act)
        if endsim:
            q_next = 0
        else:
            q_next = np.max(qv_td_table[state_new[0]-1, state_new[1]-1, int(state_new[2]),:])
        qv_td_table[state[0]-1, state[1]-1, int(state[2]),act] += alpha*(reward + gamma*q_next  -  qv_td_table[state[0]-1, state[1]-1, int(state[2]),act])
        state = state_new
    epsilon = epsilon*0.9999
   

    returnSum = returnSum + reward
    if (i % 100 == 0 and i > 0):    
       print "Episode: ", i, "Average Return: ", returnSum/ float(i)
       returnSum = 0
    
visualizeValue(qv_mc_table)
