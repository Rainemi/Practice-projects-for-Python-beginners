import requests
import datetime
import pandas as pd
from requests_html import HTML

now = datetime.datetime.now()
year = now.year


url = 'https://www.boxofficemojo.com/year/world/'
def url_to_text(url,filename="box.html",save=False):
    r = requests.get(url)
    if r.status_code == 200:
        html_text = r.text
        if save :
            with open(f"box-{year}.html" , 'w',encoding="utf-8") as f:
                f.write(html_text)
            return html_text  
        return''
        

html_text = url_to_text(url,save=True)
r_html = HTML(html=html_text)
table_class =".imdb-scroll-table"
r_table = r_html.find(table_class)


table_data = []
header_names = []
if len(r_table) == 1:
    parsed_table = r_table[0]
    rows = parsed_table.find('tr')
    header_cols = header_row.find('th')
    header_row = rows[0]
    header_names = [x.text for x in header_cols]
    #print(p_table)
    for row in rows[1:]:
        #print(row.text)
        cols = row.find('td')
        row_data = []
        for i, col in enumerate(cols):
            #print(i,col.text,'\n\n')
            row_data.append(col.text)
        table_data.append(row_data)
print(header_names)
print(table_data)
        
#df = pd.DataFrame(table_data,columns=header_names)
#df.to_csv('cfe.csv',index=False)   
    



