import pandas as pd

# Here I am loading the dataset using tab as delimiter
df = pd.read_csv('marketing_campaign.csv', sep='\t')

# Filling null values with mean (average)
df['Income'] = df['Income'].fillna(df['Income'].mean())

# To check which column has missing values and how many
print(df.isnull().sum())

# To check for duplicates and remove if available
print("Duplicates before :", df.duplicated().sum())
df = df.drop_duplicates()
print("Duplicates after :", df.duplicated().sum())

# Checking for inconsistent values in categorical columns
print("Education:", df['Education'].unique())
print("Marital Status:", df['Marital_Status'].unique())

# Converting to proper datetime format
df['dt_customer'] = pd.to_datetime(df['Dt_Customer'], format='%d-%m-%Y', errors='coerce')
df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'], errors='coerce')
print(df.dtypes['Dt_Customer'])

# Grouping ['Alone', 'Absurd', 'YOLO'] as 'Other'
df['Marital_Status'] = df['Marital_Status'].replace(
    ['Alone', 'Absurd', 'YOLO'], 'Other'
)

# Clean Column Names
df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")

# Checking all the data types
print(df.dtypes)

# Saving the file 
df.to_excel("Cleaned_Marketing_Data.xlsx", index=False,)
