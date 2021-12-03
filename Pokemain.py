from playsound import playsound
from pydub import AudioSegment
from pydub.playback import play
from time import sleep
import pyttsx3

a1 = "Pikachu"
a2 = "Balbasaur"
a3 = "Charmander"
evo = "Evolution is Happening\n"
engine = pyttsx3.init()


class Pokemon():
    def __init__(self, name, type, special, evolution):
        self.name = name
        self.type = type
        self.special = special
        self.evolution = evolution

    def description(self):
        print(f"I am {self.name} and I'am an {self.type} Pokemon!\n")

    def showSpecial(self):
        print(f"My special attack is {self.special}")

    def exhausted(self):
        print(f"{self.name} is exhausted")

    def evolve(self):
        print(f"{self.name} is evolving!")
        sleep(1)
        for i in range(22):
            print(evo[i], sep=" ", end=" ", flush=True)
        print(f"{self.name} evolved to {self.evolution}")

    def eat(self):
        print(f"{self.name}: nom nom nom")

    def sound(self):
        playsound(f'./{self.name.lower()}.mp3')


class Pikachu(Pokemon):
    def __init__(self):
        super().__init__('Pikachu', 'Electric', 'Thunderbolt', 'Raichu')

    def quote(self):
        print("PIKACHU!")


class Balbasaur(Pokemon):
    def __init__(self):
        super().__init__('Balbasaur', 'Grass', 'Razor Leaf', 'Ivysaur')

    def quote(self):
        print("BALBA BALBA!")


class Charmander(Pokemon):
    def __init__(self):
        super().__init__('Charmander', 'Fire', 'Scratch', "Charmelon")

    def quote(self):
        print("CHAR CHAR CHAR")


class Onix(Pokemon):
    def __init__(self):
        super().__init__('Onix', 'Ground', 'Rock Throw', 'Steelix')

    def quote(self):
        print('OHH , ARRRR')

    def say(self):
        engine.say()
        engine.runAndWait()


b = Balbasaur()
p = Pikachu()
c = Charmander()
o = Onix()

# o.say()


while True:
    p.sound()
    if input("Enter the pokemons name: ") == a1 or "Pika":
        print("Correct!")
        p.description()
        break
while True:
    b.sound()
    if input("What is this pokemon? ") == "Balbasaur":
        print("Correct!")
        b.description()
        break
while True:
    if input("It's a Fire starter pokemon: ") == "Charmander":
        print("Correct!")
        c.sound()
        c.description()
        break


b.evolve()
# Pikachu

# p.sound()p

# sleep(0.55)
# p.description()

# # Balbasaur

# sleep(3)
# b.sound()
# sleep(1)
# b.description()
