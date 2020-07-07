def del_col_by_index(df, start_in, end_in):

    list_to_del = df[df.columns[start_in:end_in]]
    df = df.drop(list_to_del, axis = 1)
    return df