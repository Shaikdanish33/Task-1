# 🧠 Interview Questions Related to Data Cleaning Task
---

### 1. What are missing values and how do you handle them?

**Missing values** occur when no data is stored for a variable in an observation. Common ways to handle them:
- Remove rows using `dropna()`
- Replace with mean/median/mode using `fillna()`
- Predict missing values using modeling techniques
- Leave them or insert NA as-is if they're meaningful (e.g., optional field)

---

### 2. How do you treat duplicate records?

Duplicates can skew analysis. To handle:
- Use `df.duplicated().sum()` to check for duplicates
- Use `df.drop_duplicates()` to remove them

---

### 3. Difference between `dropna()` and `fillna()` in Pandas?

- `dropna()` removes rows (or columns) with missing values.
- `fillna()` replaces missing values with a specific value like mean, median, or a constant.

---

### 4. What is outlier treatment and why is it important?

**Outliers** are data points that differ significantly from others. They're important because they can:
- Distort mean and variance
- Mislead model training
Treatment methods:
- Remove them
- Cap/floor them
- Use log or robust scaling

---

### 5. Explain the process of standardizing data.
Standardizing data means transforming values into a consistent format so they can be compared or processed more accurately. This is especially useful for text and numerical data.

For text values:
Convert to lowercase, remove extra spaces, unify formats.
Example:

' Male', 'MALE', 'male' → standardized to 'male'.

For numerical values:
Scale features to a common range (e.g., mean=0, std=1) using tools like:

```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df['age_scaled'] = scaler.fit_transform(df[['Age']])
```
Benefits:
- Ensures uniformity
- Improves model performance
- Reduces data ambiguity

### 6. How do you handle inconsistent data formats (e.g., date/time)?
Inconsistent date/time formats can break analysis and cause errors. Here's how to fix them:

Use Pandas to convert to a uniform datetime format:

```pyton
df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'], format='%d-%m-%Y', errors='coerce')
```
Handle errors:
- Set errors='coerce' to convert invalid dates to NaT (can be handled later).

Benefits:
- Enables sorting and time-based analysis
- Avoids parsing errors in future operations

---

### 7. What are common data cleaning challenges?
Here are some challenges faced during data cleaning:

- Missing values : Empty or null fields in the dataset
- Inconsistent formats :	Different formats for date, text, numbers
- Duplicate records :	Repeated rows that skew analysis
- Wrong data types:	Age as string, date as object
- Categorical inconsistency :	male, Male, MALE — all mean the same
- Outliers : Extremely high or low values
- Typos & extra spaces :	Affect grouping and filtering operations
- Mixed data granularity: E.g., combining monthly and daily sales in one

--- 

### 8. How can you check data quality?
To check data quality, you can perform the following steps:

Check	Tools/Methods
- Missing values	: df.isnull().sum() or Excel filters
- Duplicates	: df.duplicated().sum()
- Consistent categories :	df['column'].unique()
- Data types	: df.dtypes to ensure correct types
- Outliers: 	Use .describe() or boxplots
- Date parsing	: Use pd.to_datetime()
- Text cleanup: 	.str.strip().str.lower()
- General overview	: .info(), .describe()
