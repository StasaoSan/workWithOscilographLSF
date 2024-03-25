def filter_indexes(indexes):
    if not indexes:
        return []

    filtered_indexes = [indexes[0]]
    for i in range(1, len(indexes)):
        if indexes[i] - filtered_indexes[-1] >= 10:
            filtered_indexes.append(indexes[i])
    return filtered_indexes

def extract_indexes(savgol_filtered_signal, threshold=2):
    indexes1 = []
    indexes2 = []

    for i in range(21, len(savgol_filtered_signal)):
        if (savgol_filtered_signal[i] - savgol_filtered_signal[i-20] > threshold):
            indexes1.append(i)
        elif (savgol_filtered_signal[i-20] - savgol_filtered_signal[i] > threshold):
            indexes2.append(i)

    return indexes1, indexes2


def calculate_avg_hi_lo(savgol_filtered_signal):
    indexes1, indexes2 = map(filter_indexes, extract_indexes(savgol_filtered_signal))
    combined_indexes = sorted([0] + indexes1 + indexes2 + [9980])
    avg_hi = []
    avg_low = []
    k = True  # Для чередования между avg_hi и avg_low

    for i in range(len(combined_indexes) - 1):
        start, end = combined_indexes[i], combined_indexes[i + 1]
        interval_avg = sum(savgol_filtered_signal[start:end]) / (end - start)
        if k:
            avg_low.append(interval_avg)
        else:
            avg_hi.append(interval_avg)
        k = not k
    avg_hi_result = sum(avg_hi) / len(avg_hi) if avg_hi else 0
    avg_low_result = sum(avg_low) / len(avg_low) if avg_low else 0
    return avg_hi_result, avg_low_result