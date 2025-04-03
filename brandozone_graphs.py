import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import os

# 📥 1. Veriyi Yükle
df = pd.read_csv("Mobiles Dataset (2025).csv", encoding="ISO-8859-1")

# 🔍 2. Fiyat kolonlarını bul
price_columns = [col for col in df.columns if "Launched Price" in col]

# 🧼 3. Temizleme fonksiyonu
def clean_price(value):
    cleaned = re.sub(r'[^\d.]', '', str(value))
    return float(cleaned) if cleaned else np.nan

# 🚿 4. Fiyatları temizle
for col in price_columns:
    df[col] = df[col].apply(clean_price)

# 💱 5. Kur dönüşümleri
df["Launched Price (Pakistan)"] = df["Launched Price (Pakistan)"] / 280
df["Launched Price (India)"] = df["Launched Price (India)"] / 83
df["Launched Price (China)"] = df["Launched Price (China)"] / 7.2
df["Launched Price (Dubai)"] = df["Launched Price (Dubai)"] / 3.67
# USA zaten USD

# Döviz dönüşümünden sonra ekle 👇
df.loc[df["Model Name"] == "T21", "Launched Price (USA)"] = 217


# 🧮 6. Price Gap hesapla
df["Min Price"] = df[price_columns].min(axis=1)
df["Max Price"] = df[price_columns].max(axis=1)
df["Price Gap"] = df["Max Price"] - df["Min Price"]

# 🔁 7. Sayıları yuvarla
df["Min Price"] = df["Min Price"].round(0)
df["Max Price"] = df["Max Price"].round(0)
df["Price Gap"] = df["Price Gap"].round(0)
for col in price_columns:
    df[col] = df[col].round(0)

# 📊 8. Grafik için Top 10 Price Gap model
top_gap_models = df.sort_values(by="Price Gap", ascending=False).head(10)

# 📁 9. charts klasörü oluştur
os.makedirs("charts", exist_ok=True)

# 📈 10. Bar Chart çiz ve kaydet
plt.figure(figsize=(12, 6))
plt.bar(top_gap_models["Model Name"], top_gap_models["Price Gap"], color="crimson")
plt.title("Top 10 Price Gap by Model (Mobile BRANDZONE 2025)")
plt.ylabel("Price Gap (USD)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("charts/top_10_price_gap_models.png")
plt.close()

print("✅ Grafik kaydedildi: charts/top_10_price_gap_models.png")
