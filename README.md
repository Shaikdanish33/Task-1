## 🧹 Task 1: Cleaning and Preparing the Dataset

**📂 Dataset:** [Customer Personality Analysis – Kaggle](https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis)  
**🛠 Tools Used:** Python (Pandas), Excel

---

### 📌 Objective

Clean and prepare the raw dataset by handling nulls, removing duplicates, correcting inconsistent formats, and saving it in a usable format for further analysis.

---


##### 📂Raw file : Marketing_Campaign.csv
##### 📂Cleaned file : Cleaned_Marketing_Data.xlsx

---

<details>
<summary>🔽 Step 1: Load the Dataset</summary>

```python
import pandas as pd

# Load CSV with tab delimiter
df = pd.read_csv('marketing_campaign.csv', sep='\t')
```
📌 Why sep='\t'?
Although the file is named .csv, it’s actually tab-separated — not comma-separated as expected.
Opening it with the default sep=',' would result in a single-column dataframe where all data is lumped into one field.
To fix this, i use sep='\t' to correctly parse it into proper columns.
</details>

<details> <summary>🔽 Step 2: Handle Missing Values</summary>
  
```python
# Check for nulls
print(df.isnull().sum())
```
  
## Found 24 null values in 'Income'
```python
df['Income'] = df['Income'].fillna(df['Income'].mean())
```python

✔️ Used mean imputation for missing values in Income
❌ Avoided deleting rows or filling with 'NA' to preserve data quality
```

</details>

<details> <summary>🔽 Step 3: Remove Duplicates</summary>

```python
print("Duplicates before:", df.duplicated().sum())

# Drop duplicate records
df = df.drop_duplicates()

print("Duplicates after:", df.duplicated().sum())
```
✔️ Ensured all records are unique
</details>

<details> <summary>🔽 Step 4: Fix Inconsistent Categorical Values</summary>
  
```python
print("Education:", df['Education'].unique())
print("Marital Status:", df['Marital_Status'].unique())

# Grouping irrelevant marital status categories
df['Marital_Status'] = df['Marital_Status'].replace(
    ['Alone', 'Absurd', 'YOLO'], 'Other'
)
```
✔️ Grouped "Alone", "Absurd", "YOLO" into a single category: Other

</details>

<details> <summary>🔽 Step 5: Convert Dates</summary>

```python
# Convert to datetime format
df['dt_customer'] = pd.to_datetime(df['Dt_Customer'], format='%d-%m-%Y', errors='coerce')
df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'], errors='coerce')

print(df.dtypes['Dt_Customer'])
```
✔️ Converted Dt_Customer to proper datetime format for time-based analysis

</details>

<details> <summary>🔽 Step 6: Clean Column Names</summary>
  
```python
# Normalize column headers
df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")
```
✔️ Standardized all column names: lowercase, no spaces, underscores for consistency
</details>

<details> <summary>🔽 Step 7: Save Cleaned Dataset</summary>
  
```python
# Save cleaned dataset
df.to_excel("Cleaned_Marketing_Data.xlsx", index=False)
```
📁 Output File: Cleaned_Marketing_Data.xlsx
</details>

---
## ✅ Summary
 Loaded dataset and examined structure

 Handled nulls with mean imputation

 Removed duplicate records

 Fixed inconsistent categorical values

 Converted date columns to datetime format

 Cleaned and standardized column names

 Exported cleaned dataset to Excel

 ---
[Interview Questions Based on This Task](interview_questions.md)









