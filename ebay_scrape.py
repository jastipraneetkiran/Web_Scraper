from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 

my_url ="https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=cammera&_sacat=0"
#opening up connection,grabbing the page
uC = uReq(my_url)
page_html = uC.read()
uC.close()
page_soup = soup(page_html,"html.parser")
new_tag = page_soup.findAll("div",{"class":"s-item__wrapper clearfix"})

filename = "products.csv"
f = open(filename,"w")
headers = " name_product,price_INR,shipping_from\n"
f.write(headers)

for title_name in new_tag:
	brand = title_name.findAll("a",{"class":"s-item__link"})
	name_p = brand[0].text
	#print(name_p)
	price_rs = title_name.findAll("div",{"class":"s-item__detail s-item__detail--primary"})
	price = price_rs[0].text
	#print(price)
	location = title_name.findAll("span",{"class":"s-item__location s-item__itemLocation"})
	area = location[0].text
	print(name_p)
	print(price)
	print(area)
	
	f.write(str(name_p) + ","  + str(price) + "," + str(area)  + "\n")

f.close()
