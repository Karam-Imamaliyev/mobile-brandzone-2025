import pandas as pd
import numpy as np
import re

# 📥 1. Veriyi yükle
df = pd.read_csv("Mobiles Dataset (2025).csv", encoding="ISO-8859-1")

# 🔍 2. Fiyat kolonlarını bul ve temizle
price_columns = [col for col in df.columns if "Launched Price" in col]

def clean_price(value):
    cleaned = re.sub(r"[^\d.]", "", str(value))
    return float(cleaned) if cleaned else None

for col in price_columns:
    df[col] = df[col].apply(clean_price)

# 💱 3. Kur dönüşümü (USD)
df["Launched Price (Pakistan)"] = df["Launched Price (Pakistan)"] / 280
df["Launched Price (India)"] = df["Launched Price (India)"] / 83
df["Launched Price (China)"] = df["Launched Price (China)"] / 7.2
df["Launched Price (Dubai)"] = df["Launched Price (Dubai)"] / 3.67

# Hatalı Nokia T21 fiyat düzeltmesi
df.loc[df["Model Name"] == "T21", "Launched Price (USA)"] = 217

# 🔁 4. Fiyatları yuvarla
for col in price_columns:
    df[col] = df[col].round(0)

# 🧠 5. Özellik kolonlarını çıkart

# RAM → "8 GB" → 8
df["RAM (GB)"] = df["RAM"].astype(str).str.extract(r'(\d+)').astype(float)

# Batarya → "5000 mAh" → 5000
df["Battery (mAh)"] = df["Battery Capacity"].astype(str).str.extract(r'(\d{4,5})').astype(float)

# Kamera → "50 MP + 2 MP" → 50
df["Camera (MP)"] = df["Back Camera"].astype(str).str.extract(r'(\d{2,3})').astype(float)

# 💥 6. KingScore hesapla
df["KingScore"] = (df["RAM (GB)"] * 100) + df["Battery (mAh)"] + df["Camera (MP)"]

# 💰 7. Fiyat başına performans
df["KingScore per Dollar"] = df["KingScore"] / df["Launched Price (USA)"]

# 🔝 8. En yüksek 10 F/P cihaz
top_fp = df.sort_values(by="KingScore per Dollar", ascending=False).head(10)

# 🖥️ 9. Sonuçları yazdır
print(top_fp[["Model Name", "RAM", "Battery Capacity", "Back Camera", "Launched Price (USA)", "KingScore", "KingScore per Dollar"]])
