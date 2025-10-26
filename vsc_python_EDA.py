{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Connected to Python 3.13.7"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Data Awal:\n",
      "    ID          Nama  Usia        Kota  Pendapatan       Status  \\\n",
      "0  118  Pengguna_118    51  yogyakarta     9819256        Aktif   \n",
      "1   29   Pengguna_29    37     jakarta     4991886        Aktif   \n",
      "2  119  Pengguna_119    31       medan    19094979        Aktif   \n",
      "3   44   Pengguna_44    54    makassar    15843052  Tidak Aktif   \n",
      "4  124  Pengguna_124    26     bandung    20000000      Pending   \n",
      "\n",
      "  Tanggal Daftar  Tahun_Daftar  Bulan_Daftar  Hari_Daftar  \n",
      "0     2023-06-26          2023             6           26  \n",
      "1     2023-07-20          2023             7           20  \n",
      "2     2023-05-17          2023             5           17  \n",
      "3     2023-05-10          2023             5           10  \n",
      "4     2023-05-05          2023             5            5  \n",
      "\n",
      "Korelasi antara Usia dan Pendapatan: 0.02532547988457472\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "# Membaca file Excel\n",
    "df = pd.read_excel('data_bersih.xlsx')\n",
    "\n",
    "# Tampilkan beberapa baris awal\n",
    "print(\"Data Awal:\")\n",
    "print(df.head())\n",
    "\n",
    "# Hitung korelasi antara kolom Usia dan Pendapatan\n",
    "correlation = df['Usia'].corr(df['Pendapatan'])\n",
    "print(f\"\\nKorelasi antara Usia dan Pendapatan: {correlation}\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Data setelah dibersihkan:\n",
      "    ID          Nama  Usia        Kota  Pendapatan       Status  \\\n",
      "0  118  Pengguna_118    51  yogyakarta     9819256        Aktif   \n",
      "1   29   Pengguna_29    37     jakarta     4991886        Aktif   \n",
      "2  119  Pengguna_119    31       medan    19094979        Aktif   \n",
      "3   44   Pengguna_44    54    makassar    15843052  Tidak Aktif   \n",
      "4  124  Pengguna_124    26     bandung    20000000      Pending   \n",
      "\n",
      "  Tanggal Daftar  Tahun_Daftar  Bulan_Daftar  Hari_Daftar  \n",
      "0     2023-06-26          2023             6           26  \n",
      "1     2023-07-20          2023             7           20  \n",
      "2     2023-05-17          2023             5           17  \n",
      "3     2023-05-10          2023             5           10  \n",
      "4     2023-05-05          2023             5            5  \n",
      "\n",
      "Korelasi antara Usia dan Pendapatan (setelah data dibersihkan): 0.02532547988457472\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "# Baca file Excel\n",
    "df = pd.read_excel('data_bersih.xlsx')\n",
    "\n",
    "# Hapus baris yang memiliki data kosong (NaN)\n",
    "df = df.dropna()\n",
    "\n",
    "# (Opsional) kalau mau hapus duplikat juga\n",
    "df = df.drop_duplicates()\n",
    "\n",
    "# Tampilkan data setelah dibersihkan\n",
    "print(\"Data setelah dibersihkan:\")\n",
    "print(df.head())\n",
    "\n",
    "# Hitung korelasi antara kolom Usia dan Pendapatan\n",
    "correlation = df['Usia'].corr(df['Pendapatan'])\n",
    "print(f\"\\nKorelasi antara Usia dan Pendapatan (setelah data dibersihkan): {correlation}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Data setelah dibersihkan:\n",
      "    ID          Nama  Usia        Kota  Pendapatan       Status  \\\n",
      "1  118  Pengguna_118    51  yogyakarta     9819256        Aktif   \n",
      "2   29   Pengguna_29    37     jakarta     4991886        Aktif   \n",
      "3  119  Pengguna_119    31       medan    19094979        Aktif   \n",
      "4   44   Pengguna_44    54    makassar    15843052  Tidak Aktif   \n",
      "5  124  Pengguna_124    26     bandung    20000000      Pending   \n",
      "\n",
      "  Tanggal Daftar  Tahun_Daftar  Bulan_Daftar  Hari_Daftar  \n",
      "1     2023-06-26          2023             6           26  \n",
      "2     2023-07-20          2023             7           20  \n",
      "3     2023-05-17          2023             5           17  \n",
      "4     2023-05-10          2023             5           10  \n",
      "5     2023-05-05          2023             5            5  \n",
      "\n",
      "Korelasi antara Usia dan Pendapatan: 0.02532547988457472\n",
      "Koefisien determinasi (R-squared) antara Usia dan Pendapatan: 0.0006413799313839988\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "# Baca file Excel (pastikan file ada di folder yang sama)\n",
    "df = pd.read_excel('data_bersih.xlsx')\n",
    "\n",
    "# Hapus data kosong (NaN) dan duplikat agar datanya bersih\n",
    "df = df.dropna()\n",
    "df = df.drop_duplicates()\n",
    "\n",
    "# Reset index biar urut dari 1 lagi\n",
    "df = df.reset_index(drop=True)\n",
    "df.index = df.index + 1\n",
    "\n",
    "# Tampilkan 5 data pertama untuk memastikan berhasil dimuat\n",
    "print(\"Data setelah dibersihkan:\")\n",
    "print(df.head())\n",
    "\n",
    "# Hitung korelasi antara Usia dan Pendapatan\n",
    "correlation = df['Usia'].corr(df['Pendapatan'])\n",
    "print(f\"\\nKorelasi antara Usia dan Pendapatan: {correlation}\")\n",
    "\n",
    "# Hitung koefisien determinasi (R-squared)\n",
    "r_squared = correlation ** 2\n",
    "print(f\"Koefisien determinasi (R-squared) antara Usia dan Pendapatan: {r_squared}\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total data setelah dibersihkan: 150\n",
      "\n",
      "Korelasi antara Usia dan Pendapatan: 0.02532547988457472\n",
      "Koefisien determinasi (R-squared): 0.0006413799313839988\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "# Baca file Excel\n",
    "df = pd.read_excel('data_bersih.xlsx')\n",
    "\n",
    "# Hapus data kosong dan duplikat\n",
    "df = df.dropna()\n",
    "df = df.drop_duplicates()\n",
    "\n",
    "# Reset index biar rapi lagi\n",
    "df = df.reset_index(drop=True)\n",
    "df.index = df.index + 1\n",
    "\n",
    "# Tampilkan total data setelah dibersihkan\n",
    "print(\"Total data setelah dibersihkan:\", len(df))\n",
    "\n",
    "# Hitung korelasi antara Usia dan Pendapatan\n",
    "correlation = df['Usia'].corr(df['Pendapatan'])\n",
    "print(f\"\\nKorelasi antara Usia dan Pendapatan: {correlation}\")\n",
    "\n",
    "# Hitung koefisien determinasi (R-squared)\n",
    "r_squared = correlation ** 2\n",
    "print(f\"Koefisien determinasi (R-squared): {r_squared}\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total data setelah dibersihkan: 150\n",
      "\n",
      "Korelasi antara Usia dan Pendapatan: 0.025\n",
      "Koefisien determinasi (R-squared): 0.001\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "# Baca file Excel\n",
    "df = pd.read_excel('data_bersih.xlsx')\n",
    "\n",
    "# Hapus data kosong dan duplikat\n",
    "df = df.dropna()\n",
    "df = df.drop_duplicates()\n",
    "\n",
    "# Reset index biar rapi lagi\n",
    "df = df.reset_index(drop=True)\n",
    "df.index = df.index + 1\n",
    "\n",
    "# Total data setelah dibersihkan\n",
    "total_data = len(df)\n",
    "print(\"Total data setelah dibersihkan:\", total_data)\n",
    "\n",
    "# Hitung korelasi dan koefisien determinasi\n",
    "korelasi = df['Usia'].corr(df['Pendapatan'])\n",
    "r_squared = korelasi ** 2\n",
    "\n",
    "# Tampilkan hasil tapi dibulatkan 3 angka di belakang koma\n",
    "print(f\"\\nKorelasi antara Usia dan Pendapatan: {round(korelasi, 3)}\")\n",
    "print(f\"Koefisien determinasi (R-squared): {round(r_squared, 3)}\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "No kernel connected"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Dataset:\n",
      "    SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm      Species\n",
      "0              51            35             14             2  Iris-setosa\n",
      "1              49            30             14             2  Iris-setosa\n",
      "2              47            32             13             2  Iris-setosa\n",
      "3              46            31             15             2  Iris-setosa\n",
      "4              50            36             14             2  Iris-setosa\n",
      "5              54            39             17             4  Iris-setosa\n",
      "6              46            34             14             3  Iris-setosa\n",
      "7              50            34             15             2  Iris-setosa\n",
      "8              44            29             14             2  Iris-setosa\n",
      "9              49            31             15             1  Iris-setosa\n",
      "10             54            37             15             2  Iris-setosa\n",
      "11             48            34             16             2  Iris-setosa\n",
      "12             48            30             14             3  Iris-setosa\n",
      "13             43            30             11             1  Iris-setosa\n",
      "14             58            40             12             2  Iris-setosa\n",
      "Jumlah data training: 12\n",
      "Jumlah data testing: 3\n",
      "Akurasi model: 1.0\n",
      "\n",
      "Classification Report:\n",
      "              precision    recall  f1-score   support\n",
      "\n",
      " Iris-setosa       1.00      1.00      1.00         3\n",
      "\n",
      "    accuracy                           1.00         3\n",
      "   macro avg       1.00      1.00      1.00         3\n",
      "weighted avg       1.00      1.00      1.00         3\n",
      "\n",
      "\n",
      "Confusion Matrix:\n",
      "[[3]]\n",
      "Hasil prediksi vs data asli:\n",
      "Asli: Iris-setosa, Prediksi: Iris-setosa\n",
      "Asli: Iris-setosa, Prediksi: Iris-setosa\n",
      "Asli: Iris-setosa, Prediksi: Iris-setosa\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\Users\\ThinkPad\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages\\sklearn\\metrics\\_classification.py:534: UserWarning: A single label was found in 'y_true' and 'y_pred'. For the confusion matrix to have the correct shape, use the 'labels' parameter to pass all known labels.\n",
      "  warnings.warn(\n"
     ]
    }
   ],
   "source": [
    "# %%\n",
    "# 1. Import library yang dibutuhkan\n",
    "import pandas as pd\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.tree import DecisionTreeClassifier\n",
    "from sklearn.metrics import accuracy_score, classification_report, confusion_matrix\n",
    "\n",
    "# %%\n",
    "# 2. Buat dataset manual sesuai tabel di soal\n",
    "data = {\n",
    "    'SepalLengthCm': [51,49,47,46,50,54,46,50,44,49,54,48,48,43,58],\n",
    "    'SepalWidthCm': [35,30,32,31,36,39,34,34,29,31,37,34,30,30,40],\n",
    "    'PetalLengthCm': [14,14,13,15,14,17,14,15,14,15,15,16,14,11,12],\n",
    "    'PetalWidthCm': [2,2,2,2,2,4,3,2,2,1,2,2,3,1,2],\n",
    "    'Species': [\n",
    "        'Iris-setosa','Iris-setosa','Iris-setosa','Iris-setosa','Iris-setosa',\n",
    "        'Iris-setosa','Iris-setosa','Iris-setosa','Iris-setosa','Iris-setosa',\n",
    "        'Iris-setosa','Iris-setosa','Iris-setosa','Iris-setosa','Iris-setosa'\n",
    "    ]\n",
    "}\n",
    "\n",
    "df = pd.DataFrame(data)\n",
    "print(\"Dataset:\")\n",
    "print(df)\n",
    "\n",
    "# %%\n",
    "# 3. Pisahkan fitur (X) dan target (y)\n",
    "X = df[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]\n",
    "y = df['Species']\n",
    "\n",
    "# %%\n",
    "# 4. Bagi data menjadi 80% training dan 20% testing\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
    "\n",
    "print(\"Jumlah data training:\", len(X_train))\n",
    "print(\"Jumlah data testing:\", len(X_test))\n",
    "\n",
    "# %%\n",
    "# 5. Buat model Decision Tree\n",
    "model = DecisionTreeClassifier(random_state=42)\n",
    "model.fit(X_train, y_train)\n",
    "\n",
    "# %%\n",
    "# 6. Lakukan prediksi\n",
    "y_pred = model.predict(X_test)\n",
    "\n",
    "# %%\n",
    "# 7. Evaluasi model\n",
    "print(\"Akurasi model:\", accuracy_score(y_test, y_pred))\n",
    "print(\"\\nClassification Report:\")\n",
    "print(classification_report(y_test, y_pred))\n",
    "print(\"\\nConfusion Matrix:\")\n",
    "print(confusion_matrix(y_test, y_pred))\n",
    "\n",
    "# %%\n",
    "# 8. Uji model dengan data testing\n",
    "print(\"Hasil prediksi vs data asli:\")\n",
    "for real, pred in zip(y_test, y_pred):\n",
    "    print(f\"Asli: {real}, Prediksi: {pred}\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
