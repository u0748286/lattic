from matplotlib.lines import Line2D
import matplotlib.patches as patches
car_width = 8
car_height = 5
# 轮子的参数
wheel_length = 2  # 轮子的长度
# Function to update animation
def update(frame,car,wheels,speed):
   
    print(int(frame));
   
    new_x = car.get_x() + speed
    car.set_x(new_x)
    # 更新轮子的位置
    wheels[0].set_xdata([new_x, new_x + wheel_length])
    wheels[1].set_xdata([new_x, new_x + wheel_length])
    wheels[2].set_xdata([new_x + car_width - wheel_length, new_x + car_width])
    wheels[3].set_xdata([new_x + car_width - wheel_length, new_x + car_width])
        
        
    return [car, *wheels]