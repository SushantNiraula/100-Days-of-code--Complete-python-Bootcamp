# Dictionary is a collection of key-value pairs like a table .
# Dictionary is mutable, unordered and indexed by keys.
# Dictionary is created using curly braces {} or the dict() function.
car={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964,
    "color":"red",
    "features":["air conditioning","power windows","sunroof"],
}
print(car)
print(car['brand'])
## Nested dictionary:
cars={
    'BMW':{
        'model':'X5',
        'year':2020,
        'color':'black',
        'features':['leather seats','sunroof']
    },
    'Ford':{
        'model':'Mustang',
        'year':1964,
        'color':'red',
        'features':['air conditioning','power windows','sunroof']
    },
    'Toyota':{
        'model':'Camry',
        'year':2021,
        'color':'blue',
        'features':['backup camera','blind spot monitoring']
    }

}
print(cars['BMW'])
## Accessing nested dictionary:
print(cars['BMW']['model'])
## Other operations on dictionary are :
