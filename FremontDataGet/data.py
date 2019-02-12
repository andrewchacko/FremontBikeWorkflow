import os
import pandas as pd
import matplotlib.pyplot as plt
from urllib.request import urlretrieve

FREMONT_URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'

# force_download - to the download whether file exists or not
def get_data(filename = 'Fremont.csv', url = FREMONT_URL, force_download = False):
        """Download and get Fremont Bike data"""
        if force_download or not os.path.exists(filename):
             urlretrieve(URL, filename)
        data = pd.read_csv('Fremont.csv', index_col='Date', parse_dates=True)
        data.columns = ['West', 'East']
        data['Total'] = data['West'] + data['East']
        
        return data
