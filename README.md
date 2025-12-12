<!-- Project Banner -->
<p align="center">
  <img src="https://raw.githubusercontent.com/Yohansgit/Genomic-Data-Analysis-for-Cancer-Subtype-Classification/main/images/project_banner.png" alt="Genomic Cancer Classification Banner" width="200"  style="object-fit:cover;"/>
</p>

<p align="center">
  <em>High-dimensional Genomics Analysis for Breast Cancer Subtype Classification</em>
</p>

<!-- Badges -->
[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.2.2-orange?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![TCGA](https://img.shields.io/badge/TCGA-Data-red?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNgYAAAAAMAASsJTYQAAAAASUVORK5CYII=)](https://www.cancer.gov/tcga)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

#### 🧬 Part 1: Project Overview

This project focuses on high-dimensional **genomics data analysis**, building interpretable **machine learning models**, and translating scientific findings into actionable insights for **R&D and clinical teams**. It integrates real **TCGA-BRCA gene expression data**, dimensionality reduction, supervised modeling, and biomarker discovery.  

| Video Walkthrough (5 min)            | Interactive PCA Visualization      | Public Notebook                  |
| ------------------------------------ | ---------------------------------- | -------------------------------- |
| *[Screenshot here]*                  | *[Screenshot here]*                | *[Screenshot here]*              |
| **[▶ Click Here to Watch the Loom]** | **[✨ Interact with the PCA Plot]** | **[📓 Open the Colab Notebook]** |

**Target Audience:** R&D Scientists, Bioinformatics Leads, & Pharma Hiring Managers

---
### 🎯 Objective    
Classify breast cancer subtypes using RNA-seq features and identify biomarker genes driving **biologically meaningful differences**, enabling **targeted therapy decisions**.   

---
#### 🚀 Part 2: Executive Summary (The "Scientific So What?")   
**Fictional Client**: Head of Bioinformatics, 'Genoma Therapeutics' (R&D)    

#### 🎯 The Problem:   
Cancer is not one disease; it's a complex set of genomic abnormalities. Histologically similar tumors can respond differently to treatment. We need a robust, computational method to classify tumors based on their core genomic signatures to advance our drug discovery pipeline.   

#### 💡 The Solution:   

A **machine learning pipeline** was developed to analyze **high-dimensional transcriptome data** (60,660 genes × 1,106 samples). After filtering low-expression and low-variance genes, the dataset was reduced to **33,472 features**.  
- **Full transcriptome** was used for feature selection and biomarker discovery.  
- **PAM50 gene set (50 genes)** was used post hoc to **validate known molecular subtypes**.  
- A **Random Forest classifier** was trained to predict breast cancer subtypes and identify the **top predictive genes**.

#### 📈 The Outcome: 
- **93% accuracy** in cancer subtype classification can distinguish between cancer subtypes (Luminal A, Luminal B, HER2-positive, Basal-like, Normal)     
- **50 key biomarkers** identified with >80% predictive power     
- **Validated target list** for therapeutic research teams      
  
#### 🏆 Model Performance  

##### 📊 Comprehensive Evaluation Metrics

| Metric | Score | Clinical Significance |   
|--------|-------|----------------------|
| **Overall Accuracy** | **93%** | High diagnostic reliability |
| **Balanced Accuracy** | 86.4% | Robust across imbalanced subtypes |
| **Macro F1-score** | 88.54% | Consistent performance across classes |
| **ROC-AUC (OvR)** | **98.6%** | Excellent class separation capability |

#### 📈 Part 3: Technical & Scientific Workflow (The "How?")
**1. Project Architecture:**  
A high-level overview of the end-to-end scientific analysis pipeline.   
```mermaid
flowchart TD
%% --- Horizontal pipeline steps ---
subgraph TOPROW [ ]
    direction LR
    A1(1. Define Objective):::start
    A2([2. 🔄 Data Acquisition<br>RNA-seq, Clinical, Gencode]):::data
    A3([3. ⚙️ Preprocess Data]):::process
    A4([4. 📊 PCA Analysis]):::process
    A5([5. ✨ Feature Selection on Full Transcriptome]):::process
    A6[6. 📝 Select Model - Random Forest]:::model
end

%% --- Vertical flow after model selection ---
A6 --> B1([7. 🤖 Train Model]):::model
B1 --> B2([8. Cross Validation]):::model
B2 --> C1{9. Performance OK?}:::decision

C1 -- "No" --> D1([10. 🔁 Hyperparameter Tuning]):::model
D1 -.->|Tune & Retry| A6
C1 -- "Yes" --> E1{{11. Identify Biomarkers<br>Top 50 Genes}}:::output
E1 --> F1(12. 🔬 External Validation):::output
F1 --> G1[/13. Performance Assessment<br>Biological & Statistical/]:::monitor
G1 -- "Insufficient Performance?" --> H1([14. 🔁 Model Refinement]):::monitor
H1 -.->|Cycle| A6

%% --- Horizontal links for first row ---
A1 --> A2 --> A3 --> A4 --> A5 --> A6

%% --- Dotted feedback arrows for loops ---
linkStyle 12 stroke:#1565C0,stroke-width:2px,stroke-dasharray: 5 5
linkStyle 14 stroke:#1565C0,stroke-width:2px,stroke-dasharray: 5 5

%% --- Node Styles ---
classDef start fill:#4CAF50,stroke:#1B5E20,color:#fff;
classDef data fill:#FF8A80,stroke:#C62828,color:#000;
classDef process fill:#26C6DA,stroke:#00838F,color:#000;
classDef model fill:#FF7043,stroke:#E64A19,color:#fff;
classDef decision fill:#FDD835,stroke:#F9A825,color:#000;
classDef output fill:#66BB6A,stroke:#2E7D32,color:#fff;
classDef monitor fill:#26A69A,stroke:#004D40,color:#fff;
```

**2. Strategic Tech Choices:**   

**🔷	Why Dimensionality Reduction (PCA)?**     
      ● Visualizing 33,000+ features is impossible without dimensionality reduction.
      ● PCA: Visualize high-dimensional data; PCA on 50 PAM50 genes captures 56.7% variance in first two components.                 
   
**🔷	Why Random Forest?**  
      ● Handles high-dimensional “wide” data without overfitting.    
      ● Provides feature importance for biomarker discovery.   

#### 📈 Part 4: Insights Deep Dive (The "What Did You Find?")   

**🧩 Finding 1: Clear Genomic Separation via PCA**   

**Insight:**    
Dimensionality reduction via **PCA** confirmed that the major breast cancer subtypes (**Luminal A, Luminal B, HER2-positive, Basal-like**) form distinct and reproducible clusters. Using the **50 PAM50 genes**, projection onto the first two principal components captured **56.7%** of variance, clearly separating the subtypes. This confirms that PAM50 genes reflect meaningful biological differences.

**🤖 Finding 2: Model Achieves 93% Classification Accuracy**

**Insight:**          
The tuned Random Forest classifier successfully captured the genomic signatures, achieving **93% overall accuracy**. The model performed exceptionally well at identifying the **Basal-like (Triple-Negative)** subtype, with **100% precision**, which is particularly important for guiding aggressive treatment decisions.

**🧬 Finding 3: High Value Novel Biomarkers Identified**   

**Insight:**         
Analysis of the model's **feature importances** revealed **50 genes** that collectively accounted for over 80% of the predictive power. This provides a focused set of potential biomarkers for developing faster, more cost-effective diagnostic panels.
**Top genes:** `ACTR3B, ANLN, BAG1, BCL2, BIRC5, BLVRA, CCNB1, CCNE1, CDC20`  

**Validation:**
**ACTR3B** – involved in actin cytoskeleton organization, linked to tumor cell migration.
**ANLN** – associated with cell proliferation and known to be overexpressed in aggressive breast cancers.
**BAG1** – modulates apoptosis, relevant in cancer cell survival.
**BCL2** – classic anti-apoptotic gene, commonly upregulated in Luminal tumors.
**BIRC5** (Survivin) – inhibits apoptosis and is linked to poor prognosis in breast cancer.
**BLVRA** – implicated in oxidative stress pathways, potentially contributing to tumor progression.
**CCNB1** & **CCNE1** – key regulators of the cell cycle, associated with proliferation in aggressive subtypes.
**CDC20** – controls mitotic progression, frequently overexpressed in basal-like tumors.

These validations show that the model not only identifies statistically important genes but also captures **biologically meaningful signals** consistent with known breast cancer pathways.

---
#### 🎯 Part 5: Actionable Recommendations (The "Now What?")

**For R&D Leadership:**

**➡️** The 93% accuracy validates that genomic subtyping is a viable strategy. The next step is to validate this model on an independent, internal (e.g., in-house patient samples) to confirm clinical applicability and robustness.

**For the Biology/Lab Team:**

**➡️** Prioritize lab validation (e.g., qPCR, Western Blot) for the top 10 biomarkers (`ESR1, MLPH, FOXA1 , KRT14, UBE2T, SFRP1, FOXC1, KRT5 , BIRC5, NAT1`) identified by the model. Focus on **subtype-specific expression**, particularly for Luminal and Basal-like tumors, to guide the development of faster, targeted diagnostic assays and therapeutic strategies.

**For the Data Science/Bioinformatics Team:**

**➡️** Investigate the **Basal-like** cluster for potential sub-segmentation, as the PCA plot indicates heterogeneity within this group that current therapies may not address. Additionally, explore advanced models such as Variational Autoencoders or Graph Neural Networks to extract deeper genomic features and uncover subtle biomarkers beyond traditional feature importance.

#### 📁 Part 6: Repository & How to Run

#### Repository Structure:
```bash
Genomic-Data-Analysis-for-Cancer-Subtype-Classification/
├── 📂 data/Output/
│   └── 📄 README.md
├── 📂 notebooks/
│   ├── 🔗 01_Data_Preprocessing_and_PCA.ipynb
│   ├── 🔗 02_Model_Training_and_Biomarker_ID.ipynb
├── 📂 images/
│   ├── 🖼️ architecture_flowchart.png
│   ├── 🖼️ pca_3d_plot.png
│   ├── 🖼️ confusion_matrix.png
│   └── 🖼️ feature_importance_top20.png
├── src
└── 🔗 requirements.txt
```

#### 🧠 Why This Project Matters

Breast cancer subtypes often look identical histologically but respond differently to therapy. This project demonstrates how computational genomics helps:
- Improve diagnostic precision   
- Support targeted therapy selection    
- Accelerate drug discovery   
- Reveal novel biological insights hidden in high-dimensional data  

#### 📊 Dataset
**● Source:** TCGA-BRCA cohort   
**● Samples:** ~1,000 tumor samples   
**● Features:** ~60,660 genes (raw → normalized → scaled)   
**● Labels:** PAM50 intrinsic gene signature for subtype annotations   
**● Metadata:** clinical + demographic   

#### ⚙️ Installation & Usage
**1. Create Environment**
python -m venv .venv
source .venv/bin/activate   # macOS/Linux    
.venv\Scripts\activate      # Windows              

**2. Download TCGA-BRCA Data**
(instructions provided in `data/README.md`   

**3. Install Dependencies**
pip install -r requirements.txt

**4. Run Analysis Scripts**
python src/preprocessing.py  
python src/models.py  

**5. Explore Notebooks**      
● `notebooks/01_Data_Preprocessing_and_PCA.ipynb`        
● `notebooks/02_Model_Training_and_Biomarker_ID.ipynb`   

#### 📚 References
Wang, L., et al. (2025). Advancements in multi-omics integration for breast cancer subtyping. Nature Communications, 16(1).           
Pereira, B., et al. (2023). Deep learning approaches for cancer subtype classification from genomic data. Nature Machine Intelligence, 5(3), 245-258.        
Pereira, B., et al. (2016). The somatic mutation profiles of 2,433 breast cancers refine their genomic and transcriptomic landscapes. Nature Communications, 7, 11479.          
The Cancer Genome Atlas Network. (2012). Comprehensive molecular portraits of human breast tumours. Nature, 490(7418), 61-70.       
Curtis, C., et al. (2012). The genomic and transcriptomic architecture of 2,000 breast tumours reveals novel subgroups. Nature, 486(7403), 346-352.     
Parker, J.S., et al. (2009). Supervised risk predictor of breast cancer based on intrinsic subtypes. Journal of Clinical Oncology, 27(8), 1160-1167.    
Pedregosa, F., et al. (2011). Scikit-learn: Machine Learning in Python. Journal of Machine Learning Research, 12, 2825-2830.    

#### 📄 License
MIT License - See `LICENSE` file for details
