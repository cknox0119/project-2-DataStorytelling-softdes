import requests
import json
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.ticker as plticker
import csv

def get_csv(url):
    """
    return the imported data from a site
    Args:
        url: string to find site
    Returns:
        data that is ready to be formatted further, currently a csv file
    """
    input_file = requests.get(url)
    return input_file

# function formatting csv files:
def format_csv_files(input_file):
    """
    reformat the csv file, removing lines that are less than 66 characters as they interrupt pandas.
    remove the unecessary columns of information.
    Args:
        input_file: original data, unformatted, including the short lines
    Returns:
        data with consistent lengths amongst strings to be read by pandas
    """
    csv_data = pd.read_csv(input_file, sep=";")
    with open(input_file) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if len(row) != 66:
                print(row)
                print()

    csv_data = csv_data.drop(columns=['Country Code', 'Indicator Name', 'Indicator Code'])
    return csv_data

def create_column_names(csv_data):
    """
    create a list of column names from the formatted data
    Args:
        csv_data: formatted data of GDP information
    Returns:
        list of column name values
    """
    column_names = csv_data.columns.values
    return column_names

def find_years(column_names):
    """
    establish the years-span of the data and create the years into a list of strings.
    Args:
        column_names: list of strings that are column names of csv data
    Returns:
        list of strings that are purely numerical years
    """
    years = column_names[1:-1]
    return years

def data_country(country_name, csv_data):
    """
    find the data applicable for one specific country of interest
    Args:
        country_name: string input that allows user to clarify the name of the country to search
        csv_data: cleaned, reformatted dataframe of csv data
    Returns:
        series of the row of data for the specified country
    """
    data_country = csv_data.loc[csv_data['Country']== country_name]
    return data_country
    
def create_country_plot(data_country, country_name):
    """
    create the plot of the specified country
    Args:
        data_country: reformatted data for specific country
        country_name: name of the country of interest to search in dataframe
    Returns:
        plot of the adoption data of the specified country
    """
    row_number = data_country.loc[data_country["Country"] == country_name].index.values[0]
    row_to_graph = data_country.iloc[row_number] 

    row_data = row_to_graph.values[1:-1]
    years = row_to_graph.index[1:-1]

    fig, axs = plt.subplots()
    axs.scatter(years, row_data)
    axs.set_xticklabels(format_column_names(years))
    plt.xticks(rotation=90)
    loc = plticker.MultipleLocator(base=5)
    axs.xaxis.set_major_locator(loc)
    plt.xlabel("Time (years)")
    plt.ylabel("Annuel GDP")
    plt.title(country_name + " GDP vs Time")
    plt.show()
