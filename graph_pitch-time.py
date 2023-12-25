import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)


def animate(i):
    data = open('pitch-time.txt', 'r').read()
    lines = data.split('\n')

    xs = []
    ys = []
    times = 1

    for line in lines:
        try:
            x, y = line.split(', ')
            
            if int(x) >= 21600:
                with open(f"results/pitch/pitch_day_{times}.txt", 'w') as file:
                    file.write(data)
                    file.close()

                    xs = []
                    ys = []
                    
                    ax.clear()
                    
                    times += 1
                    
                with open("pitch-time.txt", 'w') as file:
                    file.write(f"0, {y}\n")
                    file.close()
                    
            xs.append(float(x))
            ys.append(float(y))
        except:
            pass

    ax.clear()
    ax.plot(xs, ys)

    plt.xlabel('t')
    plt.ylabel('angle')
    plt.title('График угла полета ко времени полета')


ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()