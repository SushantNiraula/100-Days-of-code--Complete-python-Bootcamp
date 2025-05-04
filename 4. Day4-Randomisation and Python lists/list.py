'''
Imagine you have a shopping list. It's a collection of items, right? A Python list is quite similar –
it's an ordered collection of items. These items can be of different data types too! For example,
you could have a list containing strings (like names of fruits), numbers (like prices), and even other lists!

'''

my_list = ["apple", 1.99, "banana", 2, ["grocery", "store"]]## nested list i.e list inside a list
print(my_list)

'''
What makes lists special and different from, say, individual variables?

Ordered: The items in a list have a specific order, and that order is maintained.
        "apple" will always come before 1.99 in our my_list unless we change it.
Mutable: You can change the contents of a list after it's created. You can add, remove, or modify items.   
Allows Duplicates: Lists can contain multiple occurrences of the same item.

'''

## Understanding Index is an important part of learning about list.
'''
In Python lists (and many other programming structures), we access items using their index.
 Think of the index as the item's position in the list. Importantly, Python uses zero-based indexing.
 This means the first item is at index 0, the second at index 1, and so on.
 This "index" is often referred to as the "offset" from the beginning of the list.


 So, in our my_list:

"apple" is at index (offset) 0   
1.99 is at index (offset) 1
"banana" is at index (offset) 2
2 is at index (offset) 3
["grocery", "store"] is at index (offset) 4
'''
## how to access the items in the list
print(my_list[0]) ## prints the first item in the list
print(my_list[1]) ## prints the second item in the list
## We can also access the last item in the list using negative indexing.
print(my_list[-1]) ## prints the last item in the list
## Let's access the nested list inside the list
print(my_list[4]) ## prints the nested list
## We can also access the items inside the nested list using indexing
print(my_list[4][0]) ## prints the first item in the nested list

## Updating a list
new_item="orange"
my_list.append(new_item) ## adds the new item to the end of the list
print(my_list) ## prints the updated list   
## We can also insert the new item at a specific index in the list
my_list.insert(2, "grape") ## adds the new item at index 2
print(my_list) ## prints the updated list
## change the value of an item in the list
my_list[1] = 2.99 ## changes the value of the item at index 1
print(my_list) ## prints the updated list

## remove an item from the list
my_list.remove("banana") ## removes the item from the list
print(my_list) ## prints the updated list
## We can also remove the last item from the list using pop() method
my_list.pop() ## removes the last item from the list
print(my_list) ## prints the updated list

## We can also remove an item from the list using its index
my_list.pop(2) ## removes the item at index 2
print(my_list) ## prints the updated list
## We can also remove all the items from the list using clear() method
my_list.clear() ## removes all the items from the list
print(my_list) ## prints the updated list   
## We can also delete the list using del keyword
del my_list ## deletes the list
print(my_list) ## prints the updated list
## we get error: NameError: name 'my_list' is not defined

## Index errors are common when working with lists.
## They occur when you try to access an index that doesn't exist in the list.
## For example, if you have a list with 5 items (indices 0 to 4) and try to access index 5, you'll get an IndexError.