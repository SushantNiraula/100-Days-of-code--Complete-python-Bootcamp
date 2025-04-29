exam_scores=[150,142,185,180,120,80,90,100,110,130,140,160,170,200]

total_score= sum(exam_scores)
print(f"Total score of all students is {total_score}")

sum=0
for score in exam_scores:
    sum+=score
print(f"Sum of all scores is {sum}")

# Find the highest score
heighest_score=max(exam_scores)
print(f"Highest score is {heighest_score}")
heighest_score=exam_scores[0]
for score in exam_scores:
    if score> heighest_score:
        heighest_score=score
print(f"Highest score is {heighest_score}")