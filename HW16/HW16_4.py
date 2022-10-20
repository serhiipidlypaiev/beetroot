class CustomException(Exception):

    def __init__(self):
        self.logs = open('logs.txt', 'a+', encoding='utf8')

    def __enter__(self):
        return self.logs 

    def __exit__(self, *exc):
        if any(exc):
            print(exc)
            self.logs.write(str(exc))
