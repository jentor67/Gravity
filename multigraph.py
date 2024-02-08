#!/usr/bin/python3
import matplotlib.pyplot as plt
import numpy as np
#  From a stationary point above Earth with zero velocity what will the final speed be


class CreateChart:


    def createChart(x, y, xName, yName, Label):
        
        plt.plot(x, y, label=Label)  # Plot the chart
        
        plt.xlabel(xName)
        plt.ylabel(yName)

        plt.legend()
        
re = 6371000
length = 30000000  # meters
r1 = re + length
r2 = re
ge = 9.81

G = 6.67430*(10** -11)  # Gravitational Constant of the universe
m1=5.972168*(10**24)
r = np.linspace(r1-.1*length, r2, 100)

lineChart = CreateChart
plt.rcParams['figure.figsize']  = [14,9]
plt.rcParams['figure.autolayout'] = True

ax1 = plt.subplot(221)
v3 = (2*G*m1*((1/r)-(1/r1)))**.5
g  = lineChart.createChart( r, v3, 'Radius (m)', 'Velocity (m/s)', \
        'Velocity' )

ax2 = plt.subplot(222)
vI = ( 2*G*m1*( (1/r) - (1/r1) ) )**(-.5)
h  = lineChart.createChart( r, vI, 'Radius (m)', 'Velocity Inv (m/s)^-1', \
        'Velocity -1' )

ax3 = plt.subplot(223)
a = G*m1/(r**2)
h  = lineChart.createChart( r, a, 'Radius (m)', 'Acceleration (m/s^2)', \
        'Acceleration' )


plt.show()  # display
