'''
This code takes a list of movies as inpout and returns a pandas dataframe with columns:
title, vote_average, release_date, original_title, original_language, overview.
In addition some commands provide data manipulation of the dataframe.
'''
import os
from dotenv import load_dotenv
load_dotenv()
import tmdbsimple as tmdb # This is a wrapper, written in Python, for The Movie Database (TMDb).
tmdb.API_KEY = os.getenv("TOKEN")
import pandas as pd
import numpy as np
import argparse
import create_df
import data_manipulation

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
    if args.movies:
        movies_df=create_df.create_movies_df(args.movies) 
        print(movies_df)
    else:
        movies_df=pd.read_csv('../output/movies_dataset.csv')
    if args.o == True:
       data_manipulation.overview(movies_df)
    elif args.c == True:
        data_manipulation.chronological_order(movies_df)
    elif args.a == True:
        data_manipulation.vote_average_desc(movies_df)            
    elif args.m == True:
        data_manipulation.max_min_vote_average(movies_df)

if __name__=='__main__':
    main()