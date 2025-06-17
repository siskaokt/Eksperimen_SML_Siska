# Import Library
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from ucimlrepo import fetch_ucirepo
import os

# Membuat fungsi Handle Outliers
def handle_outliers_iqr(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    return df[(df[column] >= lower) & (df[column] <= upper)]

# Membuat fungsi Automate
def automate_banknote_pipeline(save_path="banknote_preprocessing.csv"):
    # Fetch data
    dataset = fetch_ucirepo(id=267)
    X = dataset.data.features
    y = dataset.data.targets
    df = pd.concat([X, y], axis=1)

    # Drop data duplikat
    df.drop_duplicates(inplace=True)

    # Bersihkan outliers untuk kolom yang memiliki outlier
    columns_with_outliers = ['variance', 'curtosis', 'skewness']
    df_clean = df.copy()
    for col in columns_with_outliers:
        df_clean = handle_outliers_iqr(df_clean, col)

    # Standarisasi fitur X
    X_clean = df_clean.drop(columns='class')
    y_clean = df_clean['class']
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_clean)

    # Gabung kembali fitur & target
    df_scaled = pd.DataFrame(X_scaled, columns=X_clean.columns)
    df_scaled['class'] = y_clean.values

    # Simpan ke CSV
    df_scaled.to_csv(save_path, index=False)
    print(f"Dataset berhasil disimpan ke: {save_path}")
    print(f"Jumlah data akhir: {df_scaled.shape[0]} baris")

    return df_scaled

# Menjalankan automate
if __name__ == "__main__":
    automate_banknote_pipeline()