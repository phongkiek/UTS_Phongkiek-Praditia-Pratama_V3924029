import seaborn as sns
import matplotlib.pyplot as plt

# Hitung probabilitas bersyarat untuk setiap kategori pendidikan
education_group = df.groupby('Education')['Loan_Status'].value_counts(normalize=True).unstack().fillna(0)

# Plot
plt.figure(figsize=(8, 5))
sns.barplot(x=education_group.index, y=education_group['Y'])
plt.title('Probabilitas Pengembalian Pinjaman Tepat Waktu Berdasarkan Pendidikan')
plt.xlabel('Jenjang Pendidikan')
plt.ylabel('Probabilitas Loan_Status = Y')
plt.ylim(0, 1)
plt.grid(True, axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
