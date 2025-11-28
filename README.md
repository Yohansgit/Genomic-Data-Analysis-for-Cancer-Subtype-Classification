
### 🧬 Genomic Data Analysis for Cancer Subtype Classification

This project focuses on high-dimensional genomics data, build interpretable ML models, and translate scientific findings into actionable insights for R&D and clinical teams. It combines real TCGA-BRCA gene expression data, dimensionality reduction, supervised modeling, and biomarker discovery.

### 🎯 Objective
Classify breast cancer subtypes using genomic (RNA-seq) features and identify biomarker genes that drive biological differences.

## Part 1: Quick Overview
A video walkthrough for scientific communication, an interactive visualization for data exploration, and a public notebook for technical validation.

## Part 2: Executive Summary (The "Scientific So What?")
Fictional Client: Head of Bioinformatics, 'Genoma Therapeutics' (R&D)

# The Problem:
Cancer is not one disease; it's a complex set of genomic abnormalities. Different subtypes (e.g., of breast cancer) can look identical under a microscope but respond very differently to treatment. We need a robust, computational method to classify tumors based on their core genomic signatures to advance our drug discovery pipeline.
# The Solution:
I developed a machine learning pipeline to analyze high-dimensional (20,000+ features) gene expression data from The Cancer Genome Atlas (TCGA-BRCA). The pipeline classifies tumors and, more importantly, identifies the key biomarkers driving that classification.
# The Outcome: 
The model (a Random Forest classifier) can distinguish between cancer subtypes (Luminal A, Luminal B, HER2-positive, Basal-like, Normal) with 93% accuracy. The analysis also identified a novel set of 50 key gene biomarkers that are the most powerful predictors, providing a validated list of new targets for our therapeutic research teams.

## 🚀 Part 3: Technical & Scientific Workflow (The "How?")
1. Project Architecture:
A high-level overview of the end-to-end scientific analysis pipeline.
2. Strategic Tech Choices:
●	Why Dimensionality Reduction (PCA)?
It is impossible for a human to visualize 20,000 features. PCA was essential to compress this high-dimensional data, allowing us to "see" the data. In this project, we reduced 51 PAM50 genes (selected from the original 33,473 genes) to 2 principal components, which captured 55.7% of the total variance. As shown in the "Findings" section, this step confirmed that distinct tumor subtypes form visible, separable clusters based on their genomic profiles, validating that the PAM50 gene set contains strong subtype-specific signals.
●	Why Random Forest?
This model was chosen for two key reasons: 1) It excels at handling "wide" data (more features than samples) without overfitting, and 2) Its built-in 'feature importance' mechanism is a powerful, validated method for interpreting the model and identifying the specific gene biomarkers driving the classification.

## 📈 Part 4: Insights Deep Dive (The "What Did You Find?")
**🧩 Finding 1: PCA Confirms Distinct Genomic Signatures**
●	Insight: Dimensionality reduction via PCA confirmed that the major breast cancer subtypes (e.g., Luminal A, Luminal B, HER2-positive, Basal-like) are not just arbitrary labels. By projecting the data from 51 PAM50 genes into 2 principal components, which captured 55.7% of the total variance, we observed distinct, separable clusters corresponding to each subtype. This demonstrates that these subtypes are driven by reproducible genomic signatures rather than random variation, validating the biological relevance of the PAM50 gene set. They form distinct, separable clusters based only on their gene expression profiles.

**🤖 Finding 2: Model Achieves 92% Classification Accuracy**
●	Insight: The tuned Random Forest classifier successfully learned these genomic signatures, achieving 92% overall accuracy. The model was most successful at identifying the 'Basal-like' (Triple-Negative) subtype (95% precision), which is critical for guiding aggressive treatment.

**🧬 Finding 3: Identification of Novel Biomarkers**
●	Insight: By analyzing the model's feature importances, I identified a small subset of 50 genes (out of 33,000+) that hold over 80% of the predictive power. This provides a focused list of potential biomarkers for developing a faster, cheaper diagnostic panel.

## 🎯 Part 5: Actionable Recommendations (The "Now What?")
**●	For R&D Leadership:**
○	Action: The 93% accuracy validates that genomic subtyping is a viable strategy. The next step is to validate this model on an independent, internal (e.g., in-house patient) dataset.
**●	For the Biology/Lab Team:**
○	Action: Prioritize lab validation (e.g., qPCR, Western Blot) for the top 10 biomarkers (ESR1, SFRP1, KRT5, KRT14, FOXA1, KRT17, FOXC1, GPR160, EGFR, NAT1) identified by the model. These are the most promising targets for new therapeutic research.
**●	For the Data Science/Bioinformatics Team:**
○	Action: Explore more advanced deep learning models (e.g., a Variational Autoencoder or a Graph Neural Network) for feature extraction, which may provide even more nuanced biomarkers than traditional feature importance.

## Part 6: Repository & How to Run
This is the standard "how-to" section for a tech lead who wants to audit the code.
1. Repository Structure:
├── 📂 notebooks/
│   ├── 🔗 01_Data_Preprocessing_and_PCA.ipynb
│   ├── 🔗 02_Model_Training_and_Biomarker_ID.ipynb
├── 📂 data/
│   └── 📄 README.md  (Explains how to download TCGA-BRCA data from GDC portal)
├── 📂 images/
│   ├── 🖼️ architecture_flowchart.png
│   ├── 🖼️ pca_3d_plot.png
│   ├── 🖼️ confusion_matrix.png
│   └── 🖼️ feature_importance_top20.png
└── 🔗 requirements.txt

## 🧠 Why This Project Matters

Cancer subtypes often look identical histologically but respond differently to therapy. This project demonstrates how computational approaches can:
- Reduce diagnostic ambiguity
- Support targeted therapy decisions  
- Accelerate drug discovery pipelines
- Identify novel biological insights hidden in high-dimensional gene data

### Dataset
- Source: TCGA BRCA cohort
- Samples: ~1,000 tumor samples
- Features: ~33,472 genes (raw counts → normalized → scaled)
- Labels: PAM50 intrinsic gene signature for setsubtype annotations
- Metadata: demographics, clinical, histology,

## 📂 Repository Structure
├── notebooks/
│ ├── 01_Data_Preprocessing_and_PCA.ipynb
│ ├── 02_Model_Training_and_Biomarker_ID.ipynb
│
├── data/
│ └── README.md # Instructions to download TCGA-BRCA data
│
├── images/
│ ├── architecture_flowchart.png
│ ├── pca_3d_plot.png
│ ├── confusion_matrix.png
│ └── feature_importance_top20.png
│
└── requirements.txt

## ⚙️ Installation & Usage
**Create Environment**
python -m venv .venv
source .venv/bin/activate 
.venv\Scripts\activate   

**Download TCGA-BRCA data**
instructions in `data/README.md

**Install Dependencies**
pip install -r requirements.txt

**Run Analysis**
python src/preprocessing.py
python src/models.py

**Run Preprocessing and modeling**
notebooks/01_Data_Preprocessing_and_PCA.ipynb  
notebooks/02_Model_Training_and_Biomarker_ID.ipynb
Explore visualizations in the `images/` directory

## References

## License

