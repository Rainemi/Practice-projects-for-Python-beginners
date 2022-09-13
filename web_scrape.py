

import requests
import json
import datetime

now = datetime.datetime.now
year = datetime.datetime.year

current_file_name = 'baby.html'
def url_to_file(url = '',filename = 'baby.html'):
    r = requests.get(url)
    if r.status_code == 200:
        html_text = r.text
        with open(filename,'w',encoding='utf=8') as f:
            f.write(html_text)
        return html_text
    
request_url = 'https://www.boxofficemojo.com/year/world/'
full_text = url_to_file(url=request_url)
'''
json_str = json.dumps(r.json())

with open(filename, 'a') as f:
    f.write(json_str)

with open(filename , 'a') as f:
    f.write(r.text)
'''
        
    

    
    
