# access protected endpoint

import requests
import base64


url = 'https://api-server.dataquest.io/private/historical_data'

response = requests.get(url)

print(response.status_code)


'''
Environment Variable
Learn
On the previous screen, we explored implementing Basic Authentication for secure API access with the World Development Indicators API. We learned that, in Basic Authentication, credentials are encoded and sent in the request headers. This method is more secure compared to directly using API keys in the code, but it still poses a risk if the credentials are exposed.

So, how do we protect our credentials in a Basic Authentication scenario? The answer lies in using environment variables.

An environment variable is a dynamic "object" containing a value that can be used by one or more software programs in an operating system. You can think of them as secret lockers in your computer where you can keep important information.

In Python, we use the os module to set and get environment variables. Here's how you can set an environment variable:

import os
​
os.environ['USERNAME'] = 'your-username'
os.environ['PASSWORD'] = 'your-password'

Explain

Copy
And to retrieve these credentials in your script:

username = os.environ.get('USERNAME')
password = os.environ.get('PASSWORD')

Explain

Copy
Alternatively, storing your Basic Authentication credentials in a separate configuration file is another secure approach. This is useful when managing multiple credentials or configurations. Your Python script can read these credentials as needed, keeping them out of your main codebase.

For instance, your credentials.json file might look like this:

{
    "username": "your-username",
    "password": "your-password"
}

Explain

Copy
And in your Python script, you could use:

import json
​
# Reading credentials from a file
with open('credentials.json', 'r') as file:
    credentials = json.load(file)
    username = credentials['username']
    password = credentials['password']

Explain

Copy
Using these methods, your Basic Authentication credentials are kept secure, reducing the risk of accidental exposure and enhancing the overall security of your application.

Let's consider some risks associated with exposed credentials in Basic Authentication:

Unauthorized Access: Exposed credentials can lead to unauthorized access to APIs, potentially leading to data breaches.

Data Manipulation: If someone else gets hold of your credentials, they could manipulate the data you are accessing or modifying through the API.

Service Abuse: Misuse of your credentials could result in the abuse of the API services, affecting your application's functionality and possibly incurring additional costs.

Reputation Damage: Misuse of credentials under your name could negatively impact your or your organization's reputation.

Securing your credentials with Basic Authentication and environment variables is crucial, not just for protecting your data but also for preventing potential misuse that could have serious consequences. Always handle your credentials with utmost care.

'''




url = 'https://api-server.dataquest.io/private/economic_data/historical_data'

username = 'incorrect'
password = 'incorrect'

encoded_credentials = base64.b64encode(f'{username}:{password}'.encode()).decode()

headers = {
    'Authorization': f'Basic {encoded_credentials}'
}

try:
    response = requests.get(url, headers = headers)
    response.raise_for_status()
    
except requests.exceptions.HTTPError as err:
    print(err)


'''
 Timing API Requests
Learn
On the previous screen, we introduced the concept of rate limits in API usage. Now, we'll learn how to manage our requests to stay within these limits.

API rate limits control the maximum number of requests that can be made to an API within a specific timeframe. If this limit is exceeded, the API will deny further requests, similar to facing penalties for not adhering to set rules.

To ensure we don't exceed the rate limit, we need to manage the timing of our requests effectively. One way to do this is by using the time.sleep() function in Python. This function pauses the execution of the program for a specified number of seconds.

Let's say we're working with an API that has a rate limit of 100 requests per minute. To stay within this limit, we could add a delay of 0.6 seconds (60 seconds / 100) between each request. Here's an example:

import requests
import time
​
url = 'https://api-server.dataquest.io/private/economic_data/footnotes'
username = 'dq'
password = 'test'
encoded_credentials = base64.b64encode(f"{username}:{password}".encode()).decode()
headers = {'Authorization': f'Basic {encoded_credentials}'}
​
for i in range(100):
    response = requests.get(url, headers=headers)
    print(response.status_code)
    time.sleep(0.6)

Explain

Copy
In the code above, we send 100 requests to the API with a delay of 0.6 seconds between each request. This ensures that we don't exceed the rate limit of 100 requests per hour.

Timing our requests in this way is especially crucial when we're dealing with large-scale data retrieval tasks. For example, if we need to retrieve data for thousands of indicators from the World Development Indicators API, we'll likely need to make thousands of requests. By adding a delay between each request, we can ensure that we don't exceed the API's rate limit.

Now, let's consider some real-world scenarios where managing rate limits is crucial:

Social Media Analysis: If you're building a sentiment analysis tool that uses a social media company's API to gather posts, you'll be making a large number of requests. Most companies impose a rate limit, and if you send too many requests too quickly, your access could be temporarily suspended.

Web Scraping: If you're scraping a website for data, you'll likely be making many requests to the site's server. If you send these requests too quickly, the server might interpret it as a denial-of-service attack and block your IP address.

Financial Data Analysis: If you're using an API to gather real-time stock market data for analysis, you'll need to manage your requests to avoid exceeding the API's rate limit. Exceeding the limit could result in your access being suspended, which would disrupt your data analysis.

In the context of LLMs, managing rate limits is similar to efficiently handling resource-intensive tasks such as generating responses or processing large datasets. Just as APIs impose rate limits to maintain server stability and equitable access, LLMs need to balance their computational load to provide timely and effective responses. This might involve pacing the processing of complex language tasks or managing the frequency of interaction to prevent overloading the system, similar to using time.sleep() in APIs to avoid exceeding rate limits. Effective management ensures that the LLM remains responsive and capable of handling requests without compromising performance.

In these situations, and many others, it's important to manage the timing of your API requests to stay within the rate limits. Now let's practice.
'''

'''
Dealing with Rate Limit
Learn
In our data retrieval journey, we've learned to authenticate our requests using Basic Authentication, time our requests to avoid exceeding rate limits, and handle various potential errors. But what if we still hit the rate limit? Does this mean our data retrieval process has to stop? Not necessarily!

When we exceed the rate limit, the API server responds with a 429 Too Many Requests status code. Instead of letting this error halt our data retrieval, we can catch this error, pause our script temporarily, and then continue with our requests. This approach respects the API's rate limit while ensuring our data retrieval continues.

Here's how we can handle rate limit situations in Python, especially when using Basic Authentication:

import requests
import time
​
url = 'https://api-server.dataquest.io/private/economic_data/footness'
​
username = 'dq'
password = 'test'
encoded_credentials = base64.b64encode(f"{username}:{password}".encode()).decode()
headers = {'Authorization': f'Basic {encoded_credentials}'}
​
for i in range(101): # Sending 101 requests to demonstrate the rate limit error
    response = requests.get(url, headers=headers)
    if response.status_code == 429:  # If we hit the rate limit
        print("Rate limit exceeded. Waiting for 60 seconds before next request.")
        time.sleep(60)  # Pause the script for 60 seconds
    else:
        print(response.status_code)
    time.sleep(0.6)  # Pause for 0.6 seconds between requests to respect the rate limit

Explain

Copy
In the example above, we're using a for loop to send 101 requests to the API. Notice that we're pausing for 0.6 seconds between each request to respect the API's rate limit of 100 requests per minute. However, we're sending 101 requests in this example to intentionally exceed the rate limit and demonstrate how we can handle the 429 Too Many Requests status code.

When we hit the rate limit, the server responds with a 429 status code. We catch this status code using an if condition and pause our script for 60 seconds before continuing with our requests. This pause allows us to stay within the API's rate limit while ensuring the continuity of our data retrieval process.

In real-world data retrieval tasks, handling rate limit errors effectively is crucial to ensure the continuity of our data retrieval process and respect the API's usage policies.

In LLMs, handling situations analogous to exceeding API rate limits involves strategic pauses or shifts in processing. For instance, if an LLM encounters a task that strains its computational limits, it may need to manage this load intelligently, much like how an API handling script pauses when a 429 Too Many Requests status code is received. This could involve temporarily stopping the processing of new requests or redistributing computational resources. This approach ensures that the system remains functional and effective, respecting its operational constraints while continuing to process and respond to tasks. Such strategies are crucial for maintaining the efficiency and reliability of both APIs and advanced AI systems.

'''

'''
 Understanding API Key Authentication
Learn
While we've been focusing on basic authentication for the our API, which uses usernames and passwords, let's explore the concept of API key authentication for educational purposes. It's important to note that our API server currently only supports basic authentication, and the following discussion about API keys is for learning purposes only, as our API does not support this method of authentication.

In a typical scenario where an API supports API key authentication, the process would involve registering or signing up on the platform hosting the API. After registration, you would usually receive an API key, often accessible in your account settings or a dedicated API section. This key is then used to authenticate your requests to the API.


For illustrative purposes, let's consider a hypothetical example using Python's requests library, assuming that an API supports API key authentication.

import requests
​
# Hypothetical URL for an API that supports API key authentication
url = 'https://api.example.com/data'
headers = {'Authorization': 'Bearer YOUR_API_KEY'}
​
# Making a request with the API key
response = requests.get(url, headers=headers)
print(response.json())

Explain

Copy
In this example, YOUR_API_KEY would be replaced with the actual API key provided to you. This key, included in the request headers, would authenticate your access to the API.

Remember, this is a hypothetical scenario to help understand how API key authentication works in general. For actual interactions with the DataQuest API, you'll continue to use basic authentication with your username and password. Understanding different authentication methods is crucial as it broadens your knowledge and skills in working with various APIs.

'''