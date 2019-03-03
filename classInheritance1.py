class Fruits:
    def __init__(self, fruit1, fruit2):
        self.fruit1 = fruit1
        self.fruit2 = fruit2

    def mango(self):
        print(self.fruit1, " is one the delicious fruits in the world")

    def orange(self):
        print(self.fruit2, " is the packed with vitamin C")


class Health(Fruits):
    pass


def main():
    awesomeness = Health("Mango", "Orange")
    awesomeness.orange()


if __name__ == "__main__":
    main()
