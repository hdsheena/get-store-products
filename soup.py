from bs4 import BeautifulSoup
from urllib2 import urlopen
from time import sleep # be nice
 
BASE_URL = "http://www.anipet.com/"
 
def make_soup(url):
    html = urlopen(url).read()
    return BeautifulSoup(html, "lxml")

def find_info_on_product(product_url):
    soup = make_soup(product_url)
    #print soup.prettify
    upcs = soup.find_all(id="upc")
    upc_list = []
    for upc in upcs:
        upc_num = upc.text
        upc_list.append(upc.text)

    return upc_list

def find_product_links(url):
    urls = []
    soup = make_soup(url)
    products = soup.find_all(class_="prod-hdr")
    for product in products:
        a_sections = product.find_all('a')
        for a_section in a_sections:
            #urls.append(a_section.get('href'))
            category_links = BASE_URL + a_section.get('href')
            urls.append(category_links)
    return urls

def find_urls_with_product_links(n):
    urls = []
    while n < 5:

        n+=1
        urls.append("http://www.anipet.com/prod-list-1.php?id="+str(n))
    return urls

def decide_if_url_has_content():
    urls = []
    urls.append(find_urls_with_product_links(1))
    for url in find_urls_with_product_links(1):
        good_urls = []
        #print url
        soup = make_soup(url)
        if soup.find_all(class_="prod-hdr"):
            good_urls.append(url)
    return good_urls
 
if __name__ == '__main__':
    link = ("http://www.anipet.com/prod-list-1.php?id=1394")
    data = []
    results = find_product_links(link)
    data.append(decide_if_url_has_content())
    for result in results:
        some_link = result
        #data.append(some_link)
    #print data
    #for product in results:
        #data.append(find_info_on_product(product))
    print data
        
       
    
