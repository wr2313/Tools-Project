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

def getactor(data):
    actorlist=[]
    for i in range(len(data)):
        actorlist.append(data[i]['name'])
    return actorlist
mc['cast']=mc['cast'].apply(lambda x:getactor(x))
mc.rename(columns={'cast':'actor'},inplace=True)

#Return #ActorList
ActorList=[]
for i in range(len(mc)):
    for j in range(len(mc['actor'].iloc[i])):
        if mc['actor'].iloc[i][j] not in ActorList:
            ActorList.append(mc.iloc[i]['actor'][j])


#clean movie data frame
def extractGenre(data):
    genrelist=[]
    for i in range(len(data)):
        genrelist.append(data[i]['name'])
    return genrelist

def getcountry(x):
    country=[]
    for i in range(len(x)):
        country.append(x[i]['name'])
    return country

def getcompany(x):
    company=[]
    for i in range(len(x)):
        company.append(x[i]['name'])
    return company


def getkeywords(x):
    keywordslist=[]
    for i in range(len(x)):
        keywordslist.append(x[i]['name'])
    return keywordslist

movie['genres']=movie['genres'].apply(lambda x:extractGenre(x))
movie['production_countries']=movie['production_countries'].apply(lambda x:getcountry(x))
movie['production_companies']=movie['production_companies'].apply(lambda x:getcompany(x))
