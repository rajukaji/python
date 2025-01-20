# connecting to the database

'''
To query an SQLite database from Python, we first need to establish a
 connection to the database using the sqlite3 library. The sqlite3 library provides a 
 convenient way to interact with SQLite databases in Python, allowing us to execute SQL 
 queries, retrieve data, and manage transactions.

We'll first connect to the database with the code shown below.

import sqlite3
conn = sqlite3.connect('example.db')
conn.close()

In the code above, we first import the sqlite3 library. We then create a connection object by 
calling the connect() method and passing in the name of the database file example.db. This 
creates a new connection to the database file. Lastly, we close the connection by calling 
the close() method on the connection object. It's important to always close the connection 
when we're done working with the database to avoid data corruption or other issues.

Note that while we'll be working with an SQLite database in this lesson, the processes and
 much of the syntax will apply when using other database connections.
'''
import sqlite3

# Establish a connection to the database
conn = sqlite3.connect('world_population.db')
# conn.close() at the end


'''
Once we've established a connection to a SQLite database from Python, we can execute SQL queries on the database using pandas read_sql_query() method. The read_sql_query() method allows us to execute SQL queries and retrieve the results directly into a pandas DataFrame object.

Here's an example of how to execute a SELECT query on an SQLite database from Python using pandas:

import pandas as pd
import sqlite3
​
# Establish a connection to the database
conn = sqlite3.connect('world_population.db')
​
# Execute a SELECT query and read results into a DataFrame
query = "SELECT * FROM population;"
results = pd.read_sql_query(query, conn)

Explain

Copy
The code above connects to the world_population.db database, executes a SELECT query that retrieves all columns for the first ten rows and reads the results into a pandas dataframe. While SQLite doesn't require adding a semi-colon to the end of a query, it's considered best practice. Note that the read_sql_query() requires two arguments: the query and the connection variable.

Now let's print the results and close the connection.

#Print the results
print(results)
​
#Close the database connection
conn.close()


Now it's your turn to practice executing SQL queries on the world_population.db database from Python using the pandas read_sql_query() method.
'''
import pandas as pd

conn = sqlite3.connect('world_population.db')

query = 'SELECT CountryName, Population FROM population WHERE Year = 2020 LIMIT 10;'

results = pd.read_sql_query(query, conn)

print(results)

conn.close()

"""
Now that we know how to connect to an SQLite database from Python, 
execute SQL queries, and retrieve data, we can revisit our original
 task to create a column chart of the population by year for your country.
   Let's write a query to look at the data we'll plot.

We can use multiline strings to make our code more readable when writing
 longer queries. Multiline strings are strings that span multiple 
 lines and are enclosed in triple quotes (''' or """ '''). 
Using multiline strings allows us to write SQL queries with 
line breaks and indentation, making our code easier to read and understand.

Here's an example of how to use a multiline string to write an SQL query:
'''

# Define the SQL query as a multiline string
query = '''
    SELECT *
      FROM mytable
     WHERE mycolumn = 'myvalue';
'''

import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('world_population.db')

# Write a SELECT query
query = """
    SELECT CountryName, Year, Population 
      FROM population 
     WHERE CountryName = 'United States of America';
     """

# Execute the query
results = pd.read_sql_query(query,conn)

# Print the results
print(results.head(10))

# Close the database connection
conn.close()

import matplotlib.pyplot as plt

# Connect to the SQLite database
conn = sqlite3.connect('world_population.db')

# Execute a SELECT query
query = """
   SELECT Year, Population 
     FROM population 
    WHERE CountryName = 'United States of America';
    """

# Retrieve the results of the query as a pandas dataframe
data = pd.read_sql_query(query, conn)

# Create a column chart of the population data for the country by year
plt.bar(data['Year'], data['Population'])
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('Population of the United States of America by Year')

# Show the plot
plt.show()

# Close the database connection
conn.close()

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect('world_population.db')

# Write a query to select the change in population by region and subregion from 2010-2020
query = """
SELECT region, subregion, sum(PopChange) as TotalPopChange
  FROM population p
  JOIN country_mapping c ON p.CountryCode = c.CountryCode
 WHERE Year between 2010 and 2020
 GROUP BY region, subregion
 ORDER BY TotalPopChange DESC
 LIMIT 10;
"""

# Read the query results into a pandas dataframe
df = pd.read_sql_query(query, conn)

# Close the database connection
conn.close()

# Create a horizontal bar chart to visualize the results
plt.barh(df['SubRegion'], df['TotalPopChange'])
plt.title('Top 10 Subregions by Population Change from 2010 to 2020')
plt.xlabel('Population Change')
plt.ylabel('Subregion')
plt.show()