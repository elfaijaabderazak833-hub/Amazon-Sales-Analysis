import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv('Amazon_Big_Sales_Dataset_2026.csv')
print(df.head(5))
# print(df.shape)
# print(df.describe())
# print(df.columns)
# print(df.nunique())
print(df.dtypes)
print(df.isnull().sum())
df['Revenues']=df['Price_USD']*df['Review_Count']
print(df['Category'].value_counts())
print(df)
pd.options.display.float_format='{:, .2f}'.format
top_cat=df.groupby('Category')['Revenues'].sum().sort_values(ascending=False).head(5)
top_cat.plot(kind='bar', color='skyblue', alpha=0.9)
plt.title('Top 5 Category by Revenues')
plt.ylabel('Revenue')
plt.tight_layout()
plt.show()
plt.savefig('top_5_categories.png', dpi=300)

    # Export insights to text file
with open('Report.txt', 'w', encoding='utf-8') as f:
    f.write("Amazon Sales Analysis Report\n")
    f.write("============================\n\n")
    f.write(f"Total Products: {len(df)}\n")
    f.write(f"Total Categories: {df['Category'].nunique()}\n")
    f.write(f"Total Revenue: {df['Revenues'].sum():,.2f} USD\n")
    f.write("Top 5 Categories by Revenue:\n")
    f.write(top_cat.to_string())
    print("\n=== Key Insights ===")
print(f"1. Highest revenue category: {top_cat.index[0]}")
print(f"2. Total revenue: {df['Revenues'].sum():,.2f} USD")
print(f"3. Average product price: {df['Price_USD'].mean():.2f} USD")