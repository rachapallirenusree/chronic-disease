import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv(r"D:\DATA SCIENCE TOOLBOX USING PYTHON PROGRAMMING\U.S._Chronic_Disease_Indicators.csv")
df=pd.read_csv(r"https://drive.google.com/file/d/1l7otigHM33Ev4ToWCMMMVe_HlVZrVjTA/view?usp=drive_link")
print("the first five columns of th eunicorn dataset \n")
print(df.head())
print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print(df.info())
print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print(df.describe)
print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print(df['StratificationCategoryID1'].unique())
print(df['StratificationCategoryID1'].nunique())
print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("Missing Values:\n",df.isnull().sum())
print("Total Missing Values:\n",df.isnull().sum().sum())
print("------------------------------------ After Handling missimg values-----------------------------------------------------------------------------------------------------------------------------")
df['DataValue']=df['DataValue'].fillna(df['DataValue'].mean())
df['Response']=df['Response'].fillna("NA")
df['DataValueAlt']=df['DataValueAlt'].fillna(df['DataValueAlt'].mean())
df['DataValueFootnoteSymbol']=df['DataValueFootnoteSymbol'].fillna(df['DataValueFootnoteSymbol'].mode()[0])
df['DataValueFootnote']=df['DataValueFootnote'].fillna(df['DataValueFootnote'].mode()[0])
df['LowConfidenceLimit']=df['LowConfidenceLimit'].fillna(df['LowConfidenceLimit'].mean())
df['HighConfidenceLimit']=df['HighConfidenceLimit'].fillna(df['HighConfidenceLimit'].mean())
df['StratificationCategory2']=df['StratificationCategory2'].fillna("NA")
df['Stratification2']=df['Stratification2'].fillna("NA")
df['StratificationCategory3']=df['StratificationCategory3'].fillna("NA")
df['Stratification3']=df['Stratification3'].fillna("NA")
@@ -131,24 +131,25 @@

data_skew = filtered_df["DataValue"].skew()
print(f"Skewness of Diabetes DataValue: {data_skew:.2f}")

plt.figure(figsize=(8, 5))
sns.histplot(filtered_df["DataValue"], kde=True, bins=20)
plt.title(f"Distribution of Diabetes DataValue\n(Skewness = {data_skew:.2f})")
plt.xlabel("Data Value (%)")
plt.ylabel("Frequency")
plt.show()

##print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

filtered_df = df[df["DataValue"].notna()]

numeric_df = filtered_df[["DataValue", "LowConfidenceLimit", "HighConfidenceLimit"]]

corr = numeric_df.corr()

plt.figure(figsize=(6, 4))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap of Chronic Disease Metrics")
plt.show()