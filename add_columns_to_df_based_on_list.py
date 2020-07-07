def add_columns_based_list(df, col_list, in_value = None):

    df = pd.concat( [df, pd.DataFrame(data = in_value, index = df.index, columns = col_list)], axis=1)

    return df