'''
APIs and the Requests Library
1 of 9 · Introduction to APIs
Learn
In this lesson, we will explore the concept of APIs (Application Programming Interfaces) and how they are utilized in Python applications. APIs play a crucial role in enabling communication between different software components, allowing them to exchange and transmit data and perform various operations.

Picture the last time you used a web application where you had to enter your personal information into a form. You may have entered information like your name, address, phone number, and more. Once you hit the submit button, what happens next? How does that information get transmitted into a usable format for the application to use later on?

One way this can be accomplished is through the use of an API. It may help to think of an API as the waiter of the digital world. APIs are the go-betweens that ensure seamless communication between different software components, facilitating data exchange and operations.

Imagine going to a restaurant and placing an order. You provide your order, perhaps your entree and side dish choices and drink order, to the waiter, who then communicates your request to the kitchen. Once the kitchen has prepared your meal, the waiter brings it back to you. What happens when you hit the submit button in a web application, as mentioned above, is somewhat similar - the API acts like the waiter taking your data (order) and relays it in a digestible form to the software (kitchen) that processes it.


Throughout this lesson, we will use the ExchangeRate API to access the latest currency rates for all countries. This API will act as our specialized waiter, bringing us the latest currency rates from all over the world. To see it in action, type the following URL into your browser and see what you get:

https://api.exchangerate-api.com/v4/latest/usd

Let’s break down and define a few key terms relating to APIs that will help us understand what happens when we access the above URL:

API (Application Programming Interface): This is our waiter, a set of definitions and rules that allows different software components (like our tables and the kitchen) to communicate and interact with each other. It defines how data can be requested, accessed, and updated between different systems.
Endpoint: An endpoint is a specific URL (Uniform Resource Locator) that represents a unique resource or functionality provided by an API. Endpoints act as access points through which we can send requests and receive responses. We can access the specific endpoint, /v4/latest/usd, to get the latest exchange rates for USD (United States Dollar) relative to other country’s currencies. We could also change this to https://api.exchangerate-api.com/v4/latest/cad to access a different endpoint and receive exchange rates for CAD (Canadian Dollar) as well. Endpoints are similar to ordering a specific dish from the menu. We could tell our waiter that we want to order the chowder, which is the equivalent of asking the ExchangeRate API (our waiter) for the USD currency exchange rates.
HTTP Request: Hypertext Transfer Protocol (HTTP) is a message sent over the internet that requests for a specific action to be performed or certain information to be returned. In our above example, we are requesting information on the currency exchange rates for USD. The moment we ask our waiter for the chowder, we request a specific action taken and to have some response returned (our meal). So, you can think of an HTTP Request as the order itself. An HTTP request consists of several components:
URL (Uniform Resource Locator): This is the URL, or endpoint, to be called to obtain the requested information or perform the requested action. Again, this is the item we are ordering.
Method: This indicates the type of action to be performed on the resource. The two common methods are GET and POST.
GET: This is like asking for information. The request asks to retrieve or fetch data from the endpoint. An example would be asking for a menu item and receiving the dish back to eat.
POST: This is like submitting a form or sending data. The request includes data that needs to be processed or stored by the recipient. An example would be giving the chef a special recipe to prepare, where you need to supply additional information for your request to be fulfilled.
Headers: These provide additional information about the request, such as the type of data sent (for example, string or JSON data) or authentication credentials. An example would be providing extra information about how you want your meal, like that it should be gluten-free.
Body: In the case of a POST request, the body contains the data that needs to be sent to the recipient. Depending on the requirements, it can include form data, JSON, or other formats. In the example where you provide the chef with your special recipe to cook, the body would contain all the ingredients needed to make the recipe.
HTTP Response: When an HTTP request is sent, the recipient receives the request and processes it based on the endpoint that was called, the method, headers, and body. The recipient then generates an appropriate response, which could include the requested information, a confirmation message, or an error if something goes wrong. In our example, the response was a JSON-formatted string that maps countries to their exchange rates. When you place your order, it gets sent to the kitchen, where the order is processed and prepared, and the meal is returned as the response. If something was wrong with your order preventing it from being prepared, an error message could also be returned to you by the waiter.
Before we dive into further detail of all the concepts above, let’s practice calling a few more endpoints from our browser using the ExchangeRate-API.

'''

'''
2 of 9 · Requests Library
Learn
In order to interact with APIs, we need to know how to make HTTP requests. An HTTP request is a message sent by a client (such as a web browser or a Python script) to a server, or the recipient. The server then sends back an HTTP response containing the requested data.

On the previous screen, we used our browser to access the API endpoints to retrieve the currency exchange rates. We can also make these HTTP request API calls through our Python code using a library module called requests. This module provides an easy way to send HTTP requests, handle responses, and manage various aspects of the request process.

As with other modules, we start using it by importing it. We can then call the get() command to get the response data containing the exchange rates.

import requests
​
endpoint = 'https://api.exchangerate-api.com/v4/latest/usd'
​
# Make a GET request to the API endpoint
response = requests.get(endpoint)
print(type(response))
print(response)

Explain

Copy
Output
< class 'requests.models.Response'>
< Response [200] >
We will explain how the get() command works in more detail later in this lesson. But, for now, we can see that calling get() with our endpoint returns a value representing the HTTP response. As you can see, the type of the response is requests.models.Response. You may also wonder why printing the response shows an odd output, <Response [200]>. This code doesn't give us the exchange rates we thought it would because we first need to convert and parse the response data as JSON. We will learn how to convert the response into a usable, parsable Python dictionary on the next screen.

First, let's try practicing importing the requests library and making an HTTP request on an endpoint.

Instructions
Import the requests library.

Set a variable called endpoint_url to 'https://api.exchangerate-api.com/v4/latest/cad'.

Call requests.get() using the endpoint stored in endpoint_url. Set the response to a variable called response.

Print both response and the type of response.

'''

import requests

endpoint_url = 'https://api.exchangerate-api.com/v4/latest/cad'

response = requests.get(endpoint_url)

print(response)
print(type(response))

# Converting the HTTP Response to JSON

'''
Printing the response, we see a 200 that follows Response, which represents the status code of the request. We will learn more about status codes later on, but for now, know that the status code 200 means that the request was able to return a response successfully.

But how do we actually retrieve the currency exchange rate data?

To turn this JSON response into a Python dictionary, we can call json() on our response variable. This parses the response into JSON and then returns it as a Python dictionary that we can then access using key/value pairs:

import requests
​
endpoint = 'https://api.exchangerate-api.com/v4/latest/usd'
​
# Make a GET request to the API endpoint
response = requests.get(endpoint)
print(type(response))
response_json = response.json()
print(response_json)
print(type(response_json))

Explain

Copy
Output
​
{'provider': 'https://www.exchangerate-api.com', 'WARNING_UPGRADE_TO_V6': 'https://www.exchangerate-api.com/docs/free', 'terms': 'https://www.exchangerate-api.com/terms', 'base': 'USD', 'date': '2023-05-31', 'time_last_updated': 1685491201, 'rates': {'USD': 1, 'AED': 3.67, 'AFN': 87.47, 'ALL': 102.79, 'AMD': 386.61, 'ANG': 1.79, 'AOA': 576.79, 'ARS': 237.99, 'AUD': 1.53, 'AWG': 1.79, 'AZN': 1.7, 'BAM': 1.82,...
When we print the contents of response_json, we can see that our dictionary now resembles the result we saw in our browser. We can print the type of response_json and see that it is now a dictionary instead of a response. Our dictionary has several different key and value mappings. Let's discuss what some of these keys and values are:

rates: a dictionary that maps country codes to their exchange rates. When we want to get an exchange rate for a specific country, we should use this key and value to retrieve the value.

provider: the main URL for the API, without any added-on endpoint.

terms: links to the terms and conditions for using the API.

base: the base currency, or our original currency, that we requested exchange rates for in our initial endpoint (i.e., https://api.exchangerate-api.com/v4/latest/usd).

date: the date we made the HTTP request.

time_last_updated: the timestamp when the currency exchange rates were last updated. It is a Unix timestamp, which is the number of seconds that have elapsed since January 1, 1970 (also known as the Unix epoch).

WARNING_UPGRADE_TO_V6: this key is simply a warning to switch to using the latest version (V6) of the API provider URL. We are using version V4 in our examples throughout this lesson since V4 is completely free and open to use, whereas V6 requires account creation. You are more than welcome to experiment with using V6 by following the ExchangeRate-API documentation listed here.
'''



import requests

endpoint_url = 'https://api.exchangerate-api.com/v4/latest/gbp'

response = requests.get(endpoint_url)

response_dict = response.json()

print(type(response))

print(type(response_dict))

for key in response_dict:
    print(key)


'''
GET Method
Learn
On the previous screen, we introduced that an HTTP request uses different methods to send or retrieve data. In this lesson, we are covering two of these methods, specifically the GET and POST methods.

The GET method is an HTTP method used for retrieving data from a server. It is widely used in programming, particularly with APIs. It is a safe method to use because it does not modify or have any side effects on the server's data like the POST method does. The primary purpose of the GET method is to retrieve information and resources. It can retrieve data in various formats but typically in HTML (Hypertext Markup Language), XML, and JSON.

Let's review how to use the GET method:

import requests
​
endpoint = 'https://api.exchangerate-api.com/v4/latest/usd'
​
# Make a GET request to the API endpoint
response = requests.get(endpoint)

Explain

Copy
The response can be accessed similarly as we did with the POST method by converting to a dictionary and accessing any of the keys present in the dictionary. In this example, if we print the response dictionary, we can access response['rates'] to get the whole dictionary of country codes and their exchange rates.

import requests
​
endpoint = 'https://api.exchangerate-api.com/v4/latest/usd'
​
# Make a GET request to the API endpoint
response = requests.get(endpoint)
response_dict = response.json()
​
print(response_dict['rates'])

Explain

Copy
Output
​
{'USD': 1, 'AED': 3.67, 'AFN': 86.98, 'ALL': 101.34, 'AMD': 387.06, 'ANG': 1.79, 'AOA': 597.08, 'ARS': 240.52, 'AUD': 1.51, 'AWG': 1.79, 'AZN': 1.7, 'BAM': 1.83, 'BBD': 2, 'BDT': 107.23, 'BGN': 1.83, 'BHD': 0.376, 'BIF': 2816.76, 'BMD': 1, 'BND': 1.35, 'BOB': 6.91, 'BRL': 5, 'BSD': 1, 'BTN': 82.44, 'BWP': 13.74, 'BYN': 2.82, 'BZD': 2, 'CAD': 1.34, 'CDF': 2280.71, 'CHF': 0.909, 'CLP': 800.75, 'CNY': 7.1, 'COP': 4360.84, 'CRC': 542.26, ...
GET requests can include query parameters as part of the URL. These parameters provide additional information to the server to refine the request or filter the response data. Query parameters are appended to the URL using the ? symbol, followed by key-value pairs separated by &.

Note: The following code example is not a live-working endpoint but demonstrates how to construct an endpoint with added parameters.

import requests
​
url = 'https://api.exchangerate-api.com/v4'
​
# Specify the parameters for the GET request
param1 = 'usd'
param2 = 'cad'
​
# Construct the URL with parameters
full_url = url + '?param1=' + param1 + '&param2=' + param2
​
response = requests.get(full_url)

Explain

Copy
The server side can then, for example, take these provided parameters to filter returned results or to perform a conversion from USD to CAD.

The GET method does not include a request body like the POST method. As we learn more about the POST method on the next screen, we will also cover the request body. For now, know that the GET method does not need a request body and that all the necessary information is passed through the URL and query parameters instead.

Let's practice making some more GET calls and accessing the response data.

Instructions
Loop through every currency code in currencies using a loop variable called currency_code. In each loop iteration:
Build the URL endpoint for the request by concatenating base_url and currency_code and store in a variable called url.
Call requests.get() on url and set the response to a variable called response.
Convert response to a Python dictionary using json() and set the result back to response.
Print the value of response['rates']['USD'] to get the USD rate for each currency code.
'''


import requests

currencies = ['EGP', 'GMD', 'CLP']
base_url = "https://api.exchangerate-api.com/v4/latest/"


for currency_code in currencies:
    url = base_url + currency_code
    
    response = requests.get(url)
    
    response = response.json()
    
    print(response['rates']['USD'])



    '''

     POST Method
Learn
The POST method is one of the HTTP methods used in applications to send data to a server, or the recipient of our HTTP request. It is commonly used to create or update resources on the server. For example, when you create a new account on a website, the information you submit is sent to the server using a POST request.

Note: The following code example is not a live-working endpoint but simply demonstrates how to construct a POST call.

# Define the API endpoint URL where the account creation information will be submitted
endpoint = "https://example.com/api/create-account"
​
# Prepare the account creation data as a dictionary
account_data = {
    "username": "example_user",
    "email": "example@example.com",
    "password": "example_password"
}
​
# Make the POST request to submit the account creation data

Explain

Copy
This method submits data and requests the server to act based on that data. On the server side, it can parse all of the data from account_data sent in the request and take an action like storing your new account information in a database.

The POST method can send data to the server within the request body. The body can contain different data types, such as JSON, XML (Extensible Markup Language), form data, or plain text, depending on the content type specified when submitting the request. After the URL endpoint is specified, the body is passed into the post() call. It is set to the parameter called data if our data is in string format or to the parameter called json if the data is a dictionary.


The following code example is also not a live-working endpoint but simply demonstrates how to construct a POST call. We cannot make any POST calls using the free and open ExchangeRate-API endpoints. API providers offering open access endpoints will typically have restricted access to their POST methods for security reasons. Allowing unrestricted POST requests from any unregistered user could lead to unauthorized modification of the server's data, posing a security risk.

Since we cannot practice using POST calls directly, we have simulated what a POST call would look like using the ExchangeRate-API:

import requests
​
url = 'https://api.exchangerate-api.com/v4/convert'
​
# Specify the parameters for the POST request
payload = {
    'from': 'USD',         # Convert from USD
    'to': 'EUR',           # Convert to EUR
    'amount': 100          # Specify the amount to convert
}
​
response = requests.post(url, json=payload)
​
data = response.json()

Explain

Copy
In the above code, there is a parameter, or a value being passed to the endpoint, called json that is set to the payload we want to send to the server. We used the json parameter since our payload variable is a dictionary.

Continuing with our POST example, we are sending the following information in our payload dictionary:

The currency we want to convert from
The currency we want to convert to
The amount we wanted to be converted
On the server side, the server or API endpoint processes the request body to extract and handle the data that was sent. The server may parse the data based on the specified content type and perform actions such as storing the data in a database, updating records, or triggering other code logic based on the received information. In this simulated example, the server side would perform some logic like retrieving the USD conversion rates, specifically the rate for EUR, and then taking the amount and multiplying it by the conversion rate. This would then get sent back in the form of an HTTP response. The JSON response may resemble something like this:

{
    "result": 93.43
}

Explain

Copy
We can unbundle the response by first converting the response to a dictionary using json() and then accessing the key result in the dictionary to get the final converted amount:

response = requests.post(url, json=payload)
​
data = response.json()
converted_amount = data['result']
print(converted_amount)

Explain

Copy
Output
​
93.43

'''

'''

· Converting JSON Data to Strings
Learn
On the previous screen, we set the json attribute in the requests.post() call to send our payload dictionary data.

We could have instead used the data attribute by converting our payload dictionary into a string first. The json module that we have previously introduced has a command called dumps() that lets us do just this:

import json
import requests
​
url = 'https://api.exchangerate-api.com/v4/convert'
​
# Specify the parameters for the POST request
payload = {
    'from': 'USD',         # Convert from USD
    'to': 'EUR',           # Convert to EUR
    'amount': 100          # Specify the amount to convert
}
​
payload_str = json.dumps(payload)
print(payload_str)
print(type(payload_str))
response = requests.post(url, data=payload_str)

Explain

Copy
Output
{"from": "USD", "to": "EUR", "amount": 100}
< class 'str' >
The json.dumps() command takes our payload dictionary and returns a string representation of that dictionary in JSON format. When we print the type that is returned after calling json.dumps(), we get back a str type. Once our payload is converted to a string, it can then be passed into the data attribute in the requests.post() call.

Using json.dumps() is particularly useful when an API specifically requires JSON-formatted string data in the request body.


In case you are wondering what some of the use cases are for when to use the data attribute versus the json attribute in the POST call, here are a few:

You can use the data attribute when:

The API expects the request payload to be in a format other than JSON, like form data encoded in a string format.
When sending a string or bytes-like object as the payload.
Example data: Form data or file uploads.
You can use the json attribute when:

The API expects the request payload to be in JSON format.
You want to automatically serialize a Python object (like a dictionary or list) into JSON format.
Example data: Sending a Python dictionary to an API that accepts JSON payloads.

'''

import json
# importing json library

exchange_rate_map = {
    'EUR': 0.927,
    'USD': 1,
    'CAD': 1.33,
    'JPY': 139.9,
    'GBP': 0.794
}
print(type(exchange_rate_map))

exchange_rate_map_str = json.dumps(exchange_rate_map)

print(exchange_rate_map_str)

'''
Formatting Strings
Learn
In Python, there's a powerful tool called f-strings (also known as "formatted string literals") that allows us to embed expressions inside string literals, using curly braces {}. This makes it easier to construct and manipulate strings.

The syntax of an f-string is straightforward: prefix the string with a lowercase f or an uppercase F before the opening quotation mark. Within the string, any expressions placed within curly braces {} are evaluated and replaced with their results.

Let's look at how we can use this with our API calls:

Let's say we want to convert from one specific currency to another and we want to make these currencies dynamic. We can use f-strings to construct our API URL endpoint.

base_currency = 'USD'
​
url = f'https://api.exchangerate-api.com/v4/latest/{base_currency}'
print(url)

Explain

Copy
https://api.exchangerate-api.com/v4/latest/USD

Explain

Copy
In this example, base_currency is a variable. By using f-strings, we can construct the URL to fetch the conversion rates for a currency without having to manually edit the URL each time.

F-strings can also be used when constructing the payload for a POST request. For example:

base_currency = 'USD'
target_currency = 'EUR'
amount_to_convert = 100
​
payload = f'{{"from": "{base_currency}", "to": "{target_currency}", "amount": {amount_to_convert}}}'
print(payload)

Explain

Copy
{"from": "USD", "to": "EUR", "amount": 100}

Explain

Copy
This code creates a JSON-formatted string that includes variable content, using f-string formatting. It's important to use double curly braces {{}} when you want to include a literal brace character in the formatted string.

Please remember that although f-strings can be very useful for string formatting, the json.dumps() function is often a better choice when working with more complex data structures because it automatically handles special characters and escape sequences.

'''

currencies = ['EGP', 'GMD', 'CLP']
base_url = "https://api.exchangerate-api.com/v4/latest/"

for currency_code in currencies:
    # url = base_url + currency_code
    # response = requests.get(url)
    # response = response.json()
    
    url = f'{base_url}{currency_code}'
    response = requests.get(url)
    response = response.json()
    print(f'The exchange rate from {currency_code} to USD is {response["rates"]["USD"]}.')



    '''
    HTTP Request Error Handling
Learn
We were previously able to make successful HTTP requests because we retrieved valid and expected HTTP responses that represented all of our currency exchange rates. There are times, however, when we do not receive a successful response from the server. Checking for these errors is important because it allows us to gracefully handle the error so that the users of our application can be informed of what went wrong in a way that they understand.

When we initiate an HTTP request, we get back an HTTP response. This response contains an attribute, or a specific piece of information or property associated with the response, called status_code that indicates the outcome of the request. Here are a few example status codes:

Code	Status	Description
200	OK	Successful request
201	Created	Successful request, new resource created (occurs with a PUT request)
400	Bad Request	Request syntax or parameters are incorrect
401	Unauthorized	Authentication required or credentials are invalid
404	Not Found	Requested resource does not exist (for example, the endpoint does not exist
500	Internal Server Error	An error occurred on the server side
We can access the response status code by running the following lines of code:

import requests
​
endpoint = 'https://api.exchangerate-api.com/v4/latest/usd'
​
# Make a GET request to the API endpoint
response = requests.get(endpoint)
print(response.status_code)

Explain

Copy
Output
200
We can use if/elif/else statements to check the response and print appropriate messages for each.

import requests
​
endpoint = 'https://api.exchangerate-api.com/v4/latest/usd'
​
# Make a GET request to the API endpoint
response = requests.get(endpoint)
if response.status_code == 200:
    print("Request was successful!")
elif response.status_code == 404:
    print("Endpoint not found. Please check the currency code provided in the endpoint."
else:
    print("Something went wrong.")

Explain

Copy
Let’s practice more with checking response status codes.

Instructions
Your task is to generate URLs dynamically using currency_codes, make requests.get() calls to each, and print relevant messages based on the status code returned.

    '''

currency_codes = ['cad', 'abc']
base_url = "https://api.exchangerate-api.com/v4/latest/"

for currency_code in currency_codes:
    url = f'{base_url}{currency_code}'
    print(url)
    
    response = requests.get(url)
    
    if response.status_code == 200:
        print('Request was successful')
    elif response.status_code == 404:
        print('Endpoint not found!')