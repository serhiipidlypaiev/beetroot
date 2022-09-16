
def outside_func(firtst_number):
    def inside_func(number):
        if number*firtst_number >= 100:
            return print("Number >= 100 ")
        if number*firtst_number < 100:
            return print("Number < 100 ")
    return inside_func
result = outside_func(25)
result(4)