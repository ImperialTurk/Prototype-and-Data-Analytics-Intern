# Q6
import pandas as pd

# Load the imputed dataset 
file_path = "country_vaccination_stats_imputed.csv"
df = pd.read_csv(file_path)

# Calculate the median daily vaccinations per country
median_vaccinations = df.groupby("country")["daily_vaccinations"].median()

# Get the top-3 countries with the highest median daily vaccinations
top_3_countries = median_vaccinations.nlargest(3)

print("Top-3 countries with highest median daily vaccinations:")
for country, median_vax in top_3_countries.items():
    print(f"{country}: {median_vax:.0f}")
