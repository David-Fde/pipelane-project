def overview(df):
    print(df)
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
    print(df)
    order=input('Chronological order ~ Ascending (A), Descending (D): ')
    while order != 'A' and order != 'D':
        order=input('Chronological order ~ Ascending (A), Descending (D): ')
    print("\n")
    if order == 'A':
        return print(df.sort_values(by='release_date',ascending=True))
    elif order == 'D':
        return print(df.sort_values(by='release_date',ascending=False))

def vote_average_desc(df):
    print(df)
    order=input('Vote average order ~ Ascending (A), Descending (D): ')
    while order != 'A' and order != 'D':
        order=input('Vote average order ~ Ascending (A), Descending (D): ')
    print("\n")
    if order == 'A':
        return print(df.sort_values(by='vote_average',ascending=True))
    elif order == 'D':
        return print(df.sort_values(by='vote_average',ascending=False))

def max_min_vote_average(df):
    print(df)
    value=input('Write M (Max) or m (Min) to get the value: ')
    while value != 'M' and value != 'm':
        ('Write M (Max) or m (Min) to get the value: ')
    if value == 'M':
        return print(df['vote_average'].max())
    elif value == 'm':
        return print(df['vote_average'].min())
