from cfg import *

def plot_graph(x_data, y_data, avg_hi, avg_low):
    plt.figure(figsize=(10, 5))
    plt.plot(x_data, y_data, drawstyle='steps-post', label='Meander Line')
    plt.title('Meander Waveform')
    plt.xlabel('Sample Number')
    plt.ylabel('Voltage (V)')
    plt.grid(True)
    plt.legend()
    plt.show()