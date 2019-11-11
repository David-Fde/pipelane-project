# With this code data can be manipulated without the need of downloading all of them again.
import pandas as pd
import argparse

data = pd.read_csv('./output/movies_dataset.csv')

def overview(df):
    print(data)
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
    print(data)
    order=input('Chronological order ~ Ascending (A), Descending (D): ')
    while order != 'A' and order != 'D':
        order=input('Chronological order ~ Ascending (A), Descending (D): ')
    print("\n")
    if order == 'A':
        return print(df.sort_values(by='release_date',ascending=True))
    elif order == 'D':
        return print(df.sort_values(by='release_date',ascending=False))

def vote_average_desc(df):
    print(data)
    order=input('Vote average order ~ Ascending (A), Descending (D): ')
    while order != 'A' and order != 'D':
        order=input('Vote average order ~ Ascending (A), Descending (D): ')
    print("\n")
    if order == 'A':
        return print(df.sort_values(by='vote_average',ascending=True))
    elif order == 'D':
        return print(df.sort_values(by='vote_average',ascending=False))

def max_min_vote_average(df):
    print(data)
    value=input('Write M (Max) or m (Min) to get the value: ')
    while value != 'M' and value != 'm':
        ('Write M (Max) or m (Min) to get the value: ')
    if value == 'M':
        return print(df['vote_average'].max())
    elif value == 'm':
        return print(df['vote_average'].min())

def parse():
    parser = argparse.ArgumentParser()                 
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
    if args.o == True:
       overview(data)
    elif args.c == True:
        chronological_order(data)
    elif args.a == True:
        vote_average_desc(data)            
    elif args.m == True:
        max_min_vote_average(data)

if __name__=='__main__':
    main()