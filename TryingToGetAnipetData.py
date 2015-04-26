from BeautifulSoup import BeautifulSoup
import urllib2
import csv
import json
import sys

root_url = "http://www.anipet.com/"
list_of_numbers = range(0,3000)
data_for_exporting = []
for number in list_of_numbers:	
	url = root_url + "prod-list-1.php?id=" + str(number) 	
	try:
			
		page = urllib2.urlopen(url)
		soup = BeautifulSoup(page.read())
		content = soup.find(id="content")
		content_data = content.find('ul').findAll("div", { "class" :"data" })
		
	
		
		for data_found in content_data:
		    product_id = data_found.find('u').text
		    url_to_product_page = root_url + data_found.find('a').get('href')
		    description = data_found.find('a').text[len(product_id):]
		   
		    image_url = root_url + data_found.findPrevious('div').find('img').get('src')
		    data_for_exporting.append( {'product_id':product_id,
		                                'description':description,
		                                'image_url':image_url,
		                                'product_link':url_to_product_page})
	except:
		print "This url " + url + " has no page" + str(sys.exc_info())

with open('AnipetDatafull.csv', 'w') as fp:
    writer = csv.DictWriter(fp, fieldnames=data_for_exporting[0].keys())
    writer.writeheader()
    try:
	    for product in data_for_exporting:
	        writer.writerow(product)
    except:
        print "This data " + str(product) + " couldn't be put in the table"

with open('AnipetDatafull.json', 'w') as fp:
    fp.write(json.dumps(data_for_exporting,
                        sort_keys=True,
                        indent=4,
                        separators=(',', ': ')))
