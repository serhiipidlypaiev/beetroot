class Dogtohuman:
    def __init__(self, dog_age):
        self.dog_age = dog_age

    def human_age(self):
        return f"Human age = {self.dog_age*7}"


dog = Dogtohuman(10)

print(Dogtohuman.human_age(dog))
