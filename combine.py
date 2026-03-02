import pandas as pd
import os
from tqdm import tqdm

# Define the paths based on your folders
benign_folder = 'CCCS-CIC-Benign-CSVs/'
malicious_folder = 'CCCS-CIC-Malicious-CSVs/'

# 1. Process Benign Files (Label 0)
benign_files = [f for f in os.listdir(benign_folder) if f.endswith('.csv')]
benign_list = []

print("Reading Benign files...")
for file in tqdm(benign_files, desc="Benign Progress"):
    df = pd.read_csv(os.path.join(benign_folder, file))
    df['label'] = 0
    benign_list.append(df)
    df = df.astype('float32', errors='ignore')

print("Combining Benign data...")
benign_combined = pd.concat(benign_list, ignore_index=True)
benign_combined.to_csv('benign_dataset.csv', index=False)
print(f"Saved: benign_dataset.csv ({len(benign_combined)} rows)")



# 2. Process Malicious Files (Multiclass Labels 1-14)
malicious_files = sorted([f for f in os.listdir(malicious_folder) if f.endswith('.csv')])
malicious_list = []
mapping = {}

print("\nReading Malicious files...")
for index, file in enumerate(tqdm(malicious_files, desc="Malicious Progress")):
    label_value = index + 1
    class_name = file.replace('.csv', '')
    mapping[class_name] = label_value
    
    df = pd.read_csv(os.path.join(malicious_folder, file))
    df['label'] = label_value
    malicious_list.append(df)
    df = df.astype('float32', errors='ignore')

print("Combining Malicious data...")
malicious_combined = pd.concat(malicious_list, ignore_index=True)
malicious_combined.to_csv('malicious_multiclass_dataset.csv', index=False)

print(f"\nSaved: malicious_multiclass_dataset.csv ({len(malicious_combined)} rows)")
print("\nFinal Label Mapping:")
for name, val in mapping.items():
    print(f"Label {val}: {name}")