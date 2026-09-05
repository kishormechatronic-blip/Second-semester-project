scores = {'Alice': 85, 'Bob': 62, 'Charlie': 90, 'Diana': 55}
scores1 = {keys: value for keys, value in scores.items() if value >= 70}
print(scores1)
