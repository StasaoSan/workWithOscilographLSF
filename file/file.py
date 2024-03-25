from cfg import *

def read_lsf_header(file_path):
    with open(file_path, 'rb') as file:
        content = file.read()
        waveform_data_index = content.find(b'Waveform Data;') + len('Waveform Data;')
        header_content = content[:waveform_data_index].decode('ascii')
        header_params = {}
        for param in header_content.split(';'):
            if ',' in param:
                key, value = param.split(',', 1)
                header_params[key.strip()] = value.strip()
        return header_params


def read_waveform_data(file_path, header_params):
    with open(file_path, 'rb') as file:
        waveform_data_index = file.read().find(b'Waveform Data;') + len('Waveform Data;')
        file.seek(waveform_data_index)

        raw_data = file.read()

        data_points = np.frombuffer(raw_data, dtype=np.int16)

        vertical_scale = float(header_params['Vertical Scale'])
        ad_factor = 25  # Заданный AD Factor - коэффициент преобразования (max int compare to real max voltages)
        voltages = (data_points / ad_factor) * vertical_scale

        return voltages