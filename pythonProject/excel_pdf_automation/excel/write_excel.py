import pandas as pd


def write_excel(data, file_path):
    df = pd.DataFrame(data)
    df.to_excel(file_path, index=False)
    print(f"Excel written to {file_path}")
