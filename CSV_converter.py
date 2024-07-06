import pandas as pd
import json

def CSV_converter1(path1,path2):                                                                                                        

    df = pd.read_json(path1)
    #print(df)
    df.to_csv(path2)
