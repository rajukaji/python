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


'''
Extracting Data from Web Pages
Learn
On the previous screen, we looked at some practical web scraping applications and got a taste of how to extract data from a webpage. Now, let's explore the process of extracting data from web pages using Python's requests library and BeautifulSoup.

Web scraping essentially involves two main steps: sending a request to the webpage and parsing its content.

Let's visualize this with an analogy: Imagine you're an archaeologist who wants to study ancient scripts. The process you would follow is similar to web scraping:


Sending a Request: This is like traveling to the archaeological site. You need to reach the location first to start your work. In the context of web scraping, this involves sending an HTTP request to the URL of the webpage you want to access. The server responds to the request by returning the HTML content of the webpage.

Parsing the Content: Once you've reached the archaeological site, you need to carefully dig and find the artifacts (in our case, the scripts). This is similar to parsing the HTML content of the webpage to find the information you need. The Python library BeautifulSoup is designed for this purpose. It creates a parse tree from the HTML content of the webpage that can be used to extract data in a hierarchical and more readable manner.

Let's take a look at the code snippet we used in the previous screen to extract data from the Wikipedia page:

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
In this code, we first send an HTTP request to the URL of the webpage using requests.get(). The server responds to the request and returns the HTML content of the webpage, which we store in the response object.

Next, we use BeautifulSoup to parse the HTML content of the webpage. This creates a BeautifulSoup object (soup) that represents the document as a nested data structure. We can now use this object to extract data from the webpage in a more readable and hierarchical manner.

To find the main table on the webpage, we use the find() method, which returns the first matching element. We pass in the HTML element we're looking for ('table') and a dictionary that describes the attribute(s) the element should have ({'class': 'wikitable'}).

Then, we use the find_all() method to find all row elements ('tr') in the table. This method returns a ResultSet object containing all the matching elements.

Finally, we loop through each row and find all column elements ('td') in each row. We use a list comprehension to get the text from each column and strip any extra whitespace. We then print the columns, which gives us the data from each column in each row of the main table.

Handling Different Data Types While Web Scraping
Web pages can contain various types of data, such as text, numbers, dates, and even images and videos. When we scrape data from a web page, we need to be aware of the data types we are dealing with.

Text: Text is the most common form of data you'll extract from a web page. In BeautifulSoup, you can use the .text or .get_text() methods to extract text from a tag. You can also use the .string attribute to get the exact string within a tag.

Numbers: Numbers are usually represented as text in HTML. After extracting the text, you can convert it to an integer or float using the int() or float() functions.

Dates: Dates can be tricky because they can be in different formats. You might need to use the datetime module to parse and format dates.

Images and Videos: To scrape images or videos, you typically extract the URL of the image or video file rather than the content itself. In BeautifulSoup, you can get the src attribute of an img or video tag to get the URL.

Remember, it's important to inspect the HTML content of the web page to understand the structure and data types before you start scraping.

'''


from requests.exceptions import RequestException, HTTPError

try:
    response = requests.get('https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population')
    response.raise_for_status()
    

except RequestException as e:
    print(f'There was an error: {e}')

except HTTPError as e:
    print(f'There was an error: {e}')
    
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table', {'class': 'wikitable'})

rows = table.find_all('tr')

top_20_countries = rows[2:22]

for row in top_20_countries:
    cols = row.find_all('td')
    
    cols = [col.text.strip() for col in cols]
    print(cols)


# element = soup.find('div', {'id': 'unique_id'})
# this is the way to find any attribute, id or class 

try:
    response = requests.get('https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population')
    response.raise_for_status()
    
except RequestException as e:
    print(f'There was an exception : {e}')
          
except HTTPError as e:
          print(f'There was an exception : {e}')
                
soup = BeautifulSoup(response.text, 'html.parser')
                
table = soup.find('table', {'class': 'wikitable'})

print(table)

'''
In BeautifulSoup, we can use the .select() method to apply 
CSS selectors and extract specific data. 
For example, to select all paragraph elements, we'd write:

paragraphs = soup.select('p')

CSS selectors can be more specific. For instance, to select all elements with a certain class, we use the pattern .class_name. To select elements with a certain ID, we use #id_name.

Let's say we're looking for a book on our bookshelf with the label history. In CSS selector terms, we'd use .history to attract that book. If our book has a unique identifier, book_123, we'd use #book_123 to select it.

Here's how we'd use these selectors in BeautifulSoup:

# Select elements with the class 'history'
history_elements = soup.select('.history')
​
# Select the element with the id 'book_123'
book_123 = soup.select('#book_123')

CSS selectors also support more complex patterns to select elements. For example, we can select all p elements inside div elements using the selector 'div p'.

# Select all `p` elements inside `div` elements
div_paragraphs = soup.select('div p')


With CSS selectors, we can also use modulo operators to select every nth element in a list. Modulo operation finds the remainder after the division of one number by another. In Python, we use the % symbol for modulo operation.

For example, if we have a list of td elements and we want to select every 5th element (which corresponds to the Date column), we can use a loop and the modulo operation as follows:

td_elements = td_elements[13:]  # The first two rows are unstructured, so we start at the 14th element, assuming the 3rd row onwards.
​
# Loop through each 'td' element
for i in range(len(td_elements)):
    # If the index of the 'td' element is 4 (which corresponds to the 'Date' column)
    if i % 7 == 4:
        # Extract the text from the 'td' element and print it
        date = td_elements[i].text
        print(date)

In this code, i % 7 == 4 checks if the remainder of the division of i by 7 is 4. This condition is true for every 4th element in the list (with indices 4, 11, 18, etc.), so these elements are selected.

We use 7 because the structure of our HTML table from which we are scraping data consists of rows with 7 cells each. This pattern suggests that every row represents a distinct set of data points (like country name, population, world percentage, date, etc.) distributed across 7 columns.

'''

try:
    response = requests.get('https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population')
    response.raise_for_status()
    
except RequestException as e:
    print(f'Error raised : {e}')
    
except HTTPError as e:
    print(f'Error raised : {e}')
    
soup = BeautifulSoup(response.text, 'html.parser')

td_elements = soup.select('tr td')[13:]
# select all the td elements inside tr,row )
# selector select

population_list = []

for i in range(len(td_elements)):
    if i % 7 == 2:
#         To select every nth element in a list, you can use the modulo operator (%). For example, if i % n == 0: will select every nth element.
        population = td_elements[i].text
        population_list.append(population)
        
print(population_list[:10])


# Handling Different Data Types in Web Scraping

'''
Continuing our web scraping education, we'll come across various data types on webpages, including strings, numbers, and dates. Similar to categorizing distinct items in a collection, we must process each data type appropriately to effectively organize and understand our findings.

Mastering the handling of different data types is crucial for web scraping, as it ensures that the data we extract is accurate and usable in our subsequent analyses or applications. Let's look at how to manage these data types with confidence.

So far, we've been treating all the data we scrape as strings because that's what the .text attribute of a BeautifulSoup object returns. But what if we want to perform mathematical operations on numeric data? Or what if we want to analyze dates? We need to convert these string representations into appropriate data types.

Handling different data types is crucial in web scraping because it allows us to perform appropriate operations on our data. For instance, we can perform mathematical operations on numeric data, compare dates, or manipulate strings. Without converting our data into the correct types, we would be limited in our ability to analyze and interpret our data.

Let's take a look at our data from the Wikipedia page again:

['[b]','China', '1,411,750,000', '17.5%', '31 Dec 2022', 'Official estimate[4]', '[b]']
['[b]','China', '1,411,750,000', '

Here, 1,411,750,000 is a string representation of a population, 17.5% is a string representation of a percentage, and 31 Dec 2022 is a string representation of a date. To work with these values, we'll need to convert them into the appropriate data types.

For the population, we can remove the commas and convert the string to an integer:

population = '1,411,750,000'
population = int(population.replace(',', ''))
print(population)

1411750000

For the percentage, we can remove the '%' sign and convert the string to a float:

percentage = '17.5%'
percentage = float(percentage.replace('%', ''))
print(percentage)

17.5

For the date, we can use the datetime module to convert the string to a datetime object:

from datetime import datetime
​
date = '31 Dec 2022'
date = datetime.strptime(date, '%d %b %Y')
print(date)
%d is the day, %b is the month abbreviation, and %Y is the year.
 The datetime.strptime() function parses the date string 
 according to the specified format and returns a datetime object.

2022-12-31 00:00:00

Sometimes, we may encounter values that can't be converted into the desired data type. For instance, trying to convert a string with non-numeric characters into an integer will raise a ValueError. To handle such errors, we can use a try-except block.

Let's say we have a population value that's not formatted correctly:

population = '1,411,750,000abc'

If we try to convert this string to an integer, we'll get a ValueError. Here's how we can handle it:

try:
    population = int(population.replace(',', ''))
except ValueError:
    print(f"Could not convert {population} to an integer.")

In this block, the try clause (the code between the try and except keywords) is executed. If no exception occurs, the except clause is skipped. However, if an exception occurs, the rest of the try clause is skipped, and the except clause is executed.

We can apply similar error handling when converting strings to floats or dates. This way, if we encounter any data that can't be converted, our program won't crash - instead, it will handle the error gracefully and move on.

Remember, each data type has its own set of operations and methods. By converting our data into the correct types, we're unlocking the power to manipulate and analyze it meaningfully.

'''

from datetime import datetime

try:
    response = requests.get('https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population')
    response.raise_for_status()
    
except RequestException as e:
    print(f'Error raised : {e}')

except HTTPError as e:
    print(f'Error raised : {e}')
    
soup = BeautifulSoup(response.text, 'html.parser')


td_elements = soup.select('tr td')[13:]
# elements from only the 3rd row on wards from 13th index

for i in range(len(td_elements), 30):
    try:
        if i % 7 == 2:
    #         Population column
            population = td_elements[i].text
            integer = population.replace(',', '')
            print(integer)

        if i%7 == 3:
    #         world column
            world = td_elements[i].text
            percentage = world.replace('%', '')
            print(percentage)

        if i%7 == 4:
    #         if the column is 4th, ie, 
    # Source (official or form the United Nations) column
    # date column
            source = td_elements[i].text
            date = datetime.strptime(source, '%d %b %Y')
    #         day, month, year format
            print(date)
        
    except ValueError as e:
        print(f'Raised ValueError : {e}')

'''
Storing and Structuring Scraped Data
Learn
After successfully scraping our data and handling different data types, the next step is to structure and store it for further analysis. The process of structuring and storing data is much like organizing a library. Imagine each piece of information we scraped is a book. We can't just leave our books in a pile; we need to arrange them on shelves and categorize them so that we can easily find what we're looking for. In the same way, we need to structure our scraped data into a suitable format and store it for easy access and analysis.

One common way to structure web-scraped data is by using pandas DataFrames. A DataFrame is a two-dimensional, size-mutable, and heterogeneous tabular data structure with labeled axes (rows and columns). Think of it as a spreadsheet, SQL table, or dictionary of Series objects. We can easily convert our scraped data into a DataFrame and then perform all sorts of data analysis tasks.

Let's say we've scraped the following data from our Wikipedia page:

data = [['China', '1,411,750,000', '17.5%', '31 Dec 2022', 'Official estimate[4]', '[b]'], ['India', '1,392,329,000', '17.3%', '1 Mar 2023', 'Official projection[5]', '[c]'], ['United States', '335,495,000', '4.2%', '11 Oct 2023', 'National population clock[7]', '[d]']]

Explain

Copy
We can convert this data into a DataFrame like this:

import pandas as pd
​
# Define the column names
columns = ['Country/Dependency', 'Population', '% of World', 'Date', 'Source', 'Notes']
​
# Create a DataFrame from the data
df = pd.DataFrame(data, columns=columns)
​
print(df)

Explain

Copy
Country/Dependency     Population % of World          Date                          Source Notes
0              China  1,411,750,000      17.5%   31 Dec 2022              Official estimate[4]   [b]
1              India  1,392,329,000      17.3%    1 Mar 2023             Official projection[5]   [c]
2      United States    335,495,000       4.2%  11 Oct 2023   National population clock[7]   [d]

Explain

Copy
Once our data is in a DataFrame, we have a wide range of tools at our disposal to manipulate, analyze, and visualize it. We can filter rows, calculate statistics, create plots, and much more.

After structuring our data, we can store it in a file for later use. One common way to do this is by writing the data to a CSV file. Here's how we can do it:

# Write the DataFrame to a CSV file
df.to_csv('population_data.csv', index=False)

Explain

Copy
The to_csv() function writes the DataFrame to a CSV file. The index=False argument prevents pandas from writing row indices. Now, we have a CSV file named 'population_data.csv' that we can open anytime without scraping the web page again.

Storing our data in a file not only allows us to access it later but also enables us to share our data with others. Furthermore, it allows us to work with large amounts of data that might not fit into memory.
'''

