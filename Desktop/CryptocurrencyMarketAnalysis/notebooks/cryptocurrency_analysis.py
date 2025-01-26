# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the datasets
df1 = pd.read_csv('datasets/coinmarketcap_06012018.csv')
df2 = pd.read_csv('datasets/coinmarketcap_06122017.csv')

# Display the first few rows of each dataframe to understand the structure
print("Dataset from June 1, 2018:")
print(df1.head())
print("\nDataset from December 6, 2017:")
print(df2.head())

# Data Preprocessing (Example: Convert the date column to datetime if available)
# If there are any specific preprocessing steps needed, apply them here
# Example: if there's a date column, convert it
# df1['Date'] = pd.to_datetime(df1['Date'])
# df2['Date'] = pd.to_datetime(df2['Date'])

# Basic summary of the datasets
print("\nSummary of June 1, 2018 dataset:")
print(df1.describe())
print("\nSummary of December 6, 2017 dataset:")
print(df2.describe())

# Merging the two datasets based on a common column, e.g., 'Coin'
# If both datasets have the 'Coin' column and it's used for classification, we can merge them
merged_df = pd.merge(df1, df2, on="Coin", suffixes=('_June', '_Dec'))

# Now, we will perform a simple classification or comparison based on 'Market Cap'
# Example: Visualize the market cap of the coins
plt.figure(figsize=(10, 6))

# Plot market capitalization for June 1, 2018
plt.plot(df1['Market Cap'], label='June 1, 2018', color='blue')

# Plot market capitalization for December 6, 2017
plt.plot(df2['Market Cap'], label='December 6, 2017', color='orange')

# Add titles and labels
plt.title('Cryptocurrency Market Capitalization Comparison')
plt.xlabel('Coins')
plt.ylabel('Market Capitalization')
plt.legend()

# Show the plot
plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
plt.tight_layout()
plt.show()

# Save the figure to an image file if needed
plt.savefig('market_cap_comparison.png')

# You can also export the merged dataset to a CSV if further analysis is required
merged_df.to_csv('merged_market_data.csv', index=False)

# Example analysis: Find the coins that increased in market cap between the two dates
merged_df['Market Cap Change'] = merged_df['Market Cap_Dec'] - merged_df['Market Cap_June']
increased_coins = merged_df[merged_df['Market Cap Change'] > 0]

print("\nCoins with increased market cap between June 1, 2018 and December 6, 2017:")
print(increased_coins[['Coin', 'Market Cap_June', 'Market Cap_Dec', 'Market Cap Change']])

# Example: Save the increased coins data to a CSV
increased_coins.to_csv('increased_market_cap_coins.csv', index=False)

# Add any other analysis as required
