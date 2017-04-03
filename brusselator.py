#
#       Yaroslav Bershatsky 2017
#
#       dx/dt = t       
#
#

import numpy as np
import matplotlib.pyplot as plt

def main():
    
    t_n = np.arange(0, 20, h)
    n = int(len(t_n))
    
    
    x = t_n * t_n / 2
    
    #print('x\n', x)
    
    t = t_n
    
    a_implicit = np.diag(3 * np.ones(n - 1), k = -1) + np.diag(-4 * np.ones(n), k = 0) + np.diag(np.ones(n - 1), k = 1) # implicit solution k = 2
    #a_implicit = np.diag(25/12 * np.ones(n - 1), k = -1) + np.diag(-4 * np.ones(n), k = 0) + np.diag(3 * np.ones(n - 1), k = 1) + np.diag(-4 / 3 * np.ones(n - 2), k = 2) + np.diag(1 / 4 * np.ones(n - 3), k = 3) # implicit solution k = 4
    
    a_explicit = np.diag(np.ones(n - 1), k = -1) + np.diag( -1 * np.ones(n), k = 0)  # explicit solution k = 1
    #a_explicit = np.diag(np.ones(n - 1), k = -1) + np.diag( -1 * np.ones(n - 1), k = 1)  # explicit solution k = 2
    #a_explicit = np.diag(1 / 3 * np.ones(n - 1), k = -1) + np.diag( 1/2 * np.ones(n), k = 0)+ np.diag(-1 * np.ones(n - 1), k = 1) + np.diag(1/6 * np.ones(n - 2), k = 2)  # explicit solution k = 3
       
    #print('a_implicit\n', a_implicit)
    #print('a_explicit\n', a_explicit)
    

    a_implicit_inv = np.linalg.inv(a_implicit)
    a_explicit_inv = np.linalg.inv(a_explicit)
    
    #print('a_inv\n', a_inv)
    #print('a_inv * a\n', np.dot(a_inv,a))
       
    x_implicit_n = -2 * h * np.dot(a_implicit_inv, t_n)
    x_explicit_n = -1 * h * np.dot(a_explicit_inv, t)
        
    #print(t,'\n', b,'\n', t + b)
    #print('x_n\n', x_n)
 
    fig = plt.figure(facecolor = 'white')
    plt.plot(x_implicit_n, t_n, linewidth = 1, label = 'Implicit solution')
    plt.plot(x_explicit_n, t_n, linewidth = 1, label = 'Explicit solution')
   
    plt.legend(fontsize = 12)
    plt.grid(True)
    plt.show()
if __name__ == '__main__':
    main()
