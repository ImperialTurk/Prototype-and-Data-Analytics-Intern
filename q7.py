# Q7
import pandas as pd

# Load the imputed dataset
file_path = "country_vaccination_stats_imputed.csv"
df = pd.read_csv(file_path)

# Filter data
date_to_find = "01/06/2021"
filtered_df = df[df["date"] == date_to_find]

# Calculate the total vaccinations for that date
total_vaccinations = filtered_df["daily_vaccinations"].sum()

print(f"Total vaccinations on {date_to_find}: {total_vaccinations}")
