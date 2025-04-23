import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Asumsikan kita sudah memiliki dataset yang dimuat sebagai df
# Karena dataset aktual tidak tersedia, saya akan membuat contoh dataset

# Membuat contoh dataset
np.random.seed(42)
data = {
    'Marital_Status': np.random.choice(['Married', 'Single', 'Divorced'], size=1000),
    'Dependents': np.random.randint(0, 5, size=1000),
    'Has_Rumah': np.random.choice(['Urban', 'Rural', 'Suburban'], size=1000),
    'Income': np.random.normal(5000000, 2000000, size=1000).astype(int),
    'Education': np.random.choice(['SD', 'SMP', 'SMA', 'D3', 'S1', 'S2'], size=1000),
    'On_Time_Repayment': np.random.choice(['Yes', 'No'], size=1000, p=[0.7, 0.3])
}

df = pd.DataFrame(data)

# a. Probabilitas nasabah yang sudah menikah dan memiliki tanggungan > 1
married_dependents = df[(df['Marital_Status'] == 'Married') & (df['Dependents'] > 1)]
prob_a = len(married_dependents) / len(df)
print(f"a. Probabilitas nasabah menikah dengan tanggungan > 1: {prob_a:.2%}")

# Visualisasi untuk poin a
plt.figure(figsize=(10, 6))
married_dep_counts = df[(df['Marital_Status'] == 'Married')].groupby('Dependents')['On_Time_Repayment'].value_counts(normalize=True).unstack()
married_dep_counts.plot(kind='bar', stacked=True, color=['#ff9999','#66b3ff'])
plt.title('Probabilitas Pembayaran Tepat Waktu berdasarkan Jumlah Tanggungan (Nasabah Menikah)')
plt.xlabel('Jumlah Tanggungan')
plt.ylabel('Probabilitas')
plt.legend(title='Tepat Waktu', loc='upper right')
plt.xticks(rotation=0)
plt.show()

# b. Probabilitas nasabah memiliki rumah di perkotaan dan penghasilan di atas rata-rata
avg_income = df['Income'].mean()
urban_high_income = df[(df['Has_Rumah'] == 'Urban') & (df['Income'] > avg_income)]
prob_b = len(urban_high_income) / len(df)
print(f"\nb. Probabilitas nasabah urban dengan penghasilan di atas rata-rata: {prob_b:.2%}")

# Visualisasi untuk poin b
plt.figure(figsize=(10, 6))
urban_income = df[df['Has_Rumah'] == 'Urban']
urban_income['Income_Level'] = pd.cut(urban_income['Income'], 
                                     bins=[0, avg_income, urban_income['Income'].max()],
                                     labels=['Below Average', 'Above Average'])
income_repayment = urban_income.groupby('Income_Level')['On_Time_Repayment'].value_counts(normalize=True).unstack()
income_repayment.plot(kind='bar', stacked=True, color=['#ff9999','#66b3ff'])
plt.title('Probabilitas Pembayaran Tepat Waktu untuk Nasabah Urban berdasarkan Tingkat Penghasilan')
plt.xlabel('Tingkat Penghasilan')
plt.ylabel('Probabilitas')
plt.legend(title='Tepat Waktu', loc='upper right')
plt.xticks(rotation=0)
plt.show()

# c. Distribusi probabilitas bersyarat berdasarkan jenjang pendidikan
plt.figure(figsize=(12, 6))
education_repayment = df.groupby('Education')['On_Time_Repayment'].value_counts(normalize=True).unstack()
education_repayment = education_repayment.sort_values('Yes', ascending=False)
education_repayment.plot(kind='bar', stacked=True, color=['#ff9999','#66b3ff'])
plt.title('Distribusi Probabilitas Pembayaran Tepat Waktu berdasarkan Pendidikan')
plt.xlabel('Jenjang Pendidikan')
plt.ylabel('Probabilitas')
plt.legend(title='Tepat Waktu', loc='upper right')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()