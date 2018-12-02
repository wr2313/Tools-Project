<div align="center">
  <img src="https://pbs.twimg.com/media/DtYt8ywWwAA4xk0.jpg"><br>
</div>

-----------------
# Tools-Project

## Movie Recommender
Section 2: def group_name()

Team Member: Taimoor Chatoor, Wenchang Rong, Yaqi Zhang, Yue Zheng

## Description:
Let us show a quick demo of what our Movie Recommender can do!
<div align="center">
  <img src="https://media.giphy.com/media/24FIiakadcnXfy3GR6/giphy.gif"><br>
</div>


## Dataset:
Our TMDB 5000 Movie Dataset comes from kaggle (https://www.kaggle.com/tmdb/tmdb-movie-metadata).

The two csv files contain columns like movieid, overviews, directors and etc.

## What is it?:
Just enter a movie name and we'll be able to output an overview of the movie or generate a list of recommending movies based on it. There are in total two ways that we recommend movies to you. We can either give you recommendation based on the content of the movie, or based on its features(cast, genre, etc.)

## Main Features:
1. Provide basic info about the input movie

	Preview:

<div align="center">
  <img src="https://i.ibb.co/bBZmT5B/overview.jpg"><br>
</div>

2. Content based recommendation system

	Attribute: Overview

3. Feature based recommendation system

	Attribute: Director, cast, keywords, genres
	check similarity using cosine similarity

## Installation instructions:
Here are all of packages we have implements
```
import pandas as pd
import numpy as np
import json
```
Use sklearn to support our similarity model
```
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
```
Use fuzzywuzzy to predict what user mean
first install packages
```
! pip install fuzzywuzzy
```
```
from fuzzywuzzy import process
```
## Run instructions:
1.
