class Person:
    def __init__(self, name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
            print(f"I am {self.name} of {self.age} years, a {self.gender}.")

persona1 = Person("Jane", 34, "female")

persona1.introduce()