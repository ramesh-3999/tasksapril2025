import requests
import pandas
from bs4 import BeautifulSoup

response=requests.get("https://www.meesho.com/sports-shoes-men/pl/3kj")
#print(response)

soup=BeautifulSoup(response.content,'html.parser')
names=soup.find_all('div',class_="NewProductCardstyled__ProductHeaderWrapper-sc-6y2tys-32 knWeEt")
#print(names)
# print(soup)
name=[]
for i in names[1:10]:
    d= i.get_text()
    name.append(d)
#print(name)
price=[]
prices=soup.find_all('h5',class_='sc-eDvSVe dwCrSh')
#print(prices)

for i in prices[1:10]:
    d=i.get_text().replace('₹','')
    price.append(d)
#print(price)
# price.remove('₹')
# print(price)
ratings=soup.find_all('span',class_='sc-eDvSVe laVOtN')
#print(ratings)
rating=[]
for i in ratings[1:10]:
    d=i.get_text()
    rating.append(d)
#print(rating)    

men_shoes=pandas.DataFrame()
#print(men_shoes)
men_shoes['Name']=name
men_shoes['Price']=price
men_shoes['Rating']=rating
#print(men_shoes)
men_shoes.to_csv('Mens_sports_shoes.csv',index=False)
print("📃 File saved Successfully!")