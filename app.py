import pandas as pd

sheet_id = '1iKSZsqWUoPISFn3bcwtMQS7aFIOulm3qmnv1a9Oe2To'

df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")

#FilterDB will filter out all rows with column dates that are Tuesday, and filter out all rows with GuestStars column containing Catherine Tate
def filter_db():
    #Identify day of week for each episode date. New column named 'Weekday'
    df['Weekday']=pd.DatetimeIndex(df.Date).weekday

    #Identify all 'Weekdays' that are Tuesdays. 1 = Tuesday
    index_tuesdays = df[(df['Weekday'] == 1)].index

    #Index and identify all episodes starring Catherine Tate, or her stage name Nellie Bertram
    index_cath = df[(df['GuestStars'] == "Catherine Tate")].index
    
    #Drop all rows containing Catherine Tate by using our index variable that identified the episodes in our DB.
    df.drop(index_cath, inplace=True)
    
    #Drop all rows containing Tuesday by using our index variable that identified all Tuesdays in our DB.
    df.drop(index_tuesdays, inplace=True)
    
    return df

#Invoke the function inside of a print statement to view our results
print(filter_db())

def writer_viewership_avg():
    
    #Make a new dataframe, df2, and then Split up the writers, with new rows for each episode for each individual show Writer. 
    df2 =df.assign(Writers=df['Writers'].str.split('|')).explode('Writers').reset_index(drop=True)
  

    #After splitting our 'Writers' column by '|', there is whitespace left behind. We can strip this, making it possible to find the mean and remove any duplication bugs from appearing
    df2['Writers'] = df2['Writers'].str.strip()

    #In this data frame, since we have collected all episode data and filtered it properly, now we only are wanting to view the viewership of all individual writers. So we drop all unrelated columns for this solution
    df2 = df2.drop(columns=["Season","EpisodeTitle","About","Ratings","Votes","Duration","Date","GuestStars","Director","Weekday"])

    #Here, we declare a mean variable. We find the mean by merging the writers, and finding their average viewership by invoking .mean()
    viewership_mean = df2.groupby(['Writers']).mean()



    #Print our viewership average results
    return viewership_mean


#Invoke the function inside of a print statement to view our results
print(writer_viewership_avg())



