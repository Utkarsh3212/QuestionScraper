import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from bs4 import BeautifulSoup
import time

driver =webdriver.Chrome()

heading_class=".truncate.cursor-text"
body_class=".elfjS"
index=1
QDATA_FOLDER="QDATA"

def get_links():
    new_arr=[]
    with open("properPLinks.txt",'r') as f:
        for line in f:
            new_arr.append(line)
    return new_arr

def add_text_to_indexFile(text):
    filePath=os.path.join(QDATA_FOLDER,"index.txt")
    with open(filePath,'a') as f:
        f.write(text+'\n')

def add_link_to_qindexFile(link):
    filePath=os.path.join(QDATA_FOLDER,"qIndex.txt")
    with open(filePath,'a') as f:
        f.write(link)

def add_question_description(fileName,text):
    new_filePath=os.path.join(QDATA_FOLDER,fileName)
    os.makedirs(new_filePath,exist_ok=True)
    new_filePath=os.path.join(new_filePath,fileName+".txt")
    with open(new_filePath,'w',encoding="utf-8",errors="ignore") as f:
        f.write(text)

def explorer(url,ix):
    try:
        driver.get(url)
        WebDriverWait(driver,5).until(EC.presence_of_element_located((By.CSS_SELECTOR,body_class)))
        time.sleep(1)
        heading=driver.find_element(By.CSS_SELECTOR,heading_class)
        body=driver.find_element(By.CSS_SELECTOR,body_class)
        print(heading.text)
        if(heading.text):
            add_link_to_qindexFile(url)
            add_question_description(str(ix),body.text)
            add_text_to_indexFile(heading.text)
        time.sleep(1)
        return True
    except Exception as e:
        print(e)
        return False
    

arr=get_links()

for element in arr:
    done=explorer(element,index)
    if(done):
        index=index+1


driver.quit()