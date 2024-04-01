import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import os

def AnalysisListGenerator(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    prices_raw = [price.text.strip() for price in soup.select('.fake-btn b')]
    numeric_prices = [re.search(r'(\d[\d,]*)', price).group().replace(',', '') for price in prices_raw if re.search(r'(\d[\d,]*)', price)]
    return numeric_prices

Waterloo = AnalysisListGenerator("https://findallrentals.ca/for-rent?location=waterloo-county&property_types=apartment")
Waterloo = Waterloo[-27:]
Toronto =  AnalysisListGenerator("https://findallrentals.ca/for-rent?location=toronto-county&property_types=apartment")
Vancouver = AnalysisListGenerator("https://findallrentals.ca/for-rent?location=vancouver&property_types=apartment")
Ottawa = AnalysisListGenerator("https://findallrentals.ca/for-rent?location=ottawa-county&property_types=apartment")
Montreal = AnalysisListGenerator("https://findallrentals.ca/for-rent?location=montreal-county&property_types=apartment")
Calgary = AnalysisListGenerator("https://findallrentals.ca/for-rent?location=calgary-county&property_types=apartment")

max_len = max(len(Waterloo), len(Toronto), len(Vancouver), len(Ottawa), len(Montreal), len(Calgary))
prices_array = np.full((max_len, 6), np.nan)

prices_array[:len(Waterloo), 0] = Waterloo
prices_array[:len(Toronto), 1] = Toronto
prices_array[:len(Vancouver), 2] = Vancouver
prices_array[:len(Ottawa), 3] = Ottawa
prices_array[:len(Montreal), 4] = Montreal 
prices_array[:len(Calgary),5] = Calgary 

def statistic_return():
    df = pd.DataFrame(prices_array, columns=['Waterloo', 'Toronto', 'Vancouver', 'Ottawa', 'Montreal', 'Calgary'])
    current_directory = os.path.dirname(os.path.abspath(__file__))
    data_file_path = os.path.join(current_directory, 'numeric_prices_data.csv')
    statistics_file_path = os.path.join(current_directory, 'numeric_prices_statistics.csv')
    df.to_csv(data_file_path, index=False)
    print(f"Data saved to: {data_file_path}")
    statistics = df.describe()
    statistics.to_csv(statistics_file_path)
    print(f"Statistics saved to: {statistics_file_path}")

statistic_return()
