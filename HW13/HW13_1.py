def number_of_loc_variables(one_more = 5):
    first_variable = 10
    second_variable = 25
    third_variable = "third"

print(number_of_loc_variables.__code__.co_nlocals)