# import pandas as pd

# drop samples (columns) with too low reads number
# range in reverse order, because columns are dropped immediately
# and columns index would change if the drop start from the beginning


def reads_treshold(data_frame, minimum_reads):
    for col_no in reversed(range(4, len(data_frame.iloc[1, :]))):
        if data_frame.iloc[:, col_no].sum() < minimum_reads:
            data_frame.drop(columns=data_frame.columns[col_no], inplace=True)
    return data_frame
