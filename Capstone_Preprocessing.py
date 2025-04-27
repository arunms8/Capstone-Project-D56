import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.impute import SimpleImputer
import joblib
# Load the dataset into a pandas DataFrame
df = pd.read_csv('./secondary_data.csv', sep=';')
print(df.head())
# Explore dataset: shape, columns, data types
def data_explore(df):
    print("\nDataset Shape:", df.shape)
    print("Dataset Columns:", df.columns.tolist())
    print("\nData Types:\n", df.dtypes)
    
data_explore(df)