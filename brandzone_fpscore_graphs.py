import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re
import os

# 📥 Veriyi yükle
df = pd.read_csv("Mobiles Dataset (2025).csv", encoding="ISO-8859-1")

# Fiyat kolonlarını bul ve temizle
price_columns = [col for col in df.columns if "Launched Price" in col]

def clean_price(value):
    cleaned = re.sub(r"[^\d.]", "", str(value))
    return float(cleaned) if cleaned else None

for col in price_columns:
    df[col] = df[col].apply(clean_price)

# Kur dönüşümü (USD)
df["Launched Price (Pakistan)"] = df["Launched Price (Pakistan)"] / 280
df["Launched Price (India)"] = df["Launched Price (India)"] / 83
df["Launched Price (China)"] = df["Launched Price (China)"] / 7.2
df["Launched Price (Dubai)"] = df["Launched Price (Dubai)"] / 3.67

# RAM, Batarya, Kamera
df["RAM (GB)"] = df["RAM"].astype(str).str.extract(r'(\d+)').astype(float)
df["Battery (mAh)"] = df["Battery Capacity"].astype(str).str.extract(r'(\d{4,5})').astype(float)
df["Camera (MP)"] = df["Back Camera"].astype(str).str.extract(r'(\d{2,3})').astype(float)

# Skor
df["KingScore"] = (df["RAM (GB)"] * 100) + df["Battery (mAh)"] + df["Camera (MP)"]
df["KingScore per Dollar"] = df["KingScore"] / df["Launched Price (USA)"]

# 📊 En iyi 10 cihazı seç
top_fp = df.sort_values(by="KingScore per Dollar", ascending=False).head(10)

# 📁 charts klasörünü oluştur
os.makedirs("charts", exist_ok=True)

# 📈 Grafik çiz
plt.figure(figsize=(12, 6))
plt.bar(top_fp["Model Name"], top_fp["KingScore per Dollar"], color="seagreen")
plt.title("Top 10 Value-for-Money Phones (KingScore per Dollar)")
plt.ylabel("KingScore / USD")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("charts/king_score_top10.png")
plt.close()

print("✅ Grafik kaydedildi: charts/king_score_top10.png")
