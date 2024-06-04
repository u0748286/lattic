import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation
from functools import partial
from matplotlib.lines import Line2D

import draw_car
plt.ion()  # Turn on interactive mode

car_initial_x = 0
car_initial_y = 50 
# 轮子的参数
wheel_length = draw_car.wheel_length  # 轮子的长度
car_width,car_height = draw_car.car_width,draw_car.car_height 
# Animation settings
fps = 60
speed = 0.5

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 10))

# Set the display limits
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
x = 0
y = 50 
# Create a rectangle that initially appears on the left side of the screen
car = patches.Rectangle((car_initial_x, car_initial_y), car_width, car_height, fc='blue')
ax.add_patch(car)
wheels = [
    Line2D([car_initial_x, car_initial_x + wheel_length], [car_initial_y, car_initial_y], color='black'),
    Line2D([car_initial_x, car_initial_x + wheel_length], [car_initial_y + car_height, car_initial_y + car_height], color='black'),
    Line2D([car_initial_x + car_width - wheel_length, car_initial_x + car_width], [car_initial_y, car_initial_y], color='black'),
    Line2D([car_initial_x + car_width - wheel_length, car_initial_x + car_width], [car_initial_y + car_height, car_initial_y + car_height], color='black')
]

for wheel in wheels:
    ax.add_line(wheel)
# Flag to control car movement
moving = False



# Function to handle keyboard events
def on_key(event):
    global moving
    if event.key == 'r':
        moving = not moving
        

# Connect keyboard event
cid = fig.canvas.mpl_connect('key_press_event', on_key)
wrapped_update = partial(draw_car.update, car=car, wheels=wheels,speed = speed)
# Create and start animation
ani = FuncAnimation(fig, wrapped_update, frames=np.linspace(0, 100, 100),blit=True, interval=1000/fps)

plt.pause(100)
plt.close()
