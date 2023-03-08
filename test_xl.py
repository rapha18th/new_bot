import pandas as pd
import numpy as np


def get_dataframes(fn):
    """
    Returns 3 dataframes from the 3 tables given inside excel file fn.
    """

    # (1) Read file
    df_start = pd.read_excel(fn, engine="openpyxl")
    df = df_start.copy()  # preserve df_start, just in case we need it later
    # print(df.to_string())  # study layout

    # (2) Clean df
    # reset column index, so we can see 0, 1, 2 ...
    df = pd.DataFrame(np.vstack([df.columns, df]))
    df = df.drop([0], axis=1)  # drop index column 0, it is not needed
    df = df.dropna(how='all')  # drop rows if all cells are empty
    # reset row index so we can see the correct row no. 0, 1, ...
    df = df.reset_index(drop=True)
    # reset col index so we can see the correct col no. 0, 1, ...
    df = pd.DataFrame(np.vstack([df.columns, df]))

    # (3) Tasks
    # We have 3 dataframes to create:
    # 1) df1 is for the first table the one with "Description".
    # 2) df2 is the one with the first "Sku Description:".
    # 3) df3 is the one with the second "Sku Description:".

    # (4) Get all the indexes (row and col) of "Description" and "Sku Description:" texts,
    # we will use it to extract data in order to create dataframes df1, df2 and df3.

    # Get the index of "Description" we will get row index and col index from it, by knowing
    # the row index, we will be able to extract at correct row index on this particular table.
    i_desc = df.where(df == 'Inventory').dropna(
        how='all').dropna(how='all', axis=1)

    # Assume that there is only one "Description" and this is true according to the given sample excel files.
    i_desc_row = i_desc.index[0]
    # print(f'row index of "Description": {i_desc_row}')

    # Get the index of "Sku Description:".
    i_sku = df.where(df == 'Customer:').dropna(
        how='all').dropna(how='all', axis=1)

    # There are 2 "Sku Description:", get the row indexes of each.
    i_sku_row = i_sku.index
    # print(f'row indexes of "Sku Description:": {i_sku_row}')

    i_sku_row_1 = i_sku_row[0]
    i_sku_row_2 = i_sku_row[1]
    # print(f'i_sku_row_1: {i_sku_row_1}, i_sku_row_2: {i_sku_row_2}')

    # There are 2 "Sku Description:", get the col indexes of each.
    i_sku_col = i_sku.columns
    # print(f'col indexes of "Sku Description:": {i_sku_col}')

    if len(i_sku_col) == 2:
        i_sku_col_1 = i_sku_col[0]
        i_sku_col_2 = i_sku_col[1]
    else:
        i_sku_col_1 = i_sku_col[0]
        i_sku_col_2 = i_sku_col_1

    # print(f'i_sku_col_1: {i_sku_col_1}, i_sku_col_2: {i_sku_col_2}')

    # (5) Create df1
    cols = ['Description', 'Qty', 'Price', 'Total']
    # [start_row:end_row, start_col:end_col]
    df1 = df.iloc[i_desc_row+1: i_sku_row_1-2, 0:4]
    df1.columns = cols
    # print(df1)
    # reset the row index so we can see 0, 1, ...
    df1 = df1.reset_index(drop=True)
    # print(df1)

    # (6) Create df2
    cols = ['Customer:', 'Quantity:']
    df2 = df.iloc[i_sku_row_1+1: i_sku_row_2, i_sku_col_1:i_sku_col_1+2]
    df2.columns = cols
    df2 = df2.reset_index(drop=True)
    # print(df2)

    # (7) Create df3
    cols = ['Customer:', 'Quantity:']
    df3 = df.iloc[i_sku_row_2+1:, i_sku_col_2:i_sku_col_2+2]
    df3.columns = cols
    df3 = df3.reset_index(drop=True)
    # print(df3)

    return df1, df2, df3


def process_file():
    # fn = 'F:\\Downloads\\dell.xlsx'
    fn = 'Asmara_Coffee.xlsx'
    desc_df, sku1_df, sku2_df = get_dataframes(fn)

    print(f'file: {fn}')
    print(f'desc_df:\n{desc_df}\n')
    print(f'sku1_df:\n{sku1_df}\n')
    print(f'sku2_df:\n{sku2_df}\n')


# Start
process_file()
