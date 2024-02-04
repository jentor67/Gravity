#!/usr/bin/python3
import matplotlib.pyplot as plt
import numpy as np

# expore the function ( r1*r/(r1-r) ) ** (.5 + n) 
# where r < r1 and n are all positive integers

r0=110

r1 = 2
r2 = 1

r = np.linspace(r1, r2, 100)

plt.xlabel('variable r')
plt.ylabel('result')

for n in range(5):
    print(n)
    exp = .5+n

    fd = (r0*r)**exp
    fn = (r0-r)**exp
    
    ratio = fd/fn
    plt.plot(r, ratio, label='ratio' + str(n))  # Plot the chart
    """
    plt.plot(r, fd, label='function denominator')  # Plot the chart
    plt.plot(r, fn, label='function numerator')  # Plot the chart
    """

plt.legend()
plt.show()  # display
