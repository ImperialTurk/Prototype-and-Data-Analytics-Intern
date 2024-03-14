# Q8
WITH ImputedData AS (
    SELECT
        country,
        date,
        COALESCE(daily_vaccinations, 0) AS daily_vaccinations,
        vaccines
    FROM country_vaccination_stats
)
SELECT
    country,
    date,
    CASE
        WHEN daily_vaccinations = 0 THEN
            (SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY daily_vaccinations)
             FROM ImputedData AS i2
             WHERE i2.country = ImputedData.country)
        ELSE daily_vaccinations
    END AS imputed_daily_vaccinations,
    vaccines
FROM ImputedData;
