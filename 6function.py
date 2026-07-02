people = {'John': 25, 'Emma': 15, 'Lucas': 8, 'Sophia': 42}
def classify_age(age):
    if age<=13:
        return 'Child'
    elif 19>= age >=13:
        return 'Teen'
    else:
        return 'Adult'
    
check={key:classify_age(age) for (key, age) in people.items()}
print(check)