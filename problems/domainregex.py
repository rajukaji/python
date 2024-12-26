import pandas as pd
import re

test_urls = pd.Series([
 'https://www.amazon.com/Technology-Ventures-Enterprise-Thomas-Byers/dp/0073523429',
 'http://www.interactivedynamicvideo.com/',
 'http://www.nytimes.com/2007/11/07/movies/07stein.html?_r=0',
 'http://evonomics.com/advertising-cannot-maintain-internet-heres-solution/',
 'HTTPS://github.com/keppel/pinn',
 'Http://phys.org/news/2015-09-scale-solar-youve.html',
 'https://iot.seeed.cc',
 'http://www.bfilipek.com/2016/04/custom-deleters-for-c-smart-pointers.html',
 'http://beta.crowdfireapp.com/?beta=agnipath',
 'https://www.valid.ly?param',
 'http://css-cursor.techstream.org'
])


# pattern = r'https?://(\b\w+-?\w+?\b)?.(\w+)?.?[^/](\w+)?'

pattern = r'https?://([\w\-\.]+)'
# pattern = r'https?://(w{3}?\w+.\w+.?\w+)'
# [https?://] [www.] [amazon] [.com] [/Technology-Ventures-Enterprise-Thomas-Byers/dp/0073523429]
# [\w\-\.]+ it means that it can have any word character, hyphen or dot
# + means that it can have one or more of the characters in the square brackets
# when there is nothing to match or after /, it will stop matching

test_urls_clean = test_urls.str.extract(pattern, expand=False, flags=re.I)

print(test_urls_clean)

'''
Use a regular expression to extract the domains from the url column of the hn dataframe. Assign the result to domains.
Note that passing the cases in test_urls does not guarantee passing all the cases in the url column.

'''

# pattern = r'https?://[(www)(\w+)]?(.)(\w+)(.)?(\w+)?/'
# pattern = r'https?://(w{3}?\w+.\w+.?\w+)'

# domains = hn['url'].str.extract(pat= pattern, expand=False, flags=re.I)


# top_domains = domains.value_counts().head()