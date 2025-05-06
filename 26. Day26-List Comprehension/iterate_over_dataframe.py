import pandas as pd
student_dict={
    "student":['Angela','James','Lily'],
    "score":[56,76,98]

}

student_df=pd.DataFrame(student_dict)
print(student_df)

for (key,value) in student_df.items():
    print(f"keys are\n: {key}")
    print(f"values are\n: {value}")

## pandas built in loops
for (index, row) in student_df.iterrows():
    print(f"index is\n: {index}")
    print(f"row is\n: {row}")
