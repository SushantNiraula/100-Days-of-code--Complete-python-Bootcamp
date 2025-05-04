## list can be nested inside dictionaries.
fruits={
    'mango':['Yellow','Orange','Green'],
    'banana':['Green','Yelllow'],
    'orange':['Green','Orange'],

}
print(fruits['mango'][0])
fruits[1]='apple' # Adding a new key-value pair to the dictionary i.e 1:'apple'
print(fruits)