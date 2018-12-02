#read two data files (basic info about each movie: cast, genre, director, etc)
import pandas as pd
import numpy as np
import json
movie=pd.read_csv('data/tmdb_5000_movies.csv')
mc=pd.read_csv('data/tmdb_5000_credits.csv')


#change json columns into python string and drop unesccary columns
movie['genres']=movie['genres'].apply(json.loads)
movie['keywords']=movie['keywords'].apply(json.loads)
movie['production_companies']=movie['production_companies'].apply(json.loads)
movie['production_countries']=movie['production_countries'].apply(json.loads)
movie=movie.drop(['original_title','spoken_languages','status','revenue','vote_average','vote_count','budget'],axis=1)
mc['cast']=mc['cast'].apply(json.loads)
mc['crew']=mc['crew'].apply(json.loads)
mc=mc.drop(['title'], axis=1)


#exract the data we need from the strings
#extract director from the 'crew' column
def director(x):
    for i in x:
        if i['job'] == 'Director':
            return i['name']
mc['crew']=mc['crew'].apply(director)
mc.rename(columns={'crew':'director'},inplace=True)

def getcast(x):
    castlist=[]
    for i in range(len(x)):
        castlist.append(x[i]['name'])
    return castlist
mc['cast']=mc['cast'].apply(lambda x:getcast(x))

def getgenre(x):
    genrelist=[]
    for i in range(len(x)):
        genrelist.append(x[i]['name'])
    return genrelist
movie['genres']=movie['genres'].apply(lambda x:getgenre(x))

def getcountry(x):
    country=[]
    for i in range(len(x)):
        country.append(x[i]['name'])
    return country
movie['production_countries']=movie['production_countries'].apply(lambda x:getcountry(x))

def getcompany(x):
    company=[]
    for i in range(len(x)):
        company.append(x[i]['name'])
    return company
movie['production_companies']=movie['production_companies'].apply(lambda x:getcompany(x))

def getkeywords(x):
    keywordslist=[]
    for i in range(len(x)):
        keywordslist.append(x[i]['name'])
    return keywordslist
movie['keywords']=movie['keywords'].apply(lambda x:getkeywords(x))


#merge two datasets
movie.rename(columns={'id':'movie_id'},inplace=True)
dataset=pd.merge(movie,mc,on='movie_id')
dataset = dataset[['title', 'movie_id', 'director', 'cast', 'genres','overview','keywords','tagline','homepage','original_language','production_companies','production_countries','release_date','runtime','popularity']]
dataset = dataset[pd.notnull(dataset['overview'])]

dataset = dataset[['title', 'movie_id', 'director', 'cast', 'genres','overview','keywords','tagline','homepage','original_language','production_companies','production_countries','release_date','runtime','popularity']]
dataset
dataset['overview'].head()
dataset['overview'].isna().sum()
dataset = dataset[pd.notnull(dataset['overview'])]
dataset['overview']
