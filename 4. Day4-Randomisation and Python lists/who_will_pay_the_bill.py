## There are friends and they want to randomly choose who will pay the bill.
# The program will randomly select one of the friends to pay the bill.
import random 

friends=["Alice", "Bob", "Charlie", "David",'Emanuel']

random_index= random.randint(0, len(friends)-1)# why len(friends)-1? because the index starts from 0 and ends at len(friends)-1
print(f"{friends[random_index]} is going to pay the bill. [Random Method is used]")

## we have another way to do this using choice() method
random_friend=random.choice(friends) ## it selects a random item from the list
print(f"{random_friend} is going to pay the bill.[Choice Method is used]")

## we can also use shuffle() method to shuffle the list and then select the first item
random.shuffle(friends) ## it shuffles the list
print(f"{friends[0]} is going to pay the bill.[Shuffle Method is used]")
