import pandas as pd

df=pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

df_squirrel_count=df['Primary Fur Color'].value_counts()
df_squirrel_count.to_csv("squirrel_count.csv")
print(df_squirrel_count)

grey_squirrel_count=len(df[df['Primary Fur Color']=='Gray'])
red_squirrel_count=len(df[df['Primary Fur Color']=='Cinnamon'])
black_squirrel_count=len(df[df['Primary Fur Color']=='Black'])
print(f"Grey Squirrel Count: {grey_squirrel_count}")
print(f"Red Squirrel Count: {red_squirrel_count}")
print(f"Black Squirrel Count: {black_squirrel_count}")

data_dict={
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrel_count, red_squirrel_count, black_squirrel_count]
}
df_squirrel_count=pd.DataFrame(data_dict)
df_squirrel_count.to_csv("squirrel_count.csv")