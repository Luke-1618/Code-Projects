import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

# List of data in the following format for each data point
# data=['IP Address', 'Latitude', 'Longitude'), ('IP Address', 'Latitude', 'Longitude')...]

data = [...]

# Convert to DataFrame
df = pd.DataFrame(data, columns=['IP Address', 'Latitude', 'Longitude'])

# Initialize Nominatim API
geolocator = Nominatim(user_agent="geoapiExercises")

# Apply rate limiter to avoid being blocked by the service
geocode = RateLimiter(geolocator.reverse, min_delay_seconds=1)

# Function to get location details
def reverse_geocode(lat, lon):
    try:
        location = geocode((lat, lon), exactly_one=True)
        address = location.raw['address']
        city = address.get('city', address.get('town', address.get('village', '')))
        country = address.get('country', '')
        return city, country
    except:
        return "Unknown", "Unknown"

# Apply reverse geocoding
df['City'], df['Country'] = zip(*df.apply(lambda row: reverse_geocode(row['Latitude'], row['Longitude']), axis=1))

# Display the DataFrame with city and country
print(df)

# Save the DataFrame to a CSV file if needed
df.to_csv('geocoded_locations.csv', index=False)
