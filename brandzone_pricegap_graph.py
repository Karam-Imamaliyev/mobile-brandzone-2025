import pandas as pd
import matplotlib.pyplot as plt
import os
import re

# Veriyi yükle
df = pd.read_csv("Mobiles Dataset (2025).csv", encoding="ISO-8859-1")

# Fiyat kolonlarını bul ve temizle
price_columns = [col for col in df.columns if "Launched Price" in col]

def clean_price(value):
    cleaned = re.sub(r"[^\d.]", "", str(value))
    return float(cleaned) if cleaned else None

for col in price_columns:
    df[col] = df[col].apply(clean_price)

# Price Gap hesapla
df["Min Price"] = df[price_columns].min(axis=1)
df["Max Price"] = df[price_columns].max(axis=1)
df["Price Gap"] = df["Max Price"] - df["Min Price"]

# charts klasörü varsa kullan, yoksa oluştur
os.makedirs("charts", exist_ok=True)

# Top 10 kazık model
top_gap_models = df.sort_values(by="Price Gap", ascending=False).head(10)

# Grafik
plt.figure(figsize=(12, 6))
plt.bar(top_gap_models["Model Name"], top_gap_models["Price Gap"], color="crimson")
plt.title("Top 10 Price Gap by Model (Mobile BRANDZONE 2025)")
plt.ylabel("Price Gap (USD)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("charts/top_10_price_gap_models.png")
plt.close()

print("✅ Grafik çizildi: charts/top_10_price_gap_models.png")


# Marka başına ortalama fiyat farkı
brand_gap = df.groupby("Company Name")["Price Gap"].mean().sort_values(ascending=False)

print("\n💣 Marka Bazlı Ortalama Fiyat Farkı (Kazıklama Sırası):")
print(brand_gap)
