def decorator(func):
    def actions(*args, **kwargs):
        print(func.__name__, len(args), args, len(kwargs), kwargs)
        return func(*args, **kwargs)
    return actions

@decorator
def zip_list_turple(names:list, years:list):
    names_years = zip(names, years) 
    return list(names_years)


print(zip_list_turple(['Max', 'Dima', 'Vlad', 'Anna'], [23, 34, 21, 30]))