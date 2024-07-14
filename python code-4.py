import matplotlib.pyplot as plt
import seaborn as sns

# Set the style for the plots
sns.set(style="whitegrid")

# Distribution of Age and App Sessions
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
sns.histplot(encoded_dataset['Age'], kde=True, bins=20, color='skyblue')
plt.title('Distribution of Age')

plt.subplot(1, 2, 2)
sns.histplot(encoded_dataset['App Sessions'], kde=True, bins=20, color='salmon')
plt.title('Distribution of App Sessions')

plt.tight_layout()
plt.show()

# Correlation Heatmap
plt.figure(figsize=(12, 8))
correlation_matrix = encoded_dataset.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()

# Box Plot for Calories Burned by Gender
plt.figure(figsize=(8, 6))
sns.boxplot(x='Gender_Male', y='Calories Burned', data=encoded_dataset, palette='viridis')
plt.title('Calories Burned by Gender')
plt.xticks([0, 1], ['Female', 'Male'])
plt.show()

# Activity Level vs. App Sessions
plt.figure(figsize=(8, 6))
sns.boxplot(x='Activity Level_Moderate', y='App Sessions', data=encoded_dataset, palette='viridis')
plt.title('App Sessions by Activity Level')
plt.xticks([0, 1], ['Active/Sedentary', 'Moderate'])
plt.show()