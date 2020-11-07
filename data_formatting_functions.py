import requests
import json
import matplotlib.pyplot as plt
import pandas as pd

# request of whatever input link
# figure out type the data is --- json formatting, csv, excel, etc.
    # input line for what the data is 

# function formatting json files:
def format_json_files(input_data):
    data = input_data.json() # converts into json formatting input data into json format
    country_data_from_json = data["features"] # assign the input data's features to a seperate variable

    column_titles = format_column_names(column_names) # jump to outside function format_column_names to create the appropriate year titles

    # using pandas, below formats and adjusts the data to a proper dataframe:
    country_data = []
    for each in country_data_from_json:
        country_data.append(each["attributes"])

    df = pd.DataFrame(columns = column_names)

    for data in country_data:
        df = df.append(data, ignore_index=True)

    return df
# used in the function above to remove text and underscores found before the year titles:
def format_column_names(column_names):
    new_column_names = []
    for each in column_names:
        temp = each.split("_")
        if len(temp) == 2:
            new_column_names.append(temp[1])
        else:
            new_column_names.append(temp[0])
    return new_column_names

# function formatting csv files:
def format_csv_files(input_file_link):
    data = requests.get(input_file_link) # may or may not need this line, may do request statement outside of function
    with open('China_GDP.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if len(row) != 66:
                print(row)
                print()

    China_GDP_data = pd.read_csv("China_GDP.csv")