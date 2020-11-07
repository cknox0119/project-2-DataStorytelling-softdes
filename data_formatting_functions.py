import requests
import json
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.ticker as plticker
import csv

def get_csv(url):
    input_file = requests.get(url)
    # remove the first rows that are not the majority character length...

    return input_file

# function formatting csv files:
def format_csv_files(input_file):
    csv_data = pd.read_csv(input_file, sep=";")
    
    with open(input_file) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if len(row) != 66:
                print(row)
                print()

    csv_data = csv_data.drop(columns=['Country Code', 'Indicator Name', 'Indicator Code'])
    # column_names = csv_data.columns.values
    return csv_data

def create_column_names(csv_data):
    column_names = csv_data.columns.values
    return column_names

def find_years(column_names):
    years = column_names[1:-1]
    return years

def data_country(country_name, csv_data):
    data_country = csv_data.loc[csv_data['Country']== country_name]
    return data_country
    
def create_country_plot(data_country, column_titles, years, country_name, x_label, y_label, plot_title):
    # row_int = data_country.loc[data_country["Country Name"]== country_name]
    row_number = data_country.loc[data_country["Country Name"] == country_name].index
    row_to_graph = data_country.iloc[row_number] ## gets specific rows data --- How would I go about plotting this?
    
    row_data = row_to_graph.values[1:-1]
    # row_idx = row_to_graph.index[1:-1]

    # scatter plot formatting:
    fig, axs = plt.subplots()
    axs.scatter(years, row_data)
    plt.xticks(rotation=90)
    loc = plticker.MultipleLocator(base=5) # this locator puts ticks at regular intervals
    axs.xaxis.set_major_locator(loc)

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(plot_title)
    
