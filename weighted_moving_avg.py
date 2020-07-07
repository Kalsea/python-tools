def weighted_moving_avg(df, start_col = None, end_col = None, win_size = None, inverted = False, lag_days = 0):

    alpha = 2 / (win_size + 1)

    if inverted:
        win_arr = pd.Series([(1-alpha)**x for x in range(win_size)])
    else:
        win_arr = pd.Series([(1-alpha)**x for x in reversed(range(win_size))])
    
    denominator = win_arr.sum()

    for col in range(start_col, end_col):

        arr = df.iloc[:, col]
        ewa_length = df.shape[0]-(win_size-1)-lag_days

        temp_arr = arr.copy()
        out_arr = arr.copy()
        
        for x in range(ewa_length):
            out_arr.iloc[x+(win_size-1)+lag_days] = (win_arr * temp_arr.iloc[x:x+win_size].reset_index(drop=True)).sum() / denominator

        df.iloc[:, col] = out_arr

        print(col)