class Animal:

    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} -> {self.sound}")

dog = Animal("bobik ", "byaqa kee")
cat = Animal("saripishka ", "tur yuqol")

dog.make_sound()
cat.make_sound()

