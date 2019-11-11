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



def chronological_order(df):
    return df.sort_values(by='release_date')

def vote_average_desc(df):
    return df.sort_values(by='vote_average',ascending=False)

def max_min_vote_average(df,value):
    if value == maximo:
        return print(df[df['vote_average'] == df['vote_average'].max()])
    elif value == minimo:
        return print(df[df['vote_average'] == df['vote_average'].min()]) 

def overview(df):
    title=input('Tell me a movie and I tell you its overview: ')
    #os.system('clear')
    counter=1
    for e in df['title']:
        if e==title:
            return print(df['overview'][counter])
        else:
            counter+=1

