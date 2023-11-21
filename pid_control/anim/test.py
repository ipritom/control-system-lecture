import matplotlib.pyplot as plt
import time



def update_plot(x, y):
  # Generate new data.
   

  # Update the plot.
    plt.clf()
    
    plt.plot(x, y)
    plt.draw()
    plt.pause(0.02)

  # Pause for a few seconds.
#   time.sleep(0.5)


x = []
y = []
# plt.ion()
for i in range(6):
    a = i
    b = 2*i**0.5
    print(a, b)
    x.append(i)
    y.append(b)
    update_plot(x, y)

plt.show()