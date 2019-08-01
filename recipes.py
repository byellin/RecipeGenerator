import pandas as pd 
import json

#recipes = pd.read_json("recipes.json")

data=None
with open("recipes_raw_nosource_ar.json", "r") as read_file:
    data = json.load(read_file)

#print(data)

recipe_ids = []

count=0
for id, recipe in data.items():
	count = count+1
	#print("id: {}".format(id))
	#print("recipe: {}".format(recipe))

	try:

		print("title: "+str(recipe['title']))

		#print("instructions:", recipe['instructions'])

		

		ingredients = []


		for ingredient in recipe['ingredients']:

			if " ADVERTISEMENT" in ingredient:
				ingredient = ingredient[:-13]
			
			#print("Ingredient:", ingredient)
			#print("Boop")

			#print("ingredient[0] is ",ingredient[0])
			try:
				while ingredient[0] in '1234567890/ ':
					try:
						#print("entered the try statement")
						ingredient = ingredient[1:]
						#print("got to the end of the try statement")
					except IndexError:
						pass
			except:
				pass
			#print("exited the if statement")
			ingredients.append(ingredient)
			#print("appended to ingredients_without_amounts")
		#print("ingredients without amounts: ",ingredients_without_amounts)
		print("ingredients: ",ingredients)
	except KeyError:
		print("Hit a KeyError exception")
		continue
	
	except UnicodeEncodeError:
		print("Hit a UnicodeEncodeError exception")
		continue
	#print("after the KeyError exception")
	#print("after the UnicodeEncodeError exception")

	#print(recipe[u'ingredients'])
	#print('ingredients' in data.items()['wcqidH1M2ULuZG4hS/IztpBVyD4D1TO'])

	#for key, value in recipe.items():
		#print("Item for {}: {}\n".format(key, value))
#print(data['rmK12Uau.ntP510KeImX506H6Mr6jTu'])



#example = {u'instructions': u'In a small saucepan, combine the strawberry preserves, minced garlic, soy sauce and horseradish. Cook over low heat, stirring frequently until heated through.\nMelt butter in a medium skillet. Lightly sprinkle both sides of each pork chop with cayenne pepper. Fry the chops until browned on each side, then continue to cook over medium heat until no longer pink, and the juices run clear.\nServe chops with sauce poured over, and garnish with fresh strawberries.\n', u'ingredients': [u'1/4 cup strawberry preserves ADVERTISEMENT', u'1 1/2 tablespoons minced garlic ADVERTISEMENT', u'1 tablespoon soy sauce ADVERTISEMENT', u'1 tablespoon prepared horseradish ADVERTISEMENT', u'2 pork chops ADVERTISEMENT', u'1 tablespoon butter ADVERTISEMENT', u'1 pinch cayenne pepper ADVERTISEMENT', u'4 fresh strawberries for garnish ADVERTISEMENT', u'ADVERTISEMENT'], u'picture_link': u'2kBc25yaAEqpfdlAvTSW24vZgvrE6si', u'title': u"Leslie's Strawberry Breakfast Chops"}

#print(example['instructions'])
print(count)
print(len(data.items()))
print("all lookin' good so far")