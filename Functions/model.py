dataset = dataset[['title', 'movie_id', 'director', 'cast', 'genres','overview','keywords','tagline','homepage','original_language','production_companies','production_countries','release_date','runtime','popularity']]
dataset
dataset['overview'].head()
dataset['overview'].isna().sum()
dataset = dataset[pd.notnull(dataset['overview'])]
dataset['overview']