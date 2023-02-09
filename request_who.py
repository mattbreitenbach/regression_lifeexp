import pandas
import requests
import json

API_LINK = "https://ghoapi.azureedge.net/api/"

def get_indicator_code(indicators_name_list):

    request = requests.get(url="https://ghoapi.azureedge.net/api/Indicator")
    request.raise_for_status()
    list_api = request.json()
    dict_codes = {}
    
    for i in list_api["value"]:
        if i["IndicatorName"] in indicators_name_list:
            dict_codes[i["IndicatorCode"]] = i["IndicatorName"]
            
    return dict_codes


def get_indicator_data(indicator_name, filter_config):
    
    request = requests.get(url=f"{API_LINK}{indicator_name}?$filter={filter_config}")
    data = json.loads(request.text)['value']

    data_clean_list= []
    for country in data:
        data_clean_list.append([country['SpatialDim'], country['NumericValue']])
        
    columns = ["CountryCode", indicator_name]
    df = pandas.DataFrame(data_clean_list, columns=columns)
    return df


