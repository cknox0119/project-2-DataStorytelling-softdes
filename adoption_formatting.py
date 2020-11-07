import requests
import json
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.ticker as plticker


# FUNCTIONS TO MAKE:
# get the data with the URL input and format in json --- features to the data to be analyzed + establish column names
# format column names of data set 
# country data to DataFrame
# data of one country returning the series
# plot in other .py

# request data and initally format because of json formatting,
# establish beginning variables:
def get_data(url):
    data = requests.get(url)
    data = data.json()
    country_data = data["features"]

    column_names = country_data[0]["attributes"].keys()
    column_titles = format_column_names(column_names)
    years = column_titles[1:-1]

    return country_data

# format the column names, getting rid of unecessary characters
def format_column_names(column_names):
    new_column_names = []
    for each in column_names:
        temp = each.split("_")
        if len(temp) == 2:
            new_column_names.append(temp[1])
        else:
            new_column_names.append(temp[0])
    return new_column_names

# put the data into a dataframe:
def data_to_dataframe(country_data, column_names):
    country_data_formatted = []
    for each in country_data:
        country_data_formatted.append(each["attributes"])

    adoption_dataframe = pd.DataFrame(columns = column_names)

    for data in country_data_formatted:
        adoption_dataframe = adoption_dataframe.append(data, ignore_index=True)

    return adoption_dataframe

# find the data for one specific country:
def data_for_country(country_name, adoption_dataframe):
    data_country = adoption_dataframe.loc[adoption_dataframe['Country']== country_name]
    return data_country

def create_country_plot(data_country, column_titles, years, country_name, x_label, y_label, plot_title):
    # row_int = data_country.loc[data_country["Country Name"]== country_name]
    row_number = data_country.loc[data_country["Country Name"] == country_name].index
    row_to_graph = data_country.iloc[row_number] ## gets specific rows data --- How would I go about plotting this?
    
    row_data = row_to_graph.values[1:-1]
    # row_idx = row_to_graph.index[1:-1]

    fig, axs = plt.subplots()
    axs.scatter(years, row_data, label = "Uganda Adoptions over Time (Years)")
    plt.xticks(rotation=90)
    loc = plticker.MultipleLocator(base=5) # this locator puts ticks at regular intervals
    axs.xaxis.set_major_locator(loc)

    plt.xlabel(x_label)
    plt.ylabel(y_label)

    #title
    plt.title(plot_title)






