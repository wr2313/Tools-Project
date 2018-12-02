def find_movie_names(l):
    movie_index = []
    movies = []
    
    for i in l:
        movie_index.append(i[0])
        
    for i in movie_index:
        movies.append(dataset['title'].iloc[i])
        
    return movies