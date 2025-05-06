## List comprehension is a concise way to create lists in Python.
# It consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses.

## Example 1:
numbers=[1,2,3]
new_list=[]
for n in numbers:
    add_1=n+1
    new_list.append(add_1)
print(new_list) # [2, 3, 4]

## using list comprehension same thing can be achieved in one line:

new_list=[n+1 for n in numbers] ##[operation for item in iterable]
print(new_list) # [2, 3, 4]

## Can also work with strings:
name="Sushant"
new_list=[letter for letter in name]
print(new_list) # ['S', 'u', 's', 'h', 'a', 'n', 't']

## task 1 to take a range(1,5) and create a list of double of each number in range:
range_list=[item*2 for item in range(1,5)]
print(range_list) # [2, 4, 6, 8]

## names task
names=['Alex','Beth','Caroline','Dave','Eleanor','Freddie']
## task 2 to create a list of names with less than 4 characters or less:
short_names=[item for item in names if len(item)<=4]
print(short_names) # ['Alex', 'Beth', 'Dave']

## task 3 to create a list of names with more than 4 characters and also uppercase:
upper_long_names=[item.upper() for item in names if len(item)>4]
print(upper_long_names) # ['CAROLINE', 'ELEANOR', 'FREDDIE']

## exercise 1:
numbers=[1,1,2,3,5,5,8,13,21,34,55]
squared_numbers=[item*item for item in numbers]
print(squared_numbers) # [1, 1, 4, 9, 25, 25, 64, 169, 441, 1156, 3025]