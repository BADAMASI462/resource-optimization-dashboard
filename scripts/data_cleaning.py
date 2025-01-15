import pandas as pd

# Load datasets
resource_data = pd.read_csv('data/resource_utilization.csv')
performance_data = pd.read_csv('data/performance_metrics.csv')
budget_data = pd.read_csv('data/budget_reports.csv')

# Data cleaning
resource_data['Utilization (%)'] = resource_data['Used'] / resource_data['Allocated'] * 100
budget_data['Variance (%)'] = (budget_data['Budget_Allocated'] - budget_data['Budget_Used']) / budget_data['Budget_Allocated'] * 100

# Merge datasets for analysis
merged_data = resource_data.merge(performance_data, on='Department').merge(budget_data, on='Department')

# Save cleaned data
merged_data.to_csv('data/cleaned_data.csv', index=False)
print("Data cleaned and saved to 'data/cleaned_data.csv'")
