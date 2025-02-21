'''
Introduction to Web Scraping
Learn
Welcome to this lesson on web scraping in Python. In this lesson, we'll learn all about the world of web scraping.

Imagine you're at a library, looking for books on a specific topic. You could go through every bookshelf, one by one, checking each book to see if it's relevant. That would be time-consuming, right? Now, what if you had a robot that could do this tedious task for you, quickly scanning the entire library and returning a list of books that match your interests? That's essentially what web scraping is!


Web scraping is a way to automate the process of collecting data from websites. It's like sending a robot to a web page, instructing it to read the page's content, and then asking it to bring back the specific pieces of information you need.

Web scraping is particularly useful when the data you need is not readily accessible through an API. For instance, as we'll see on the next screen, we'll be able to retrieve the List of countries and dependencies by population Wikipedia page that doesn't have a corresponding API. So, in this lesson, we'll learn how to extract this data using web scraping techniques.

The robots.txt file is a text file that webmasters create to instruct web robots (typically search engine robots) how to crawl pages on their website. You can usually find this file by appending /robots.txt to the base URL of a website. For example, the robots.txt file for Wikipedia is at https://en.wikipedia.org/robots.txt. Always check this file before scraping a website to ensure you're not violating any rules.

While web scraping is a powerful tool, it's important to use it responsibly. Some websites may have rules about what data you can scrape and how often you can do it, usually found in theirrobots.txt file or Terms of Service. Ignoring these rules could lead to being blocked from the website or even legal trouble. Always make sure to respect the website's rules and the privacy of any individuals whose data you might be scraping.

In this lesson, we'll be using Python's requests library to send HTTP requests and the bs4 (BeautifulSoup) library to parse web page HTML content. The requests library allows us to send HTTP requests using Python, while BeautifulSoup helps us parse a web page's HTML content to find the data we need.

By the end of this lesson, you'll be able to extract data from web pages for your analysis, handle common errors and exceptions in web scraping, understand the role of HTML elements, IDs, and classes in web scraping, and apply CSS selectors for targeted data extraction.
'''

'''
 Practical Applications of Web Scraping
Learn
On the previous screen, we introduced the concept of web scraping and its ethical considerations. Now, let's explore some real-world applications of web scraping.

Web scraping can be a powerful tool for a variety of applications across different domains:

Data Journalism: Reporters often need to analyze large amounts of data to uncover stories. Web scraping allows journalists to collect data from various sources for their investigative work.

E-commerce: Retailers and e-commerce companies use web scraping to monitor competitors' prices and product reviews. This information can help them adjust their strategies and improve their products.

Recruitment: HR professionals use web scraping to gather data on potential candidates from professional networking sites and job boards.

Social Media Analysis: Web scraping can gather data from social media platforms to understand customer sentiment and trends.

SEO Monitoring: Digital marketers use web scraping to track website performance, monitor SEO rankings, and gather intelligence on competitors.

Research: Academics and researchers use web scraping to collect data for research in fields like linguistics, data science, and sociology.

Let's apply what we've learned to a practical example. We'll continue with our scenario at EcoData Inc., where we've identified valuable data on the List of countries and dependencies by population Wikipedia page. To extract this data, we'll use the BeautifulSoup library to collect population data from a Wikipedia page. This can help us analyze demographic trends, which is a common application of web scraping in data science.

Here's a snippet of code that demonstrates how to extract the main table from the Wikipedia page:

# Import necessary libraries
import requests
from bs4 import BeautifulSoup
​
# Send an HTTP request to the URL of the webpage
response = requests.get('https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population')
​
# Parse the content of the request
soup = BeautifulSoup(response.text, 'html.parser')
​
# Find the main table using the class attribute
table = soup.find('table', {'class': 'wikitable'})
​
# Find all rows in the table
rows = table.find_all('tr')
​
# Loop through each row
for row in rows:
    # Find all columns in each row
    cols = row.find_all('td')
    # Get the text from each column
    cols = [col.text.strip() for col in cols]
    # Print the columns
    print(cols)

Explain

Copy
In this code, we're using the BeautifulSoup library to parse the HTML content of the webpage. BeautifulSoup allows us to navigate and search through the HTML and extract the data we need. This code will print the data from each column in each row of the main table. The data includes the rank, country/dependency, population, % of world population, source, and explanatory notes. For example, the output for the first few rows would look like this:

[]
['World', '8,064,922,000', '100%', '11 Oct 2023', 'UN projection[3]', '']
['China', '1,411,750,000', '17.5%', '31 Dec 2022', 'Official estimate[4]', '[b]']
['India', '1,392,329,000', '17.3%', '1 Mar 2023', 'Official projection[5]', '[c]']
['United States', '335,495,000', '4.2%', '11 Oct 2023', 'National population clock[7]', '[d]']
[]
['World', '8,064,922,000', '100%', '11 Oct 2023', 'UN projection[3]', '']
['China', '1,411,750,000', '17.5%', '31 Dec 2022', 'Official estimate[4]', '[b]']
['India', '1,392,329,000', '17.3%', '1 Mar 2023', 'Official projection[5]', '[c]']
['United States', '335,495,000', '4.2%', '11 Oct 2023', 'National population clock[7]', '[d]']
'''


import requests
from bs4 import BeautifulSoup

'''
Write a function named extract_data that takes a URL as an argument
and returns a list of lists containing the data from the main table
on the page. Each inner list should contain the rank, 
country/dependency, population, % of world population, source,
and explanatory notes for a single row of the table.
'''

def extract_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        
    except requests.exception.HTTPError as err:
        print(err)
        return
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    table = soup.find('table', {'class':'wikitable'})
    
    rows = table.find_all('tr')
    
    table = []
    
    for row in rows:
        cols = row.find_all('td')
#         find all columns in each rows
        cols = [col.text.strip() for col in cols]
    
        table.append(cols)
    
    return table
    
    
    
    
population_data = extract_data('https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population')

print(population_data[:5])