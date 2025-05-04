height=10
weight=20
## BMI calculated by dividing weight by square of height.

bmi=weight/(height*height)
## exponent can be done using bmi=weight/height**2

print(f"The BMI of the person with height {height} is {weight} is {round(bmi,3)}")