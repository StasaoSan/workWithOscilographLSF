from filters.index_work import *

def calculate_graph_data(savgol_filtered_signal):
    avg_hi, avg_low = calculate_avg_hi_lo(savgol_filtered_signal)
    x_data = []
    y_data = []
    indexes1, indexes2 = map(filter_indexes, extract_indexes(savgol_filtered_signal))
    indexes = sorted([0] + indexes1 + indexes2 + [9980])

    # Генерация данных графика
    for i in range(len(indexes) - 1):
        x_data.extend([indexes[i], indexes[i+1]])
        y_data.extend([avg_low, avg_low] if i % 2 == 0 else [avg_hi, avg_hi])
        if i < len(indexes) - 2:
            x_data.append(indexes[i+1])
            y_data.append(avg_hi if i % 2 == 0 else avg_low)

    return x_data, y_data, avg_hi, avg_low
