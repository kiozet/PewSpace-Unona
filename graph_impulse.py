import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)


def animate(i):
    data = open('impulse-time.txt', 'r').read()
    lines = data.split('\n')

    xs = []
    ys = []
    times = 1

    for line in lines:
        try:
            x, y = line.split(', ')
            
            
            if int(x) >= 21600: # /6 + clear gr
                
                xs = []
                ys = []
                
                ax.clear()
                
                with open(f"results/impulse/impulse_day_{times}.txt", 'w') as file:
                    file.write(data)
                    file.close()

                times += 1
                    
                with open("impulse-time.txt", "w") as file:
                    file.write(f"0, {y}\n")
                    file.close()
                    
            xs.append(float(x))
            ys.append(float(y))
                
            
        except Exception as ex:
            pass

    ax.clear()
    ax.plot(xs, ys)

    
    plt.xlabel('m')
    plt.ylabel('p')
    plt.title('График импульса ко времени полета')


ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()