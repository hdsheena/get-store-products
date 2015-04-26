import json

store_data = open("convertcsv.json", "r").read()
anipet_data = open("AnipetDatafull.json", "r").read()

store_products = json.loads(store_data)

anipet_products = json.loads(anipet_data)
smaller_anipet_products = anipet_products[0:15]
anipet_product_names = []

for anipet_product in anipet_products:
	#print anipet_product["description"]
	anipet_product_name = anipet_product["description"]
	anipet_product_names.append(anipet_product_name)
		
store_prod = []
not_a_product = []

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
	

products_to_replace = []
products_to_import = []
for item in anipet_product_names:

	#json code to look up value of product_name
	ani_prod = item
	#print item
	anipet_products_shortened = item[0:15]

	if anipet_products_shortened in short_store_prod:
		location_of_product = short_store_prod.index(anipet_products_shortened) +1
		try:		
			product_item = store_prod[short_store_prod.index(ani_prod[0:15])]["full_name"]		
			print ani_prod, "Is the same as ", product_item, "Product"
			if raw_input()=="y":
				products_to_replace.append(product_item)
				products_to_import.append(ani_prod)
			else:
				if anipet_products_shortened in short_store_prod[location_of_product:]:
					location_of_product = short_store_prod[location_of_product:].index(anipet_products_shortened)
					try:		
						product_item = store_prod[short_store_prod.index(ani_prod[0:15])]["full_name"]		
						print ani_prod, "Is the same as ", product_item, "Product"
						if raw_input()=="y":
							products_to_replace.append(product_item)
							products_to_import.append(ani_prod)
					except:
						pass
		except:
			#print "This item", ani_prod, "isnt in the list"
			pass			
			

print products_to_replace
print products_to_import
