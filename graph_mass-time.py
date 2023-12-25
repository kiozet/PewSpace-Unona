import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)


def animate(i):
    data = open('mass-time.txt', 'r').read()
    lines = data.split('\n')

    xs = []
    ys = []
    times = 1
    
    for line in lines:
        try:
            x, y = line.split(', ')
            
            if int(x) >= 21600:
                with open(f"results/mass/mass_time_day_{times}.txt", 'w') as f1:
                    f1.write(data)
                    f1.close()

                    xs = []
                    ys = []
                    
                    ax.clear()
                    
                    times += 1
                
                with open("mass-time.txt", "w") as f2:
                    print("skip 1 day")
                    f2.write(f"0, {y}\n")
                    f2.close()
                    
            xs.append(float(x))
            ys.append(float(y))
            
        except Exception as ex:
            pass

    ax.clear()
    ax.plot(xs, ys)

    plt.xlabel('t')
    plt.ylabel('m')
    plt.title('График массы ко времени полета')


ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()