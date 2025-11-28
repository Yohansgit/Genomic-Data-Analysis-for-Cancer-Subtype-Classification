# create_flowchart.py
from graphviz import Digraph
import os

def create_flowchart(output_folder=r"C:\Projects\BRCA_ML_Project\Data\Output"):
    # Ensure the folder exists
    os.makedirs(output_folder, exist_ok=True)
    
    output_path = os.path.join(output_folder, "brca_pipeline.png")
    
    dot = Digraph(comment='Breast Cancer Subtyping Pipeline', format='png')

    # Nodes
    dot.node('A', 'Data Collection\n(Clinical Data, Gene Expression)')
    dot.node('B', 'Data Preprocessing\n(Filter, Impute, Normalize)')
    dot.node('C', 'Dimensionality Reduction\n(PCA / Feature Selection)')
    dot.node('D', 'ML Model Training\n(Random Forest, Cross-validation)')
    dot.node('E', 'Model Evaluation\n(Accuracy, F1, ROC-AUC)')
    dot.node('F', 'Feature Importance\n(Gini, Permutation, SHAP)')
    dot.node('G', 'Biomarker Selection\n(Top Genes for Lab Validation)')
    dot.node('H', 'Actionable Recommendations\n(R&D, Lab, Data Science)')

    # Edges
    dot.edges(['AB', 'BC', 'CD', 'DE', 'EF', 'FG', 'GH'])

    # Style
    dot.attr(rankdir='TB', size='10')
    dot.attr('node', shape='box', style='filled', color='lightblue')

    # Render and save
    dot.render(filename=output_path, cleanup=True)
    print(f"Flowchart saved to: {output_path}")

if __name__ == "__main__":
    create_flowchart()
