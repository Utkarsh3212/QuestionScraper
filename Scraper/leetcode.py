from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from bs4 import BeautifulSoup
import time

page_url ="https://leetcode.com/problemset/?page="

driver =webdriver.Firefox()

def get_a_tags(url):
    driver.get(url)
    time.sleep(7)
    links=driver.find_elements(By.TAG_NAME,"a")
    pattern ="problems"
    ans=[]
    for i in links:
        try:
            if pattern in i.get_attribute("href"):
                ans.append(i.get_attribute("href"))
        except:
            pass
    ans=list(set(ans))
    return ans

final_list=[]

for i in range(1,63):
    final_list+=get_a_tags(page_url+str(i))

final_list=list(set(final_list))

with open('pLinks.txt','w') as f:
    for i in final_list:
        f.write(i+'\n')

print(len(final_list))

driver.quit()