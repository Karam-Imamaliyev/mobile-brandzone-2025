# 📱 Mobile BRANDZONE 2025 — Global Price & Performance Benchmark

## 🎯 Objective

The goal of this project is to analyze the global pricing of smartphones launched in 2025, along with their technical specifications, and determine the best value-for-money (VFM) devices using a custom metric called **KingScore**.

It focuses on device prices across five countries (Pakistan, India, China, USA, and Dubai), comparing brand offerings, price gaps, and real-world performance value.

---

## 🧰 Tools & Technologies

- Python (Pandas for data manipulation, Matplotlib for visualizations)
- Excel (for structured data export)
- PNG Charts (for presentations)

---

## 📊 What We Did

1. Cleaned all price fields and converted them into USD using exchange rates:
   - Pakistan: ÷ 280
   - India: ÷ 83
   - China: ÷ 7.2
   - Dubai: ÷ 3.67
   - USA: already in USD

2. Calculated **Price Gap** between cheapest and most expensive country per model.

3. Identified the **Cheapest Country** and **Most Expensive Country** for each device.

4. Introduced **KingScore** for performance valuation:


5. Generated two core rankings:
- Top 10 Devices with the Highest Price Gap
- Top 10 Devices with Best Value-for-Money (KingScore)

6. Exported all results to an Excel file with multiple sheets.

---

## 🏆 Highlights

- 🔺 Highest price gap observed in foldable and premium flagship phones.
- 🔻 Worst value-for-money found in high-priced tablets and luxury models.
- 🥇 Best value-for-money device: **Nokia T21** (corrected to $217 USD).

> Note: An error in the dataset listed Nokia T21 as $39,622. This was manually corrected.

---

## 📁 Deliverables

- 📄 `brandzone_report.xlsx` — Full dataset, analysis, and rankings
- 📈 `charts/top_10_price_gap_models.png` — Price Gap Visualization
- 📈 `charts/king_score_top10.png` — KingScore (VFM) Visualization

---

## 💡 Conclusion

Mobile BRANDZONE 2025 provides a data-driven, global perspective on smartphone pricing and value. It reveals how market conditions, brand positioning, and regional pricing strategies affect real-world consumer value.

This benchmark can help tech analysts, consumers, and marketers better understand **what device truly offers the most for its price** — globally.


## 🪨 Dataset Source

The Dataset was picked from Kaggle (Mobiles Dataset (2025)) and adapted for this project. 
 
---

🦅  
**Prepared by:**  
👑 Der King  for BARS KRAFT 
_"What others analyze, I conquer."_  
2025
