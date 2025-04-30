def calculate_love_score(name1,name2):
    name=name1 + name2
    name=name.upper()
    score_love=0
    score_true=0
    for letter in name:
        if letter in "LOVE":
            score_love+=1
    for letter in name:
        if letter in "TRUE":
            score_true+=1
    print(score_true*10+score_love)
# Example usage
calculate_love_score("Kanye West", "Kim Kardashian")
calculate_love_score(name1 = "Angela Yu" ,name2 = "Jack Bauer")