import pandas as pd
import os

# Define the file path
file_path = r"C:\Projects\BRCA_ML_Project\Data\Raw_Data\brca_pam50"

# Make sure the file exists
if not os.path.exists(file_path):
    raise FileNotFoundError(f"The file does not exist: {file_path}")

# Load the data
# Adjust sep='\t' if it's a TSV, or remove sep if it's CSV
phenotype = pd.read_csv(file_path, sep='\t')

# Print basic info
print("Shape of the phenotype data:", phenotype.shape)
print("Columns in the phenotype data:", phenotype.columns.tolist())

# Look for PAM50/subtype columns
subtype_cols = [col for col in phenotype.columns if 'subtype' in col.lower() or 'pam50' in col.lower()]
print("Columns containing subtype info:", subtype_cols)

# Preview the subtype column(s)
for col in subtype_cols:
    print(f"\nPreview of {col}:")
    print(phenotype[col].value_counts())
