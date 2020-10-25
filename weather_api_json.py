

import urllib


import json 
url_body="https://www.metaweather.com/api/location/2487956"
temperature_dict={}

for i in range(1,30):   
    i_formatted = format(i, '02')
    date_value = f'/2020/2/{i_formatted}/'
    url_date = url_body+date_value
    response = urllib.request.urlopen(url_date)
    data=response.read()
    value = data.decode("utf-8")
    weather_dict = json.loads(value)
    for entry in weather_dict:
        created_date_split=entry['created'].split('T')
        created_date_only=created_date_split[0]
        if created_date_only==entry['applicable_date']: 
            value=entry['the_temp']
            if temperature_dict.get(created_date_only)==None: 
                values_list=[]
                values_list.append(value)
                temperature_dict[created_date_only]=values_list
            else: 
                temps=temperature_dict.get(created_date_only)
                temps.append(entry['the_temp'])
                temperature_dict[created_date_only]=temps




temp_stats_dictionary={}

for keys in temperature_dict: 
    temp_values = temperature_dict.get(keys)
    sum_temp = sum(temp_values)
    len_temp = len(temp_values)
    avg_temp = sum_temp/len_temp 
    min_temp = min(temp_values)
    max_temp = max(temp_values)
    value_list = [max_temp,min_temp,avg_temp]
    temp_stats_dictionary[keys]=value_list




with open("temp_stats.json", "w") as json_file:
    json.dump(temp_stats_dictionary, json_file)

