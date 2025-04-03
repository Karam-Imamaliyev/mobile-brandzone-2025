import pandas as pd
import re

# 📥 Veriyi yükle
df = pd.read_csv("Mobiles Dataset (2025).csv", encoding="ISO-8859-1")

# 🔍 Fiyat kolonlarını bul
price_columns = [col for col in df.columns if "Launched Price" in col]

# 🧼 Temizleme fonksiyonu
def clean_price(value):
    cleaned = re.sub(r"[^\d.]", "", str(value))
    return float(cleaned) if cleaned else None

# Temizle
for col in price_columns:
    df[col] = df[col].apply(clean_price)

# 💱 Kur dönüşümü (USD)
df["Launched Price (Pakistan)"] = df["Launched Price (Pakistan)"] / 280
df["Launched Price (India)"] = df["Launched Price (India)"] / 83
df["Launched Price (China)"] = df["Launched Price (China)"] / 7.2
df["Launched Price (Dubai)"] = df["Launched Price (Dubai)"] / 3.67

# Döviz dönüşümünden sonra ekle 👇
df.loc[df["Model Name"] == "T21", "Launched Price (USA)"] = 217


# 🧮 Fiyat farklarını hesapla
df["Min Price"] = df[price_columns].min(axis=1)
df["Max Price"] = df[price_columns].max(axis=1)
df["Price Gap"] = df["Max Price"] - df["Min Price"]

# 🔁 Yuvarlama
df["Min Price"] = df["Min Price"].round(0)
df["Max Price"] = df["Max Price"].round(0)
df["Price Gap"] = df["Price Gap"].round(0)
for col in price_columns:
    df[col] = df[col].round(0)

# 📊 Marka bazlı fiyat farkı
brand_gap = df.groupby("Company Name")["Price Gap"].mean().sort_values(ascending=False)

# 📋 En çok fark olan 10 model
top_gap_models = df.sort_values(by="Price Gap", ascending=False).head(10)

# 💾 Excel'e kaydet
with pd.ExcelWriter("brandzone_report.xlsx") as writer:
    df.to_excel(writer, sheet_name="Full Data", index=False)
    brand_gap.to_frame(name="Avg Price Gap").to_excel(writer, sheet_name="Brand Avg Gap")
    top_gap_models.to_excel(writer, sheet_name="Top 10 Price Gaps", index=False)

print("✅ Excel kaydedildi: brandzone_report.xlsx")
