import requests
from bs4 import BeautifulSoup
import pandas as pd


for i in range(1,3):
    url = f"https://www.susamusa.com/collections/shop-all?page={i}"
    headers={
        'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }
    resp = requests.get(url, headers=headers)
    html = BeautifulSoup(resp.text, 'html.parser')
    product= html.find('ul', id='product-grid')

    product_link = []
    for prod in product.find_all('li'):
        link = prod.find('a', href=True)
        product_link.append('https://www.susamusa.com' + link['href'])

    sasamusa_list = []
    for link in product_link:
        response = requests.get(link, headers=headers)
        html2 = BeautifulSoup(response.content, 'html.parser')

        name = html2.find('div', class_='product__title')
        dress_name = name.find('h1').text
        price = html2.find('span', class_='price-item price-item--regular').text.strip()
        description = html2.find('div', class_='product__description rte quick-add-hidden small-hide')
        for desc in description.find_all('span'):
            description_text = desc.text
        photo_link_list = []
        photo_url = html2.find('ul', id='Slider-Gallery-template--20217327517999__main')
        if photo_url is None:
            continue
        else:
            for pht in photo_url.find_all('li'):
                photo_link = pht.find('img')['src']
                photo_link_list.append(photo_link)
        
        sasamusa ={
            'dress_name': dress_name,
            'price':price,
            'description':description_text,
            'photo_urls': photo_link_list
        }


        sasamusa_list.append(sasamusa)
        #print(len(sasamusa_list))

sasamusa_df = pd.DataFrame(sasamusa_list)
sasamusa_df.to_csv("sasamusa.csv")
#print(sasamusa_df.head())