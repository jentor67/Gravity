#!/usr/bin/python3
import matplotlib.pyplot as plt
import numpy as np

re = 6371000
length = 3  # meters
r1 = re + length
r2 = re

G = 6.67430*(10** -11)  # Gravitational Constant of the universe
m1=5.972168*(10**24)
m2=1
v1=0

r = np.linspace(r1, r2, 100)
v2 = (2*G*m1*(r1-r)/(r1*r))**.5

'''
v3 = (2*G*m1*(r1-r2)/(r1*r2))**.5
print(v3)
'''

plt.xlabel('Radius (m)')
plt.ylabel('Velocity (m/s)')
plt.plot(r, v2)  # Plot the chart
plt.show()  # display
