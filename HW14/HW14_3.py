def arg_rules(type_: type, max_length: int, contains: list):
    def inner_decorator(func):
        def wrapper(name):
            if type(name) != type_:
                return False
            elif len(name) >= max_length:
                return False
            elif any(symbol not in name for symbol in contains):
                return False
            else:
                return func(name)  
        return wrapper
    return inner_decorator

@arg_rules(type_= str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

print(create_slogan('S@SH05'))

assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
