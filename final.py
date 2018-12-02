#read two data files (basic info about each movie: cast, genre, director, etc)
import pandas as pd
import numpy as np
import json
movie=pd.read_csv('tmdb_5000_movies.csv')
mc=pd.read_csv('tmdb_5000_credits.csv')

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
def director(x):
    for i in x:
        if i['job'] == 'Director':
            return i['name']
mc['crew']=mc['crew'].apply(director)
mc.rename(columns={'crew':'director'},inplace=True)

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

def getgenre(x):
    genrelist=[]
    for i in range(len(x)):
        genrelist.append(x[i]['name'])
    return genrelist
movie['genres']=movie['genres'].apply(lambda x:getgenre(x))

def getcast(x):
    castlist=[]
    for i in range(len(x)):
        castlist.append(x[i]['name'])
    return castlist
mc['cast']=mc['cast'].apply(lambda x:getcast(x))

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

#build 2 functions using similarity 
#content based recommendation system: overview
#featured based recommendation system: cast, genre, keywords, director
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(dataset['overview'])

tfidf_matrix.shape

from sklearn.metrics.pairwise import linear_kernel

cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

dataset[dataset.duplicated(['overview'], keep=False)]

def find_index(name):
    count = 0
    for i in dataset['title']:
        if i == name:
            return count
        count+=1

def return_sorted(l):
    return sorted(l, key=lambda x: x[1], reverse=True)[1:11]

def find_movie_names(l):
    movie_index = []
    movies = []
    
    for i in l:
        movie_index.append(i[0])
        
    for i in movie_index:
        movies.append(dataset['title'].iloc[i])
        
    return movies

def get_recommendations(title, cosine_sim=cosine_sim):
    idx = find_index(title)
    sim_scores = return_sorted(list(enumerate(cosine_sim[idx])))
    movies = find_movie_names(sim_scores)
    return movies

def create_recommendations(l):
    
    for i in range(len(l)):
        print("Recommended Movie "+str(i+1)+" : " +str(l[i]))

#create_recommendations(get_recommendations('Avatar'))

def change_list_len(x):
    return x[:5]

dataset['cast']=dataset['cast'].apply(change_list_len)

dataset['genres']=dataset['genres'].apply(change_list_len)

dataset['keywords']=dataset['keywords'].apply(change_list_len)

#Create another simple dateset
simple=dataset[['title', 'movie_id', 'director', 'popularity']]
#gathering info based on simple
directorlist=[]
for i in range(len(simple)):
    if simple['director'].iloc[i] not in directorlist:
            directorlist.append(simple['director'].iloc[i])


def clean_data_string(x):
    if type(x) == str:
        no_spaxce_string = x.replace(" ","")
        lower_case = str.lower(no_spaxce_string)
        return lower_case
    else:
        return ''
        
def clean_data_list(x):
    string_array = []
    for i in x:
        
        no_space_string = i.replace(" ","")
        lower_case = str.lower(no_space_string)
        string_array.append(lower_case)
        
    return string_array


dataset['cast'] = dataset['cast'].apply(clean_data_list)
dataset['keywords'] = dataset['keywords'].apply(clean_data_list)
dataset['director'] = dataset['director'].apply(clean_data_string)
dataset['genres'] = dataset['genres'].apply(clean_data_list)


def createstr(dataset):
    total = []
    string= ""
    i=dataset['keywords']
    j=dataset['cast']
    k=dataset['director']
    l=dataset['genres']
    for x in i:
        total.append(x)
    for y in j:
        total.append(y)
    total.append(k)
    for z in l:
        total.append(z)
    for a in total:
        string+=str(a)+" "
    return string

dataset['all_keywords'] = dataset.apply(createstr,axis=1)

from sklearn.feature_extraction.text import CountVectorizer

count = CountVectorizer(stop_words='english')
count_matrix = count.fit_transform(dataset['all_keywords'])


from sklearn.metrics.pairwise import cosine_similarity

cosine_sim2 = cosine_similarity(count_matrix, count_matrix)

#function used to return basic info of the movie to the user
def getinfo(x):
    for i in range(len(dataset)):
        if dataset.iloc[i]['title']==x:
            print('\nDetailed Info: \n')
            print('Title: ' +x +"\nGenres: "
                  +str(dataset.iloc[i]['genres']).strip('[]').replace(' ','')
                  +"\nHomepage: "
                  +str(dataset.iloc[i]['homepage']).strip('[]').replace(' ','')
                  +'\nOverview:\n' +str(dataset.iloc[i]['overview']))

#function used to return basic info of the movie to the user
moviebase=[]
for i in dataset['title']:
    moviebase.append(i)
from fuzzywuzzy import process
def doyoumean(x):
    return process.extractOne(x, moviebase)[0]

#Movie Recommender
def movie_recommendation():
    print('Thank you for using our movie recommender!')
    movieinput=input("Please enter a movie name ")
    if movieinput not in moviebase:
        similar=doyoumean(movieinput)
        response1=input('Do you mean ' + "\033[1m" + '%s' %similar + "\033[0;0m" +'?\nPlease input Y or N ' )
        if response1.upper() == 'N':
            print("Sorry we couldn't match your input movie name in our database\nPlease provide a more accurate name and try again " )
            return
        else:
            movieinput=similar
    feature=input('Do you want to get recommendations or detailed info about the movie?\nPlease input 1 for recommendation and 2 for detailed info ')
    if feature=='1':
        criteria=input("Do you want to get recommendation based on content or its features(cast, genre, etc)?\n Please input 1 for content, 2 for features ")
        if criteria == '1':
            return create_recommendations(get_recommendations(movieinput))
        else:
            return create_recommendations(get_recommendations(movieinput,cosine_sim2))
    else:
        return getinfo(movieinput)

#further function exploration
#we have simple,directorlist
def topmovie(name,simple):
    works={}
    for i in range(len(simple)):
        if simple['director'].iloc[i]==name:
            works.update({simple['title'].iloc[i]:simple['popularity'].iloc[i]})

    top=sorted(works.items(), key=lambda t: t[1],reverse=True)
    df = pd.DataFrame(top,columns=['movie','popularity'])
    return df       

def wantDirecor(name,directorlist):
    if name in directorlist:
        print("Yeah,we know him/her well! Here is the list of his/her works." )
        pop=topmovie(name,simple)
        return pop
    else:
        print("Sorry,we cannot find him/her")


movie_recommendation()
    
contin=input("Do you want explore more?\nPlease input Y or N ")

if contin.upper() == 'Y':
    print("Further Exploration our system! ")
    name=input("Please enter your favorite director.")
    result=wantDirecor(name,directorlist)
    print(result)     
print("Thank you for using our fantastic movie recommend system,See you next time!")



