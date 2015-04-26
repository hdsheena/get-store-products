#from BeautifulSoup import BeautifulSoup
import urllib2
import csv
import json
import sys
import requests
from bs4 import BeautifulSoup

anipet_data = open("AnipetDatafull.json", "r").read()
anipet_products = json.loads(anipet_data)
root_url = "http://www.anipet.com/product-1.php?item="
list_of_urls = []
for number in anipet_products:
	prod_id = number["product_id"]
	true_url = root_url + str(prod_id)
	list_of_urls.append(true_url)
	#print true_url
data_for_exporting = []
headers = []

#print type(list_of_urls)
for url in list_of_urls:
	page = urllib2.urlopen(url)
	#print page
	soup = BeautifulSoup(page.read())
	h5tag = soup.find("div", {"class" : "column-290 float-right"})
	tagfors = []
	parents = []
	for i in h5tag:
		parents += i.parent
		tagfors += [type(tag) for tag in i]
	#print parents[8].sibling
	tags = [(type(tag), tag) for tag in h5tag]
	#print tags[9]
	#print type(soup)
	content = soup.find(id="content")
	#print type(content)
	data_found = content.find("div", { "class" :"set-size" })
	#print type(data_found)
	product_area = data_found.find("span", { "class" :"prod_name" })
	#print product_area
	product_name = product_area.text
	#content[0]
	description_area = data_found.find("h5").next
	
	
	description = description_area.next
	images = []
	image_url_area = soup.findAll("img")
	#print "Find this", image_url_area
	for picture in image_url_area:
		image = picture.get('src')
		#print image[0:3]
		if image[0:3] == 'pro':
		
			#print image
			images.append(root_url + str(image))
	data_for_exporting.append( {'product_name':product_name,
		                                'description':description,
		                                'image_url1':images})
"""
for url in list_of_urls:	
	#url = root_url + "prod-list-1.php?id=" + str(number) 	
	try:
			
		page = requests.get(url)
		
		#headers.append(header)
		#page = urllib2.urlopen(url)
		soup = BeautifulSoup(page.content)
		content = soup.find(id="content")
		data_found = content.find("div", { "class" :"set-size" })
		#print "Soup is " + soup[0:50]
			

		try:
		    product_name = data_found.find(class_="prod_name").text
		    #url_to_product_page = root_url + data_found.find('a').get('href')
		    description = data_found.find('h5').findNext.text
		   
		    image_url = root_url + data_found.find(class_="column-320 float-left").findAll('img').get('src')
		    data_for_exporting.append( {'product_name':product_name,
		                                'description':description,
		                                'image_url1':image_url[0],
		                                'image_url2':image_url[1]})
		except:
		 	print "This didnt work" + str(sys.exc_info())
	
	except:
		print "This product " + url + " has no page" + str(sys.exc_info())
"""
print type(data_for_exporting)


"""To get the code to write to the import file"""
#Where anipet.json[produt name] is in store.json[product name]
#if store.json[that-product][lookup description] is not blank, ABORT
#if store.json[that-product][lookup imageurl] is not blank, ABORT
#store.json[that-product][lookup description] = anipet.json[that product][description]
#store.json[that-product][lookup Product Image File - 1] = anipet.json[that product][imageurl]

#convert store.json back to csv for import to store


with open('1ProductDataTest.csv', 'w') as fp:
    writer = csv.DictWriter(fp, fieldnames=data_for_exporting[0].keys())
    writer.writeheader()
    try:
	    for product in data_for_exporting:
	        writer.writerow(product)
    except:
        print "This data " + str(product) + " couldn't be put in the table"

with open('1ProductDataTest.json', 'w') as fp:
    fp.write(json.dumps(data_for_exporting,
                        sort_keys=True,
                        indent=4,
                        separators=(',', ': ')))
