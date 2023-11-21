import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# create a figure and an axis
fig, ax = plt.subplots()



# define the x and y data
x = []
y = []

# create an empty line plot
line, = ax.plot(x, y)

# define the function to update the plot
def update(i):
    a = i
    b = 2*i**0.5
    print(a, b)
    x.append(i)
    y.append(b)
    # shift the y data by i
    
   
    # update the line data
    line.set_data(x, y)
    ax.autoscale()
    
    return line,

# create an animation object
ani = animation.FuncAnimation(fig, update, frames=10, interval=100)

# show the plot
plt.show()