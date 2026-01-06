def number_of_cars_needed(no_of_people):
    if no_of_people % 5 == 0:
        result = no_of_people / 5
    elif no_of_people % 5 != 0:
        result = int(no_of_people / 5) + 1 
    return result
        


no_of_people = int(input())
result = number_of_cars_needed(no_of_people)
print(int(result))
