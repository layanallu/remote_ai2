import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



# READ DATA FROM CSV FILE 
df = pd.read_csv("FlavorSense.csv")

#CHECK DATA ACCESS
print(df.head())



print(df.columns)



#  رسم توزيع العمر (age)
plt.figure(figsize=(8,4))
sns.histplot(df['age'].dropna(), bins=20, kde=True, color='teal')
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()




# توزيع المناطق المناخية (climate_zone)
plt.figure(figsize=(8,4))
sns.countplot(data=df, x='climate_zone', palette='coolwarm')
plt.title('Climate Zone Distribution')
plt.xlabel('Climate Zone')
plt.ylabel('Count')
plt.show()






# تفضيلات الطعم (preferred_taste)
plt.figure(figsize=(8,4))
sns.countplot(data=df, x='preferred_taste', palette='Set2')
plt.title('Preferred Taste')
plt.xlabel('Taste')
plt.ylabel('Count')
plt.show()



