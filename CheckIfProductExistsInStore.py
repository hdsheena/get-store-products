import json

store_data = open("convertcsv.json", "r").read()
anipet_data = open("AnipetDatafull.json", "r").read()

store_products = json.loads(store_data)

anipet_products = json.loads(anipet_data)
smaller_anipet_products = anipet_products[0:15]
bionic_anipet_products = []

for anipet_product in anipet_products:
	if anipet_product["description"][0:8] == "Bionic U":
		anipet_product_name = anipet_product["description"]
		bionic_anipet_products.append(anipet_product_name)
		
store_prod = []
not_a_product = []
#print bionic_anipet_products

for store_item in store_products:
	full_product_name = store_item["Product Name"]
	name_match = full_product_name.split("(")
	"""	
	if len(name_match) <1:
		print store_item
	if len(name_match[0]) <1:
		print store_item
	"""
	try:
		if name_match[0][0] != "[":
			store_prod.append({'full_name': full_product_name,
									'short_name': name_match[0][0:15]})
	except:
		not_a_product.append(store_item)
"""	
	if name_match[0]:
		first_item = name_match[0]
		if first_item[0] == "[":
			not_a_product.append(name_match[0][0:15])
			#break
		else:
			store_prod.append(name_match[0][0:15])
	
	if name_match[0][0] == "[":
		#not_a_product.append(name_match[0][0:15])
		break
	else:
		store_prod.append(name_match[0][0:15])
"""
short_store_prod = []
for item in store_prod:
	short_store_prod.append(item["short_name"])
	
print "Product"
print store_prod[short_store_prod.index("Bionic Urban St")]["full_name"]
print len(store_prod)
products_to_import = []
for item in bionic_anipet_products:

	#json code to look up value of product_name
	#ani_prod = item["description"]
	ani_prod = item
	#print item["description"]
	#print ani_prod[0:15]
	#print store_prod[2]
	
	bionic_anipet_products_shortened = item[0:15]
	#print bionic_anipet_products_shortened
	#print bionic_anipet_products_shortened.index(ani_prod[0:15])
	#print type(store_prod)
	if bionic_anipet_products_shortened in short_store_prod:
	#if True:
		try:		
			#print "Trying"	
			product_item = store_prod[short_store_prod.index(ani_prod[0:15])]["full_name"]		
			print ani_prod, "Is the same as ", product_item, "Product"
			#product_item = bionic_anipet_products.index(ani_prod[0:15])		
			#print product_item
			products_to_import.append(product_item)
			#print "Still trying"
		except:
			#print "This item", ani_prod, "isnt in the list"
			pass			
			
#print not_a_product
#print store_products[store_prod.index("Bionic Urban St")]
#print store_products[1]["Product Name"]
#print store_prod[1]
#print store_prod.index("Don't Shoot the")
#store_products_number = store_prod.index("Eyes So Bright")
#print store_products[store_products_number]["Product Name"]
#print store_prod[0:50]
print products_to_import
#print "Product 815", store_prod[815]["full_name"]	
"""
	
#to test logic
list_of_store_products = ["One product here", "Another separate product", "third and final product"]
list_of_anipet_products = ["Three products is", "Not quite enough", "One product herfe"]
for item in list_of_anipet_products:
	products_to_import = []
	ani_prod = item
	#print item["description"]
	store_prod = []
	for store_item in list_of_store_products:
		full_product_name = store_item
		store_prod.append(full_product_name[0:15])
	#print "Product", store_prod
	#print ani_prod[0:15]
	if ani_prod[0:15] in store_prod:
		print ani_prod, "Is the same as ", list_of_store_products[store_prod.index(ani_prod[0:15])]
		products_to_import.append(item)
	
print products_to_import
"""
