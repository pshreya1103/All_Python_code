import pandas as pd
import numpy as np
from datetime import datetime as dt

INPUT_FILE_PATH = '/Users/shreyapandey/Desktop/Python-practice/car_prices.csv'
OUTPUT_FILE_PATH = '/Users/shreyapandey/Desktop/ETL/car_prices_JSON.json'

def readetl():
	return (pd.read_csv(f'{INPUT_FILE_PATH}'))

def transform(df_ip):
    my_list = [ ]
    df_ip_mod=df_ip.dropna()
    for value in df_ip_mod['saledate']:
        pattern = "GMT"
        parts_final=extrcatetl(value,pattern)
        my_list.append(parts_final)
    df_ip_mod['saledate_dt_only'] = my_list
    return df_ip_mod

def extrcatetl(string,pattern):
	parts = string.split(pattern, 1)
	return(parts[0])

def loadetl(df):
	df.to_json(f'{OUTPUT_FILE_PATH}', orient='records')
    # print(f'File loaded at path: {OUTPUT_FILE_PATH}')
    
# EXTRACT 

df_ip = readetl() #Extracting data 
df_op_mod = transform(df_ip)
loadetl(df_op_mod)