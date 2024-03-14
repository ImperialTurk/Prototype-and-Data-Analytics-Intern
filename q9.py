import pandas as pd
import re

# Sample data
data = {
    'Device_Type': ['AXO145', 'TRU151', 'ZOD231', 'YRT326', 'LWR245'],
    'Stats_Access_Link': [
        '<url>[12](https://xcd32112.smart_meter.com)</url>',
        '<url>[13](http://txh67.dia_meter.com)</url>',
        '<url>[14](http://yf5495.smart_meter.com)</url>',
        '<url>[15](https://ret323.tru.crown.com)</url>',
        '<url>[16](https://lwr3243.celcius.com)</url>'
    ]
}

df = pd.DataFrame(data)

def extract_url(link):
    match = re.search(r'<url>\[\d+\]\((?:https?://)?(?P<domain>[a-zA-Z0-9._-]+)\)</url>', link)
    if match:
        url = match.group('domain')
    else:
        url = '' 
    return url

df['Pure_URL'] = df['Stats_Access_Link'].apply(extract_url)
print(df[['Device_Type', 'Pure_URL']])
