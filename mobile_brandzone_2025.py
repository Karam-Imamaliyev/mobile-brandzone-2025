import pandas as pd
import re
import numpy as np

# CSV dosyasını yükle
df = pd.read_csv("Mobiles Dataset (2025).csv", encoding="ISO-8859-1")

# Fiyat kolonlarını bul
price_columns = [col for col in df.columns if "Launched Price" in col]

# Temizleme fonksiyonu
def clean_price(value):
    cleaned = re.sub(r'[^\d.]', '', str(value))
    return float(cleaned) if cleaned else np.nan

# Tüm fiyatları temizle
for col in price_columns:
    df[col] = df[col].apply(clean_price)

# Sonuç kontrol
print(df[price_columns].head())

# Marka başına kaç model var?
brand_counts = df['Company Name'].value_counts()
print("Marka başına model sayısı:")
print(brand_counts)

# Marka başına ortalama ABD fiyatı
brand_avg_usa_price = df.groupby('Company Name')['Launched Price (USA)'].mean()
print("\nMarka başına ortalama USA fiyatı (USD):")
print(brand_avg_usa_price)
