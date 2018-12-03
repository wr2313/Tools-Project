<div align="center">
  <img src="https://pbs.twimg.com/media/DtYt8ywWwAA4xk0.jpg" width="800"><br>
</div>

-----------------
# Tools-Project

## Movie Recommender
Section 2

Group name: def group_name()

Team Member: Taimoor Chatoor, Wenchang Rong, Yaqi Zhang, Yue Zheng

## Description:
Let us show a quick demo of what our Movie Recommender can do!
<div align="center">
  <img src="https://media.giphy.com/media/24FIiakadcnXfy3GR6/giphy.gif" width="700"><br>
</div>


## Dataset:
Our TMDB 5000 Movie Dataset comes from kaggle (https://www.kaggle.com/tmdb/tmdb-movie-metadata).

The two csv files contain columns like movieid, overviews, directors and etc.

## What is it?:
Just enter a movie name and we'll be able to output an overview of the movie or generate a list of recommending movies based on it.

There are in total two ways that we recommend movies to you.

We can either give you recommendation based on the content of the movie, or based on its features(cast, genre, etc.)

If you would like to know movies directed by your favourite directors, we can also do that!

## Main Features:
1. Provide basic info about the input movie

	Preview:

<div align="center">
  <img src="https://i.imgur.com/Zc8xzIU.png" width="700"><br>
</div>

2. Content based recommendation system

	Attribute: Overview

3. Feature based recommendation system

	Attribute: Director, cast, keywords, genres
	check similarity using cosine similarity

3. A full list of the movies directed by your favourite director
	
	Attribute: director, movie names, popularity

## Installation instructions:

Here are all of packages we have implemented:
```
import pandas as pd
import numpy as np
import json
```
Install scikit-learn usinhg pip
```
pip install sklearn --upgrade
```

Use sklearn to support our similarity model
```
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
```
Use fuzzywuzzy to predict what user means (if the input is misspelled or in the wrong format)

first install packages
```
! pip install fuzzywuzzy
```
```
from fuzzywuzzy import process
```
## Run instructions

After cloning, please make sure you are in the right directory!

* Please run our code first

```
Message popup:	Thank you for using our movie recommender!
```

* Enter movie name you want to know

In any format (even if you missed word or misspelled,we handle that! Don't worry)


```
Message Popup: "Do you mean (something)?"
```

* We will return the most similar movie name in our movie base

```
Message Popup: "Do you want to get recommendations or detailed info about the movie?"
```

You can choose a feaure between this two. Enter 1 will generate recommendations, 2 will return basic information about the movie!


* If you want movie recommendation, there is a new

```
Message Popup: "Do you want to get recommendation based on content or its features(cast, genre, etc)?"
```

Please select your preferred approach, 1 for content, 2 for features.

* If you want know more director productions, Please enter Y and then enter an director name who interests you.
```
Message Popup: "Do you want explore more?
                  Please input Y or N"
```
  when you enter name please use format
   "First_name Last_name" eg."James Cameron"
```
Message Popup: "Further Exploration our system!
          Please enter director who interests you."
```
* Hope you enjoy with our system.
```
Message Popup: "Thank you for using our fantastic movie recommend system, See you next time!"
```
