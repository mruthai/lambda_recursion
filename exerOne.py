

#Output: ['Argentina', 'San Diego', 'Boston', 'New York']

places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]

countries = list(filter(lambda x : x >= ',' , places))

print(countries)