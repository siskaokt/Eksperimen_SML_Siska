# Eksperimen_SML_Siska
## Dataset
- **Nama**: Banknote Authentication Dataset
- **Sumber**: [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/267/banknote+authentication)
- **Fitur**:
  - `variance`
  - `skewness`
  - `curtosis`
  - `entropy`
- **Target**: `class` (0 = palsu, 1 = asli)

## Langkah Eksperimen
- Exploratory Data Analysis (EDA)
  - Statistik deskriptif
  - Visualisasi distribusi dan korelasi fitur
  - Deteksi outlier
- Preprocessing:
  - Menghapus data duplikat
  - Penanganan outlier (IQR)
  - Standardisasi fitur
- Penyimpanan dataset bersih ke CSV

## Automasi Preprocessing
File `automate_Krisdayanti Siska Oktavia Simbolon.py` berisi pipeline otomatis untuk preprocessing dataset, termasuk:
- Fetch dataset langsung dari UCI
- Hapus duplikat dan outlier
- Standardisasi fitur numerik
- Simpan hasil bersih ke `banknote_preprocessing.csv`

## 📁 File dalam Repo
- `Eksperimen_Krisdayanti Siska Oktavia Simbolon.ipynb`: notebook eksplorasi dan preprocessing
- `automate_Krisdayanti Siska Oktavia Simbolon.py`: pipeline otomatis
- `banknote.csv`: dataset asli
- `banknote_preprocessing.csv`: dataset hasil preprocessing
