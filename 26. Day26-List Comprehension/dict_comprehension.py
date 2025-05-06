## new_dict={new_key:new_value for item in iterable if condition}
# new _dict={new_key: new_value for (key, value) in dict.items() if condition}
import random
names=['Alex','Beth','Caroline','Dave','Eleanor','Freddie']
students_scores={key:random.randint(0,100) for key in names }
print(students_scores) # {'Alex': 78, 'Beth': 65, 'Caroline': 87, 'Dave': 90, 'Eleanor': 56, 'Freddie': 45}

## pass student dictionary to new dictionary with only students who scored more than 60:
passed_students={ student:marks for (student,marks) in students_scores.items() if marks>=60}
print(passed_students) # {'Alex': 78, 'Caroline': 87, 'Dave': 90}

## exercise 2:
# Create a dictionary called result with the keys as the words in the sentence and the values as the number of letters in each word.
sentence='What is the Airspeed Velocity of an Unladen Swallow?'
result={word:len(word) for word in sentence.split()}
print(result)

## exercise 3:
weather_c ={"Monday":12, "Tuesday":14, "Wednesday":15, "Thursday":14,"Friday":21, "Saturday":22, "Sunday":24}
weather_f={day:(tempr*9/5 + 32) for day,tempr in weather_c.items()}
print(weather_f)