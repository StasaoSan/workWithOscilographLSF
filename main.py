from cfg import *
from filters.calculate_data import calculate_graph_data
from filters.lo_pass_filter import butter_low_pass_filter_zero_phase
from plot.plot_from_data import *
from plot.plot_from_file import *
from plot.plot_real_meandr import plot_graph

# Построение изначальных графиков
createPlotFromFile(SignalFile, "Signal")
createPlotFromFile(NoiseFile, "Noise")
createPlotFromFile(MathFile, "Math")

# Извлечение данных из файлов
mathVoltages = read_waveform_data(MathFile, read_lsf_header(MathFile))[4:]
noiseVoltages = read_waveform_data(NoiseFile, read_lsf_header(NoiseFile))[4:]
signalVoltages = read_waveform_data(SignalFile, read_lsf_header(SignalFile))[4:]

# Применение низкочастотного фильтра
filtered_signal_zero_phase = butter_low_pass_filter_zero_phase(mathVoltages, cutoff, fs, order)[10:]
# Применение медианного фильтра
median_filtered_signal = medfilt(filtered_signal_zero_phase, kernel_size=KernelSize)[5:]
# Применение фильтра Савицкого-Голея
savgol_filtered_signal = savgol_filter(median_filtered_signal, window_length=WindowLenght, polyorder=Polyorder)[5:]

# Построение полученных графиков
createPlotFromData(filtered_signal_zero_phase, "Lo-pass filter")
createPlotFromData(median_filtered_signal, "Median")
createPlotFromData(savgol_filtered_signal, "Savog")

# Построение итогового графика меандра
x_data, y_data, avg_hi, avg_low = calculate_graph_data(savgol_filtered_signal)
plot_graph(x_data, y_data, avg_hi, avg_low)
