import pandas as pd
import numpy as np
from datetime import datetime as dt

data_ip = pd.read_csv('car_prices.csv')
data_ip_mod=data_ip.dropna()

my_list = [ ]
for value in data_ip_mod['saledate']:
    original_string = value
    pattern = "GMT"
    parts = original_string.split(pattern, 1)
    # data_ip_mod['saledate_only'] = my
    my_list.append(parts[0])
data_ip_mod['saledate_only'] = my_list
data_ip_mod['saledate_only']

data_ip_mod.to_json('car_list-json.json', orient='records')