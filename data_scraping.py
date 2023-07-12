from bs4 import BeautifulSoup
import requests
import openpyxl

def scrap_data(url,worksheet):
    
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"html.parser")  
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
            
                 
        # create row in worksheet
        row=[product_name,product__subname,messaging,link,product_price,colors]
        
        #append row in worksheet
        worksheet.append(row)

def scrap_womes_shoes_data():
     
    # for setting workbook
    
    workbook=openpyxl.Workbook()
    worksheet=workbook.active 
    
    headers=['Product Name','product Subname','messaging',"link","price","available colors"]
    
    worksheet.append(headers)
    
    url="https://www.nike.com/w/womens-shoes-5e1x6zy7ok"
    scrap_data(url,worksheet)
    workbook.save('Nike Women Shoes Data.xlsx')
    
scrap_womes_shoes_data()
    