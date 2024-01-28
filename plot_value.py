import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# Num of freq swept
freq_len = 200
length = freq_len + 1

# Declare arrays
x_axis = np.arange(length)
y_axis = np.zeros((length), dtype=int)


# Initialise matplotlib
fig, ax = plt.subplots()
line, = ax.plot([], [], 'o', markersize=1)  # Initialize an empty line


ax.set(xlim=[0, freq_len], ylim=[0, 600], xlabel='Frequency', ylabel='Amplitude')



def process_arrays(x_axis, y_axis):
    # Random value to y-axis
    y_axis[:] = np.random.randint(low=150, high=550, size=(length))  # Update y_axis in-place


def init():
    line.set_data([], [])
    return line,

def update(frame):
    process_arrays(x_axis, y_axis)

    # Update the data of the line
    line.set_data(x_axis, y_axis)

    return line,



# Main function
if __name__ == "__main__":
    
    ani = animation.FuncAnimation(fig, update, frames=None, init_func=init, blit=True, interval=100, cache_frame_data=False)
    plt.show()
