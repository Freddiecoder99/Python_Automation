import pandas as pd


def read_excel(file_path):
    df = pd.read_excel(file_path)
    print("Reading Excel File:")
    print(df)
    return
