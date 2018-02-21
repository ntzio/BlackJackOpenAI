import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np

def visualizeValue(Q):
    
    fig = plt.figure(figsize=(20, 10),dpi=80)  
    x, y, z_usable_ace, z_no_usable_ace = [], [], [], [] 
    s1, s2, ace, actions = Q.shape
    
    for i in range(11,s1):
        for j in range(s2):
            y.append(i+1)
            x.append(j+1)
            z_usable_ace.append(np.max(Q[i,j,1,:]))
            z_no_usable_ace.append(np.max(Q[i,j,0,:]))
            
    ax = fig.add_subplot(1,2,1,projection='3d')
    ax.plot_trisurf(x, y, z_no_usable_ace, cmap=cm.jet)
    ax.set_xlabel('Dealer card', fontsize=20)
    ax.set_ylabel('Player sum', fontsize=20)
    ax.set_zlabel('State-Value', fontsize=20)
    ax.set_title('No Usable Ace', fontsize=20)
    ax.tick_params(axis='x', labelsize=15)
    ax.tick_params(axis='y', labelsize=15)
    ax.tick_params(axis='z', labelsize=15)

    
    ax = fig.add_subplot(1,2,2,projection='3d')
    ax.plot_trisurf(x, y, z_usable_ace, cmap=cm.jet)
    ax.set_xlabel('Dealer card', fontsize=20)
    ax.set_ylabel('Player sum', fontsize=20)
    ax.set_zlabel('State-Value', fontsize=20)
    ax.set_title('Usable Ace', fontsize=20)
    ax.tick_params(axis='x', labelsize=15)
    ax.tick_params(axis='y', labelsize=15)
    ax.tick_params(axis='z', labelsize=15)

    plt.show()
