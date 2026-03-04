
"""
import pandas as pd
import glob
from tqdm import tqdm


mal_files = glob.glob("CCCS-CIC-Malicious-CSVs/*.csv")

# First, get family sizes
family_sizes = {}
print("🔹 Reading family sizes...")


mal_list = []


for f in tqdm(mal_files, desc="Sampling malware families"):
    df = pd.read_csv(f, header=None)

    mal_list.append(df)
    print(f"{f} → original: {len(df)}, sampled: {len(df)}")

malware_100k = pd.concat(mal_list, ignore_index=True)
malware_100k["label"] = 1

print("\n🔹 Saving malware_binary.csv ...")
malware_100k.to_csv("malware_binary.csv", index=False)

print("✅ Done.")
print("Final malware shape:", malware_100k.shape)
"""

import pandas as pd
import glob
from tqdm import tqdm


benign_files = glob.glob("CCCS-CIC-Benign-CSVs/*.csv")

# First, get family sizes
family_sizes = {}
print("🔹 Reading family sizes...")


mal_list = []


for f in tqdm(benign_files, desc="Sampling benign families"):
    df = pd.read_csv(f, header=None)

    mal_list.append(df)
    print(f"{f} → original: {len(df)}, sampled: {len(df)}")

benign= pd.concat(mal_list, ignore_index=True)
benign["label"] = 0

print("\n🔹 Saving benign.csv ...")
benign.to_csv("benign.csv", index=False)

print("✅ Done.")
print("Final benign shape:", benign.shape)