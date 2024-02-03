#!/usr/bin/python3
import matplotlib.pyplot as plt
import numpy as np
#  From a stationary point above Earth with zero velocity what will the final speed be

re = 6371000
length = 30000000  # meters
r1 = re + length
r2 = re
ge = 9.81

G = 6.67430*(10** -11)  # Gravitational Constant of the universe
m1=5.972168*(10**24)
m2=1
v1=0

r = np.linspace(r1, r2, 100)
v1 = ((-r+re+length)*2*ge)**.5
v2 = (2*G*m1*(r1-r)/(r1*r))**.5
v3 = (2*G*m1*((1/r)-(1/r1)))**.5
'''
v3 = (2*G*m1*(r1-r2)/(r1*r2))**.5
print(v3)
'''

plt.xlabel('Radius (m)')
plt.ylabel('Velocity (m/s)')
plt.plot(r, v1, label='Constant gravity')  # Plot the chart
plt.plot(r, v2, label='Energy method')  # Plot the chart
plt.plot(r, v3, label='DE method')  # Plot the chart

plt.legend()
plt.show()  # display
