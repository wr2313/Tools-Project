def get_recommendations(title, cosine_sim=cosine_sim):
    idx = find_index(title)
    sim_scores = return_sorted(list(enumerate(cosine_sim[idx])))
    movies = find_movie_names(sim_scores)
    return movies