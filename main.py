import os
from dotenv import load_dotenv
load_dotenv()
import tmdbsimple as tmdb # is a wrapper, written in Python, for The Movie Database (TMDb).
tmdb.API_KEY = os.getenv("TOKEN")
import pandas as pd
import numpy as np
import argparse

def create_movies_df(movies):
    # It takes a list of movies as parameter and returns a pandas dataframe with columns:
    # title, vote_average, release_date, original_title, original_language, overview.
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
        movies_df.to_csv("./output/movies.csv")
    return movies_df

def overview(df):
    title=input('Tell me a movie and I tell you its overview: ')
    #os.system('clear')
    counter=1
    for e in df['title']:
        if e==title:
            return print(df['overview'][counter])
        else:
            counter+=1

def parse():
    parser = argparse.ArgumentParser()                 
    parser.add_argument('--movies',help='Insert a list of movies space separated and with ""', 
    nargs='+',type=str)
    parser.add_argument('-o', help='Insert a name from a movie in the list and returns its overview', 
    action='store_true')
    return parser.parse_args()

def main(): 
    args=parse()
    movies_df=create_movies_df(args.movies)
    print(movies_df)
    if args.o == True:
       overview(movies_df)  
    

if __name__=='__main__':
    main()