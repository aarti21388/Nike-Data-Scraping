from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

data=[]

def scrap_data(url,driver):
    
    #response=requests.get(url)
    driver.get(url)
    #wait until content load 
    wait=WebDriverWait(driver,10)
    element=wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"#skip-to-products > div.product-card")))
    soup=BeautifulSoup(driver.page_source,"html.parser")
    shoes=soup.select("#skip-to-products > div.product-card")
    
    for shoe in shoes:
        product_name=shoe.find("div",class_="product-card__title").text.strip()
        product__subname=shoe.find("div",class_="product-card__subtitle").text.strip()
        messaging=shoe.find("div",class_="product-card__messaging")
        link=shoe.find("a",class_="product-card__link-overlay")["href"]
        product_price=shoe.find("div",class_="product-card__price-wrapper").text.strip()
        colors=shoe.find("div",class_="product-card__product-count")
        
        if messaging is None:
            messaging =None
        else:
            messaging=messaging.text.strip()
            
        if colors is None:
            colors=None
        else:
            colors=shoe.text.strip()
            
        data.append({
            'Product Name':product_name,
            'product Subname':product__subname,
            'messaging' : messaging ,
            "Link":link,"Price":product_price,'Available Colors':colors})
                
        
def scrap_womes_shoes_data():
    #set up the selenium webdriver for asynch data
    webdriver_service=Service("C:\\Drivers\\chromedriver.exe")
    driver=webdriver.Chrome(service=webdriver_service)
    
    
    url="https://www.nike.com/w/womens-shoes-5e1x6zy7ok"
    scrap_data(url,driver)
    df=pd.DataFrame(data)
    df.to_excel('Nike Women Shoes Data Async.xlsx',index=False)
    driver.quit()

scrap_womes_shoes_data()
    