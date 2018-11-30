#two data file 
import pandas as pd
import numpy as np
import json
movie=pd.read_csv('data/tmdb_5000_movies.csv')
mc=pd.read_csv('data/tmdb_5000_credits.csv')

#change json columns into python string
movie['genres']=movie['genres'].apply(json.loads)
movie['keywords']=movie['keywords'].apply(json.loads)
mc['cast']=mc['cast'].apply(json.loads)
mc['crew']=mc['crew'].apply(json.loads)

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

