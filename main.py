# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer

# Load the dataset (Assuming it's a CSV file)
# Replace 'your_dataset.csv' with the actual dataset path
df = pd.read_csv('your_dataset.csv')

# Step 1: Data Preprocessing

# Handle missing values (Impute or drop them based on your strategy)
imputer = SimpleImputer(strategy='mean')
df[['MIN_CONC', 'MAX_CONC', 'LN_IC50']] = imputer.fit_transform(df[['MIN_CONC', 'MAX_CONC', 'LN_IC50']])

# Drop columns that are irrelevant for model building (like IDs)
df = df.drop(['SNO', 'NLME_RESULT_ID', 'NLME_CURVE_ID', 'COMPANY_ID', 'SANGER_MODEL_ID', 'COSMIC_ID', 
              'CELL_LINE_NAME', 'GENE_LIST'], axis=1)

# Encode categorical variables (such as TISSUE, DRUG_NAME, PUTATIVE_TARGET, etc.)
categorical_cols = ['TCGA_DESC', 'TISSUE', 'TISSUE_SUBTYPE', 'DRUG_NAME', 'PUTATIVE_TARGET', 'PATHWAY_NAME', 
                    'GENE', 'TRANSCRIPT', 'cDNA', 'AA_POSITION']