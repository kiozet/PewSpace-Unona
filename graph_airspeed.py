import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)


def animate(i):
    data = open('air-speed.txt', 'r').read()
    lines = data.split('\n')

    xs = []
    ys = []
    times = 1
    
    for line in lines:
        try:
            x, y = line.split(', ')
            
            if int(x) >= 21600:
                with open(f"results/airspeed/airspeed_day_{times}", 'w') as file:
                    file.write(data)
                    file.close()
                    
                    xs = []
                    ys = []
                    
                    ax.clear()
                    
                    times += 1
                
                with open("air-speed.txt", "w") as file:
                    file.write(f"0, {y}\n")
                    file.close()
                    
            xs.append(float(x))
            ys.append(float(y))
        except:
            pass

    ax.clear()
    ax.plot(xs, ys)

    plt.xlabel('t')
    plt.ylabel('v')
    plt.title('График скорости ко времени полета')


ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()