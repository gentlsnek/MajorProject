import pandas as pd
import glob
import os
from tqdm import tqdm

mal_files = sorted(glob.glob("CCCS-CIC-Malicious-CSVs/*.csv"))

print("🔹 Reading malware families...")

mal_list = []
label_map = {}

for label_id, f in enumerate(tqdm(mal_files, desc="Processing malware families")):

    df = pd.read_csv(f, header=None)

    # get family name
    family_name = os.path.basename(f).replace(".csv", "")
    
    # store mapping
    label_map[label_id] = family_name

    # assign numeric label
    df["label"] = label_id + 1

    mal_list.append(df)

    print(f"{family_name} → label {label_id + 1}, samples: {len(df)}")

# combine all families
malware_multiclass = pd.concat(mal_list, ignore_index=True)

print("\n🔹 Saving malware_multiclass.csv ...")
malware_multiclass.to_csv("malware_multiclass.csv", index=False)

print("✅ Done.")
print("Final dataset shape:", malware_multiclass.shape)

print("\n🔹 Label Mapping (IMPORTANT for later):")
for k, v in label_map.items():
    print(f"{k} → {v}")