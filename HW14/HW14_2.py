def stop_words(words: list):
    def inner_decorator(func):
        def wrapper(name):
            sentense = func(name)
            for word in words:
                if word in sentense:
                    sentense = sentense.replace(word,'*')
            return sentense
        return wrapper
    return inner_decorator

@stop_words(['pepsi', 'BMW'])
def create_slogan(name:str) -> str:
     return f"{name} drinks pepsi in his brand new BMW!"

print(create_slogan('Brad'))
 
assert create_slogan("Steve") == "Steve drinks * in his brand new *!"