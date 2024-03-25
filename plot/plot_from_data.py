from file.file import *

def createPlotFromData(data, name):
    plt.figure(figsize=(10, 6))
    plt.plot(data, label='Waveform')
    plt.xlabel('Sample Number')
    plt.ylabel('Voltage (V)')
    plt.title(f'{name} waveform')
    plt.legend()
    plt.grid(True)
    plt.show()