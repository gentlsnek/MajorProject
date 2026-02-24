import pandas as pd
import glob
from tqdm import tqdm
import pyarrow as pa
import pyarrow.parquet as pq
import os

chunk_size = 300_000
output_file = "maliciousdataset.parquet"

print("🔹 Loading malicious CSV files...")

mal_files = glob.glob("CCCS-CIC-Malicious-CSVs/*.csv")

parquet_writer = None
schema = None
col_names = None  # locked column names

for file in tqdm(mal_files, desc="Files"):
    filename = os.path.basename(file)

    for chunk in tqdm(
        pd.read_csv(file, header=None, chunksize=chunk_size, low_memory=False),
        desc=f"Chunks: {filename}",
        leave=False
    ):
        # force column names to strings
        if col_names is None:
            col_names = [str(c) for c in chunk.columns] + ["label"]
        chunk.columns = [str(c) for c in chunk.columns]

        # add label WITHOUT fragmentation
        label_col = pd.Series(1, index=chunk.index, name="label")
        chunk = pd.concat([chunk, label_col], axis=1)

        # lock schema from first chunk
        if schema is None:
            table = pa.Table.from_pandas(chunk, preserve_index=False)
            schema = table.schema
            parquet_writer = pq.ParquetWriter(output_file, schema)
        else:
            table = pa.Table.from_pandas(chunk, schema=schema, preserve_index=False)

        parquet_writer.write_table(table)

if parquet_writer:
    parquet_writer.close()

print("maliciousdataset.parquet saved.")
