import pandas as pd

def filter_data(df, time_interval, location, data_provider):

    data_filtered = df[df.nom == location][df.sourceType==data_provider][time_interval[1]>df.date][df.date> time_interval[0]]

    dates = data_filtered.date.tolist()
    deces_france = data_filtered.deces.tolist()
    
    return dates, deces_france