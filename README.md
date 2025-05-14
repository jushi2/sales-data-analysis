
# 📊 Sales Data Analysis Project

This project involves cleaning, analyzing, and summarizing a dummy sales dataset using **Pandas** and **NumPy**. It's designed as a beginner-to-intermediate level portfolio project that covers data preprocessing, aggregation, filtering, and exporting analysis results.

---

## 📁 Dataset Overview

The dataset contains the following columns:

- **Product**: Name of the product sold
- **Category**: Category under which the product falls (e.g., Electronics, Grocery)
- **Region**: Sales region (e.g., North, South, East)
- **Price**: Unit price of the product
- **Quantity**: Number of units sold

---

## 🧠 Project Steps

1. **Data Cleaning**
   - Drop rows with missing `Product` or `Category`
   - Fill missing `Price` with average price
   - Fill missing `Quantity` with 0

2. **Data Conversion**
   - Convert cleaned Pandas DataFrame to a NumPy array for additional practice

3. **Sales Analysis**
   - Total Revenue = Price × Quantity
   - Revenue per Product
   - Revenue per Category
   - Products with above-average price
   - Top 3 performing products by quantity
   - Region-wise revenue analysis (Best/Worst region)

4. **Export**
   - Save product-wise revenue analysis to `product_revenue.csv`

---

## 🛠 Technologies Used

- Python 🐍
- Pandas 🐼
- NumPy 🔢
- Jupyter Notebook 📓

---

## 📸 Sample Output

```bash
Top 3 performing products:
Product A    250
Product B    150
Product C    100
```

---

## 🚀 Getting Started

1. Clone the repo:
```bash
git clone https://github.com/jushi2/sales-data-analysis.git
cd sales-data-analysis
```

2. Install dependencies:
```bash
pip install pandas numpy
```

3. Open the project in Jupyter Notebook:
```bash
jupyter notebook
```

---

## 👨‍💻 Author

**Pijush Mazumder**  
🔗 [GitHub](https://github.com/jushi2) | [LinkedIn](https://www.linkedin.com/in/pijush-mazumder)

---

## 📝 License

This project is open-source and free to use under the MIT License.
