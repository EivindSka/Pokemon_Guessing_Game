

from catclass import Cat
import catclass


def test():
    b = Cat("KitKat", 1, "tabby")
    c = Cat("Snupi", 2, "black")
    print(b)
    print(c)
    b.description()
    c.description()

    b.meow()
    c.hungry()
    c.eat()


if __name__ == "__main__":
    x = Cat("test")
    print(x)
    test()
