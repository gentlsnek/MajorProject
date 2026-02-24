import pandas as pd

dt = pd.read_parquet('maliciousdataset.parquet')

print(dt.shape)