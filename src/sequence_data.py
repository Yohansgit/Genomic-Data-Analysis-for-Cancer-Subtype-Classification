import os
import pandas as pd

# Define paths
data_dir = r"C:\Projects\BRCA_ML_Project\Data\Raw_Data"
output_dir = r"C:\Projects\BRCA_ML_Project\Data\Output"

# Ensure output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def load_tpm():
    """
    Load TCGA-BRCA TPM gene expression data as a pandas DataFrame,
    with Ensembl_ID set as the index.
    """
    file_path = os.path.join(data_dir, "TCGA-BRCA.star_tpm.tsv.gz")
    
    print("Loading TPM gene expression file...")
    df = pd.read_csv(file_path, sep="\t", compression="gzip", low_memory=False)
    df.set_index('Ensembl_ID', inplace=True)
 
    return df


