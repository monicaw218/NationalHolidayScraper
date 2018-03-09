
# coding: utf-8

# In[108]:

import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime


# In[109]:

this_month = datetime.today().strftime("%B")
this_day = datetime.today().day
URL = 'https://nationaldaycalendar.com/' + this_month.lower()
x = requests.get(URL)
soup = bs(x.text, 'html.parser')


# In[110]:

blurb_container = soup.body.findAll('div', {'class': 'et_pb_blurb_container'})
current_header = this_month + ' ' + str(this_day)
relevant_section = [line for line in blurb_container if current_header in line.find('h4').text]
print(current_header + ' is:')
for section in relevant_section[0].findAll('li'):
    print(section.text)
input()

