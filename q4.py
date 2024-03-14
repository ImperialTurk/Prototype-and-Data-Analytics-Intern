# Q4
import pandas as pd

# Load the dataset from the CSV file
file_path = "C:\Users\brain\Downloads\country_vaccination_stats.csv"
df = pd.read_csv(file_path)

# Group by country and calculate the minimum daily vaccination number
min_vaccinations = df.groupby("country")["daily_vaccinations"].min()

# Fill missing values with the minimum daily vaccination number or 0
df["daily_vaccinations"] = df["daily_vaccinations"].fillna(min_vaccinations)

# Save the updated dataset to a new CSV file
output_file_path = "C:\Users\brain\Downloads\country_vaccination_stats_imputed.csv"
df.to_csv(output_file_path, index=False)

print(f"Imputed data saved to {output_file_path}")
