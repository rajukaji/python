'''
 Introduction to Query Parameters in APIs
Learn
Welcome to this lesson on Optional Query Parameters and Data Filtering! In an earlier lesson, we covered the basics of APIs and the Python requests library, including how to send HTTP requests, retrieve data from APIs, and handle errors. This foundational knowledge sets the stage for our next topic: optional query parameters in API interactions, a concept crucial not only in APIs but also in the world of Large Language Models (LLMs) like ChatGPT.

On this screen, we'll explore the significance of query parameters and data filtering techniques, focusing on their applications in APIs and LLMs. We'll start by understanding the role of optional query parameters in refining API requests to retrieve specific data sets. This concept mirrors the way LLMs process and analyze vast datasets, often encompassing billions of parameters, to understand and generate human-like text based on specific contexts or user queries.

Large Language Models and Data Filtering:
LLMs like ChatGPT are trained on extensive datasets to grasp the nuances of human language and generate relevant responses. When you prompt ChatGPT with a question, such as 'Explain the theory of relativity,' it filters through its dataset to find and compile information that aligns with your request. This process is analogous to using query parameters in an API to extract a subset of data from a larger dataset. Just as you might use a filter_by parameter (as we will see on the next screen) in an API to get data about a specific country or topic, ChatGPT uses its trained parameters to filter and generate a context-specific response. In both cases, the underlying concept involves selecting the most relevant information from a large pool of data to meet the specific needs of the query.

Understanding how query parameters work in API interactions provides valuable insights into the principles underlying LLMs' data processing and response generation. As we explore these concepts, you'll gain a deeper appreciation for the complexity and power of both APIs and LLMs in handling and interpreting vast amounts of information.
'''

'''
Further Exploration of Query Parameters in APIs
Learn
Having introduced the concept of query parameters and their relevance in both API interactions and Large Language Models, let's now take a closer look at how these parameters work in a more familiar context.

We will focus on the World Bank's Development Indicators, a comprehensive database containing detailed global development data for over 200 countries, some dating back more than 50 years. To enhance our interaction with this extensive resource, we have built a dedicated side server featuring our own APIs(https://api-server.dataquest.io/economic_data). This setup will provide streamlined access to the database, allowing us to efficiently utilize these valuable indicators in our coursework.

Imagine you're at a restaurant, and you order a burger. However, you don't just want any burger, you want it with extra cheese, no pickles, and a side of sweet potato fries instead of regular fries. In this scenario, the extra cheese, no pickles, and sweet potato fries are all specific instructions or parameters to modify your 'request' for a burger.


In the world of APIs, we often want to do something similar. Rather than retrieving all the data an API offers, we might want only a subset of that data. This is where optional query parameters come in. They allow us to specify or filter the data we want from an API, much like adding specific instructions to our burger order.

Optional query parameters allow us to select a subset of data from an API, rather than retrieving everything it offers. For instance, to filter data to only include countries in Sub-Saharan Africa, we use a query parameter in the URL, like https://api-server.dataquest.io/economic_data/countries?filter_by=region=Sub-Saharan%20Africa.

The World Development Indicators API supports these parameters, enabling refined searches. It has several endpoints, including /countries, /indicators, /country_series, /series_time, /footnotes, and /historical-data.

To illustrate, sending a GET request to the API without query parameters looks like this:

import requests
​
response = requests.get("https://api-server.dataquest.io/economic_data/countries")
data = response.json()

Explain

Copy
The data variable now holds a list of all countries in the database. However, if we are specifically interested in countries within a certain region, such as Sub-Saharan Africa, we need to utilize query parameters to refine our request. It's important to understand that not every API will accept the same query parameters, which is why consulting the API's documentation is essential. In our case, our API supports the filter_by parameter, which allows for more targeted searches.

We can modify our request to include this parameter:

response = requests.get("https://api-server.dataquest.io/economic_data/countries?filter_by=region=Sub-Saharan%20Africa")
data = response.json()

Explain

Copy
Here, the filter_by=region=Sub-Saharan%20Africa segment in the URL is a query parameter where:

? is a delimiter that marks the beginning of the query string. It separates the path of the URL from the parameters that are being passed.
filter_by indicates the type of filtering we are applying.
region is a specific field in the API's database that we want to filter by. In this context, region refers to the geographical area of the countries.
The first = sign following filter_by is used to assign the filtering criteria (region in this case), and the second = sign assigns the specific value (Sub-Saharan Africa) to the region field.
%20 is URL encoding for a space character, necessary because URLs cannot contain actual space characters. However, when composing a GET request in an editor or a tool, you don't need to manually type %20 for spaces; it is typically handled automatically by the software.
Now, the data variable holds a list of countries specifically in the Sub-Saharan Africa region. This demonstrates how query parameters can be effectively used, when supported by an API, to refine data requests according to our requirements.

In the upcoming exercises, you'll explore in detail API interactions using the World Development Indicators API. Your journey will guide you through refining data requests and query parameters, handling errors, and optimizing data retrieval.

'''

import requests
import json

response = requests.get('https://api-server.dataquest.io/economic_data/countries?filter_by=region=South Asia')

region_south_asia = response.json()
print(region_south_asia)


response = requests.get('https://api-server.dataquest.io/economic_data/indicators?filter_by=topic=Health: Risk factors&filter_by=periodicity=Biennial')

topic_str = response.json()

topic = json.loads(topic_str)

print(topic[0])
# print(topic['indicator_name'][0])


# invalid parameter

response = requests.get('https://api-server.dataquest.io/economic_data/indicators?filter_by=indicator_period=Biennial')

invalid_data_str = response.json()

print(invalid_data_str)


# pagination

parameters = {
    'limit' : 10,
    'offset' : 0
}

response = requests.get('https://api-server.dataquest.io/economic_data/countries', params=parameters)

data_with_pagination = json.loads(response.json())
# converted into python list

print(len(data_with_pagination))


parameters = {
    'limit':10,
    'offset':0
}

response = requests.get('https://api-server.dataquest.io/economic_data/indicators', params=parameters)

indicator_page_str = response.json()
# converting into json format

indicator_page = json.loads(indicator_page_str)
# parsing the json string into a python list of dictionaries

indicator_len_records = len(indicator_page)

fourth_indicator_name = indicator_page[3]['indicator_name']

print(indicator_len_records)
print(fourth_indicator_name)


# optimizin pagination

parameters = {
    'limit':50,
    'offset':0
}

response = requests.get('https://api-server.dataquest.io/economic_data/indicators', params=parameters)

data_page_1 = json.loads(response.json())
# python lists of dictionaries

parameters['offset'] = 50
parameters['limit'] = 50

response = requests.get('https://api-server.dataquest.io/economic_data/indicators', params=parameters)
# second request

data_page_2 = json.loads(response.json())
# python lists of dictionaries


print(data_page_2[0]['topic'])


parameters = {
    'filter_by':'region=Europe & Central Asia, income_group=Upper middle income',
    'limit':5,
    'offset':0
}

response = requests.get('https://api-server.dataquest.io/economic_data/countries', params=parameters)


data_combined_str = response.json()

data_combined = json.loads(data_combined_str)

for table_name in data_combined:
    country_name = table_name.get('table_name')
    print(country_name)