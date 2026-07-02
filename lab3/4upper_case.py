scores = {'Alice': 85, 'Bob': 62, 'Charlie': 90, 'Diana': 55}
scores1={ keys.upper(): value for (keys, value) in scores.items()}
print(scores1)