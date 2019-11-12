import os
from dotenv import load_dotenv
load_dotenv()
import tmdbsimple as tmdb # This is a wrapper, written in Python, for The Movie Database (TMDb).
tmdb.API_KEY = os.getenv("TOKEN")
import pandas as pd
import numpy as np
import argparse

def create_movies_df(movies):
    movies_df=pd.DataFrame()
    for movie in movies:
        search = tmdb.Search() # Search movie data using The Movie Database API.
        movie = search.movie(query=movie)
        df=pd.DataFrame(search.results[0])
        df = df.drop(['popularity','vote_count','video','poster_path','id','adult',
        'backdrop_path','genre_ids','original_title','original_language'],axis=1)
        df = df.reindex(columns=['title','vote_average','release_date','overview'])
        df=df.drop_duplicates()
        movies_df=pd.concat([movies_df,df])
        movies=movies_df.reset_index(drop=True)
        movies_df.index = np.arange(1, len(movies_df) + 1)
        movies_df.to_csv("../output/movies_dataset.csv", index=False)
    return movies_df
