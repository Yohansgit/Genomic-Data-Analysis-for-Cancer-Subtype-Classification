import os
import pandas as pd

# Define paths
data_dir = r"C:\Projects\BRCA_ML_Project\Data\Raw_Data"
output_dir = r"C:\Projects\BRCA_ML_Project\Data\Output"

# Ensure output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def load_clinical():

    file_path = os.path.join(data_dir, "TCGA-BRCA.clinical.tsv.gz")
 
    df = pd.read_csv(file_path, sep="\t", compression="gzip", low_memory=False)
   
    print("Loaded successfully!")
    print("Shape:", df.shape)

    return df


