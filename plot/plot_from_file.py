from file.file import *

def createPlotFromFile(filePath, name):
    HeaderParams = read_lsf_header(filePath)
    Voltages = read_waveform_data(filePath, HeaderParams)[4:]

    print(f'{name.upper()} header: {HeaderParams}')
    print(f"UNPACKED DATA: {Voltages}")

    plt.figure(figsize=(10, 6))
    plt.plot(Voltages, label='Waveform')
    plt.xlabel('Sample Number')
    plt.ylabel('Voltage (V)')
    plt.title(f'{name} waveform')
    plt.legend()
    plt.grid(True)
    plt.show()
