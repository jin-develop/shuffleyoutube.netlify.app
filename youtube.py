import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome('C:\\Users\\nick0\\Desktop\\chromedriver')
import time
import random

youtube_link = "https://www.youtube.com/watch?v=Qxf9pb-ki78"


driver.get(youtube_link)
for i in range(2):
    driver.find_element_by_tag_name('body').send_keys(Keys.END)
    driver.implicitly_wait(3)
    time.sleep(1)

req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

lines = soup.select('div.ytd-item-section-renderer')

comments = lines.find_all("yt-formatted-string.style-scope")

for comment in comments.text:
    print(comment)

# # URL을 읽어서 HTML를 받아오고,
# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# data = requests.get(youtube_link ,headers=headers)

# # HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup = BeautifulSoup(data.text, 'html.parser')

# # select를 이용해서, tr들을 불러오기
        
# contents = soup.find("id=contents")

# comments = contents.find("id=content-text")

# for line in comments:
#     if a_href is not None:  
#         print(line)