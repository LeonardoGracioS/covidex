import pandas as pd

def map_dep_region(df, inp, value, output):
    
    """Mapping function to find the corresponding region to a department or department number.
    
    :param df: DataFrame, default: None
        The region_department Dataframe.
    :param inp: string, default: None
        The input of the mapping : 'num_dep', 'dep_name' or 'region_name'.
    :param value: str or int, default: None
        The seeking value.
    :param output: string, default: None
        The output of the mapping : 'num_dep', 'dep_name' or 'region_name'.
    :return: Pandas DataFrame
"""

    row = df.loc[df[str(inp)] == value]
    
    if inp == 'region_name':
        return row[str(output)].values   
    
    return row[str(output)].values[0]