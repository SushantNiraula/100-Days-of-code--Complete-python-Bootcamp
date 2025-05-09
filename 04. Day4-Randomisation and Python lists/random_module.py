'''
Randomization is the process of making something random. It is essential because our computers are Deterministic machines, 
meaning they will always produce the same output for a given input. 
Randomization is used in various fields, including cryptography, gaming, and simulations.

Python uses Mersenne Twister as the core generator. 
It is a pseudorandom number generator (PRNG) that is widely used for its speed and quality of randomness.

The random module in Python provides functions for generating pseudo-random numbers.
 These numbers aren't truly random in a mathematical sense (they are generated by deterministic algorithms),
 but for most practical purposes, they appear random.
 This module is incredibly useful for simulations, games, generating unique identifiers, and much more!

''' 



import random

# Random number between 1 and 10
random_number = random.randint(1, 10)
print(f"Random number between 1 and 10: {random_number}")
# Random float between 0 and 1
random_float = random.random()
print(f"Random float between 0 and 1: {random_float}")

## choice from a list
fruits = ["apple", "banana", "cherry", "date"]
random_fruit = random.choice(fruits)
print(f"Random fruit from the list: {random_fruit}")

## Let's learn about shuffling a list

shuffled_fruits = fruits.copy()  # Create a copy to shuffle
random.shuffle(shuffled_fruits)
print(f"Shuffled fruits: {shuffled_fruits}")

## uniform function in random module is used to generate a random float number between two specified values.
random_uniform = random.uniform(1, 10)
print(f"Random float between 1 and 10: {random_uniform}")