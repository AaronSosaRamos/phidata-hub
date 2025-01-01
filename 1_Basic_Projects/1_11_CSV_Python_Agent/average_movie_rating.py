import pandas as pd

# Load the data
url = 'https://phidata-public.s3.amazonaws.com/demo_data/IMDB-Movie-Data.csv'
df = pd.read_csv(url)

# Calculate average rating
average_rating = df['Rating'].mean()

# Return average rating
average_rating