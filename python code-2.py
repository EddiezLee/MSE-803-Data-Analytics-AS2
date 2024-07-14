# Check for missing values
missing_values = dataset.isnull().sum()

# Get basic statistics
basic_stats = dataset.describe(include='all')

missing_values, basic_stats