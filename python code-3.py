# One-hot encode categorical variables
encoded_dataset = pd.get_dummies(dataset, columns=['Gender', 'Activity Level', 'Location'], drop_first=True)

# Display the first few rows of the encoded dataset
encoded_dataset.head()