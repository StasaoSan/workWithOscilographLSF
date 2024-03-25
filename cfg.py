import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import medfilt, savgol_filter, butter, filtfilt

# Путь к файлу
NoiseFile = 'DS0001N.LSF'
MathFile = 'DS0001M.LSF'
SignalFile = 'DS0001S.LSF'


# Параметры фильтра (низкочастотный фильтр с нулевой фазой)
fs = 100
order = 6
cutoff = 2.3

# Параметры фильтра (медианный)
KernelSize = 51

# Параметры фильтра (Савицкого-Голея)
WindowLenght = 51
Polyorder = 3