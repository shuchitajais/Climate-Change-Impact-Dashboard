import os
print("Current working directory:", os.getcwd())
import os
import pandas as pd

print("Current working directory:", os.getcwd())

temp = pd.read_csv('annual-temperature-anomalies.csv')
forest = pd.read_csv('annual-change-forest-area.csv')
co2 = pd.read_csv('owid-co2-data.csv')

print(temp.head())
print(forest.head())
print(co2.head())

import pandas as pd

# Load CSV files
temp = pd.read_csv('annual-temperature-anomalies.csv')
forest = pd.read_csv('annual-change-forest-area.csv')
co2 = pd.read_csv('owid-co2-data.csv')

# Step 1: Filter for 10 countries and years
country_list = [
    'China', 'United States', 'India', 'Russia', 'Germany',
    'Brazil', 'Indonesia', 'Democratic Republic of Congo',
    'Canada', 'Australia'
]
years = list(range(1990, 2024))

# Filter each DataFrame
temp_filtered = temp[temp['Entity'].isin(country_list) & temp['Year'].isin(years)]
forest_filtered = forest[forest['Entity'].isin(country_list) & forest['Year'].isin(years)]
co2_filtered = co2[co2['country'].isin(country_list) & co2['year'].isin(years)]

# Preview filtered data
print(temp_filtered.head())
print(forest_filtered.head())
print(co2_filtered.head())

# Step 2: Fix country names if needed
# Step 2: Fix country names if needed
co2_filtered.loc[:, 'country'] = co2_filtered['country'].replace({
    'Democratic Republic of the Congo': 'Democratic Republic of Congo'
})

# Step 3: Merge datasets
df_merged = temp_filtered.merge(
    forest_filtered, on=['Entity', 'Year'], suffixes=('_temp', '_forest')
)

df_merged = df_merged.merge(
    co2_filtered, left_on=['Entity', 'Year'], right_on=['country', 'year']
)

# Step 4: Fill missing data
df_merged = df_merged.fillna(0)

# Preview merged data
print(df_merged.head())

df_merged.to_csv('climate_dashboard_clean.csv', index=False)
print("Cleaned data saved to climate_dashboard_clean.csv")
