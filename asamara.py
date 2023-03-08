import pandas as pd
import numpy as np
from rich import print

asa = pd.ExcelFile("Asmara_Coffee.xlsx", engine="openpyxl")
sheet_ls = [sheet for sheet in asa.sheet_names]


print(sheet_ls)

df = pd.concat([pd.read_excel('Asmara_Coffee.xlsx', engine="openpyxl", sheet_name=sheet)
               for sheet in sheet_ls], ignore_index=True)

for i, sheet in enumerate(sheet_ls):
    globals()['a_df' + str(i + 1)
              ] = pd.read_excel('Asmara_Coffee.xlsx', engine="openpyxl", sheet_name=sheet)

print(df.head())
print(a_df2)
