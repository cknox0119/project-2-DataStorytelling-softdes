import requests
import json
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.ticker as plticker

def get_data(url):
    """
    return the imported data from a site, originally in json formatting.
    Args:
        url: string to find site
    Returns:
        data that is ready to be formatted further, currently in json formatting
    """
    data = requests.get(url)
    data = data.json()
    return data["features"]

def get_column_names(data):
    """
    find the attributes of the original data collected
    Args:
        data: unformatted, original data that was pulled from above
    Returns:
        attributes of the data collected
    """
    return data[0]["attributes"].keys()

def format_column_names(column_names):
    """
    format the column names, getting rid of unecessary characters
    Args:
        column_names: a list of the original column names from data collected
    Returns:
        list of column names with unecessary characters removed from strings
    """
    new_column_names = []
    for each in column_names:
        temp = each.split("_")
        if len(temp) == 2:
            new_column_names.append(temp[1])
        else:
            new_column_names.append(temp[0])
    return new_column_names

def data_to_dataframe(data, column_names):
    """
    formatting the attributes of the data into an appropriate dataframe with pandas
    Args:
        data: original data attributes
        column_names: list of column name strings
    Returns:
        dataframe of cleaned, reformatted data
    """
    country_data_formatted = []
    for each in data:
        country_data_formatted.append(each["attributes"])

    adoption_dataframe = pd.DataFrame(columns = column_names)

    for info in country_data_formatted:
        adoption_dataframe = adoption_dataframe.append(info, ignore_index=True)

    return adoption_dataframe

def data_for_country(country_name, adoption_dataframe):
    """
    find the data applicable for one specific country of interest
    Args:
        country_name: string input that allows user to clarify the name of the country to search
        adoption_dataframe: cleaned, reformatted dataframe of adoption data
    Returns:
        series of the row of data for the specified country
    """
    return adoption_dataframe.loc[adoption_dataframe['Country'] == country_name]

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
    plt.xlabel("Time (years)")
    plt.ylabel("Annuel Adoptions")
    plt.title(country_name + " Adoptions vs Time")
    plt.show()


if __name__ == "__main__":
    adoption_url = "https://services6.arcgis.com/R6wlO6UHmSzqm9Vs/arcgis/rest/services/Country_Adoptions_by_Year/FeatureServer/0/query?f=json&where=1=1&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&orderByFields=Country%20asc&resultOffset=0&resultRecordCount=2599&resultType=standard&cacheHint=true"
    raw_data = get_data(adoption_url)
    
    column_names = get_column_names(raw_data)
    dataframe = data_to_dataframe(raw_data, column_names)
    create_country_plot(dataframe, "China")


