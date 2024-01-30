import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
response = requests.get(url, headers=headers)
html_content = response.content
soup = BeautifulSoup(html_content, "html.parser")
movies = soup.find_all("div", class_="ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-1e00898e-9 jQixeG cli-title")
for x in movies:
    print(x.h3.text)