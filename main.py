import sys
from datetime import datetime

import pandas as pd


def calculate_time_difference(file_path):
    df = pd.read_excel(file_path, header=None)

    time_column = df.iloc[:, df.columns.get_loc(35)]
    time_values = pd.to_datetime(time_column, format='%H:%M:%S', errors='coerce')
    time_values = time_values.dropna()

    time_diff_array_in_minutes = \
        [
            (t - datetime.strptime('09:00:00', '%H:%M:%S'))
            .total_seconds() / 60 for t in time_values
        ]
    total_time_in_minutes = sum(time_diff_array_in_minutes)
    return total_time_in_minutes / 60


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python script_name.py <excel_file_path>")
        sys.exit(1)

    excel_file_path = sys.argv[1]
    result = calculate_time_difference(excel_file_path)
    print(f'\nTotal time difference in hours: {result}')
