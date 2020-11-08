# %matplotlib inline
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
    """
    return the imported data from a site, originally in json formatting.
    Args:
        url: string to find site
    Returns:
        data that is ready to be formatted further...(erwrite later)
    """
    data = requests.get(url)
    data = data.json()
    return data["features"]

def get_column_names(data):
    return data[0]["attributes"].keys()

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
def data_to_dataframe(data, column_names):
    country_data_formatted = []
    for each in data:
        country_data_formatted.append(each["attributes"])

    adoption_dataframe = pd.DataFrame(columns = column_names)

    for info in country_data_formatted:
        adoption_dataframe = adoption_dataframe.append(info, ignore_index=True)

    return adoption_dataframe

# find the data for one specific country:
def data_for_country(country_name, adoption_dataframe):
    return adoption_dataframe.loc[adoption_dataframe['Country'] == country_name]

def create_country_plot(data_country, country_name):
    # row_int = data_country.loc[data_country["Country Name"]== country_name]
    row_number = data_country.loc[data_country["Country"] == country_name].index.values[0]
    print(type(row_number))
    print(row_number)
    row_to_graph = data_country.iloc[row_number] 

    row_data = row_to_graph.values[1:-1]
    years = row_to_graph.index[1:-1]

    print(type(row_to_graph))

    fig, axs = plt.subplots()
    axs.scatter(years, row_data)
    axs.set_xticklabels(format_column_names(years))

    plt.xticks(rotation=90)

    # loc = plticker.MultipleLocator(base=5)
    # axs.xaxis.set_major_locator(loc)

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


