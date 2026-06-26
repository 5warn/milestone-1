#find the score of the runner up
scores=[2, 3, 6, 6, 5]

#remove duplicates
unique_scores=list(set(scores))

#sort the unique scores in descending order
unique_scores.sort(reverse=True)

#the runner up score is the second element in the sorted list
runner_up_score=unique_scores[1]

print(runner_up_score)