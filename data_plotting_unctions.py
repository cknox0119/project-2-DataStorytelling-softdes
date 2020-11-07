import requests
import json
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.ticker as plticker
import csv

# pull data from the formatting functions py whether from json or csv:
# another import statement...?

#input_data = #
def scatter_plot(input_data, country_name):
    row_int = input_data.loc[input_data["Country Name"]== country_name]
    row_number = input_data.loc[input_data["Country Name"] == country_name].index
    row_to_graph = input_data.iloc[107] ## gets specific rows data --- How would I go about plotting this?
    
    row_data = row_to_graph.values[1:-1]
    row_idx = row_to_graph.index[1:-1]

    fig, axs = plt.subplots()
    axs.scatter(years, row_data, label = "Uganda Adoptions over Time (Years)")
    plt.xticks(rotation=90)
    loc = plticker.MultipleLocator(base=5) # this locator puts ticks at regular intervals
    axs.xaxis.set_major_locator(loc)

    plt.xlabel("Time (Years)")
    plt.ylabel("Annual GDP")

    #title
    plt.title("India's GDP vs Time (Years)")

    return plt