import os
from dotenv import load_dotenv
load_dotenv()
import tmdbsimple as tmdb
tmdb.API_KEY = os.getenv("TOKEN")
import pandas as pd
import numpy as np
import argparse

def create_movies_df(movies):
    # It takes a list of movies as parameter and returns a pandas dataframe with columns:
    # title, vote_average, release_date, original_title, original_language, overview.
    movies_df=pd.DataFrame()
    for movie in movies:
        search = tmdb.Search()
        movie = search.movie(query=movie)
        df=pd.DataFrame(search.results[0])
        df = df.drop(['popularity','vote_count','video','poster_path','id','adult',
        'backdrop_path','genre_ids','original_title','original_language'],axis=1)
        df = df.reindex(columns=['title','vote_average','release_date','overview'])
        df=df.drop_duplicates()
        movies_df=pd.concat([movies_df,df])
        movies=movies_df.reset_index(drop=True)
        movies_df.index = np.arange(1, len(movies_df) + 1)
    return movies_df


def parse():
    parser = argparse.ArgumentParser()                 
    
    parser.add_argument('movies', help='Movies', type=list)
    return parser.parse_args()

def main(): 
    args=parse()
    print(create_movies_df(args.movies))

if __name__=='__main__':
    main()