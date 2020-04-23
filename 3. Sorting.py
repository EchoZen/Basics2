from operator import itemgetter
restaurant= [['Kentucky', 15,10, 'Fried Chicken'],
             ['Macdonald',4,9, 'Burger'],
             ['Subway', 18,6, 'Sandwiches']]
#Field 1(index 0): Name of restaurant
#Field 2(index 1): Distance of restaurant
#Field 3(index 2): Price of food
#Field 4(index 3): Food
sort_field= ['name', 'distance', 'price', 'food']

for i in range(len(sort_field)):
    sort_info= sorted(restaurant, key=itemgetter(i))
    print('sort by', sort_field[i], sort_info)