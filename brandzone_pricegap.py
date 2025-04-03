import pandas as pd
import numpy as np
import re

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

# 💱 5. Döviz kurlarıyla USD'ye çevir
df["Launched Price (Pakistan)"] = df["Launched Price (Pakistan)"] / 280
df["Launched Price (India)"] = df["Launched Price (India)"] / 83
df["Launched Price (China)"] = df["Launched Price (China)"] / 7.2
df["Launched Price (Dubai)"] = df["Launched Price (Dubai)"] / 3.67
# USA zaten USD

# 🧮 6. Min, Max ve Fiyat Farkı (Price Gap) hesapla
df["Min Price"] = df[price_columns].min(axis=1)
df["Max Price"] = df[price_columns].max(axis=1)
df["Price Gap"] = df["Max Price"] - df["Min Price"]

# 🔁 7. Sayıları yuvarla (görüntü temizliği)
df["Min Price"] = df["Min Price"].round(0)
df["Max Price"] = df["Max Price"].round(0)
df["Price Gap"] = df["Price Gap"].round(0)
for col in price_columns:
    df[col] = df[col].round(0)

# 🌍 8. En ucuz ve en pahalı ülke
def find_country(price_row, extreme='min'):
    if extreme == 'min':
        col_name = price_row[price_columns].idxmin()
    else:
        col_name = price_row[price_columns].idxmax()
    return col_name.split('(')[-1].split(')')[0]

df["Cheapest Country"] = df.apply(lambda row: find_country(row, 'min'), axis=1)
df["Most Expensive Country"] = df.apply(lambda row: find_country(row, 'max'), axis=1)

# ✅ 9. Kontrol için ilk 5 satırı göster
print(df[["Model Name", "Min Price", "Max Price", "Price Gap", "Cheapest Country", "Most Expensive Country"]].head())
