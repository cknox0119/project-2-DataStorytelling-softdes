import requests
import json
import pandas as pd
import numpy as np


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





