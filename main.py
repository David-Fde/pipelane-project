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
    print("\n")
    title=input('Tell me a movie (exact title) and I tell you its overview: ')
    while title not in list(df['title']):
        title=input('Tell me a movie (exact title) and I tell you its overview: ')
    print("\n")
    counter=1
    for e in df['title']:
        if e==title:
            return print(df['overview'][counter])
        else:
            counter+=1

def chronological_order(df):
    print("\n")
    order=input('Chronological order ~ Ascending (A), Descending (D): ')
    while order != 'A' and order != 'D':
        order=input('Chronological order ~ Ascending (A), Descending (D): ')
    print("\n")
    if order == 'A':
        return print(df.sort_values(by='release_date',ascending=True))
    elif order == 'D':
        return print(df.sort_values(by='release_date',ascending=False))

def vote_average_desc(df):
    print("\n")
    order=input('Vote average order ~ Ascending (A), Descending (D): ')
    while order != 'A' and order != 'D':
        order=input('Vote average order ~ Ascending (A), Descending (D): ')
    print("\n")
    if order == 'A':
        return print(df.sort_values(by='vote_average',ascending=True))
    elif order == 'D':
        return print(df.sort_values(by='vote_average',ascending=False))
        
def max_min_vote_average(df):
    print("\n")
    value=input('Write M (Max) or m (Min) to get the value: ')
    while value != 'M' and value != 'm':
        ('Write M (Max) or m (Min) to get the value: ')
    if value == 'M':
        return print(df['vote_average'].max())
    elif value == 'm':
        return print(df['vote_average'].min()) 

def parse():
    parser = argparse.ArgumentParser()                 
    parser.add_argument('--movies',help='Insert a list of movies. Ex: "Hulk" "Thor". Write the exact name.', 
    nargs='+',type=str)
    parser.add_argument('-o', help='Insert a valid and exact name of a movie in the list and returns its complete overview.', 
    action='store_true')
    parser.add_argument('-c', help='Returns the list in chronological order.', 
    action='store_true')
    parser.add_argument('-a', help='Returns the list in average order.', 
    action='store_true')
    parser.add_argument('-m', help='Returns the Max or Min average value.', 
    action='store_true')
    return parser.parse_args()

def main(): 
    args=parse()
    movies_df=create_movies_df(args.movies)
    print(movies_df)
    if args.o == True:
       overview(movies_df)
    elif args.c == True:
        chronological_order(movies_df)
    elif args.a == True:
        vote_average_desc(movies_df)            
    elif args.m == True:
        max_min_vote_average(movies_df)

if __name__=='__main__':
    main()