#two data file 
import pandas as pd
import numpy as np
import json
movie=pd.read_csv('data/tmdb_5000_movies.csv')
mc=pd.read_csv('data/tmdb_5000_credits.csv')

#change json columns into python string
movie['genres']=movie['genres'].apply(json.loads)
movie['keywords']=movie['keywords'].apply(json.loads)
movie['production_companies']=movie['production_companies'].apply(json.loads)
movie['production_countries']=movie['production_countries'].apply(json.loads)
movie=movie.drop(['original_title','spoken_languages','status','revenue','vote_average','vote_count','budget'],axis=1)
mc['cast']=mc['cast'].apply(json.loads)
mc['crew']=mc['crew'].apply(json.loads)
mc=mc.drop(['title'], axis=1)


#extract director from the 'crew' column
def director(x):
    for i in x:
        if i['job'] == 'Director':
            return i['name']
mc['crew']=mc['crew'].apply(director)
mc.rename(columns={'crew':'director'},inplace=True)

#give a binary column for director
directorlist=[]
for i in range(len(mc['director'])):
        if mc['director'][i] not in directorlist:
            directorlist.append(mc['director'][i])
def checkdirector(y):
    indicator = []
    for director in directorlist:
        if director == y:
            indicator.append(1)
        else:
            indicator.append(0)
    return indicator
mc['checkdirector'] = mc['director'].apply(lambda y:(checkdirector(y)))

#give a binary column for genre
def getgenre(x):
    for i in range(len(x):
        genrelist.append(x[i]['name'])
    return genrelist
