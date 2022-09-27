import requests
import datetime
from requests_html import HTML

now = datetime.datetime.now()
year = now.year


url = 'https://www.boxofficemojo.com/year/world/'
def url_to_file(url,filename="box.html",save=False):
    r = requests.get(url)
    if r.status_code == 200:
        html_text = r.text
        if save:
            with open(f"box-{year}.html" , 'w',encoding="utf-8") as f:
                html_text = f.write(html_text)
            return html_text
        return""
        
    
html_text = url_to_file(url)
r_html = HTML(html=html_text)
r_html.find('a')


