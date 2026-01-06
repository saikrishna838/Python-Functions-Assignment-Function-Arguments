def get_lower_and_upper_case_letters(word):
    upper_case = "".join([char for char in word if char.isupper()])
    lower_case = "".join([char for char in word if char.islower()])
    
    print(upper_case)
    print(lower_case)
    
word = input()
get_lower_and_upper_case_letters(word)
