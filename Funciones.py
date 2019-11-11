def right_order():
    return mcu_df['title']  

def chronological_order():
    return mcu_df.sort_values(by='release_date')

def vote_average_desc():
    return mcu_df.sort_values(by='vote_average',ascending=False)

def max_min_vote_average('value'):
    if value == maximo:
        return print(mcu_df[mcu_df['vote_average'] == mcu_df['vote_average'].max()])
    elif value == minimo:
        return print(mcu_df[mcu_df['vote_average'] == mcu_df['vote_average'].min()]) 

def overview():
    title=input('Tell me a movie and I tell you its overview: ')
    #os.system('clear')
    counter=1
    for e in mcu_df['title']:
        if e==title:
            return print(mcu_df['overview'][counter])
        else:
            counter+=1