
from urllib.request import urlopen as uReq
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import urllib.request
opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)


my_url = Request('https://www.99acres.com/microsite/pyramid-builders-and-developers-carnations-avalahalli-bangalore/?from_src=LI130877&src=FPLINK', headers={'User-Agent': 'Mozilla/5.0'})
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html,"html.parser")
containers = page_soup.findAll("a",{"class":"cboxElement fancybox-buttons"})
for container in containers:
	img_url = container['href']
	urllib.request.urlretrieve(img_url, img_url.split("/")[-1])