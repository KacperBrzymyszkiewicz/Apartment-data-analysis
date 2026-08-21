import os
import pandas as pd

data = []
cols_num = 0
for file in os.listdir("./data"):
    if file.endswith(".csv"):
        df = pd.read_csv(os.path.join("./data", file))
        if cols_num == 0:
            cols_num = df.shape[1]
            data.append(df)
        elif cols_num == df.shape[1]:
            data.append(df)
        else:
            print(f"{file} has a different number of columns")
data = pd.concat(data,ignore_index=True)
data["priceForSquareMeter"] = round(data["price"]/data["squareMeters"],2)
print(data.columns.tolist())
print(data["city"].value_counts())
# print(data["priceForSquareMeter"])
# print(data["price"].describe())
