# Spam Text Classification RNN
Seto Aryotomo (A11.2021.13747/A11.4706)

## Prasyarat
- **Python 3.8 atau lebih baru**
- **pip** sudah terinstal

## Cara Instalasi

1. Clone repository ini:
   ```bash
   git clone https://github.com/setoaryotomo/spam-text-classification.git
   cd spam-text-classification
   ```
   
2. Install dependensi:
   ```bash
   pip install -r requirements.txt
   ```
   
3. Cara Menjalankan Proyek:
   ```bash
   streamlit run index.py
   ```

## Dataset
- **text**: teks yang akan diklasifikasikan.
- **label**: label untuk teks tersebut (`spam` atau `not spam`).

Contoh:
```csv
text,label
"Congratulations! You won a prize!",spam
"Meeting rescheduled to 3 PM",not spam
```
