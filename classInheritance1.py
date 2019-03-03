class Fruits:
    other_fruits = "these are some other important fruits: pawpaw, berries, bananas"

    def __init__(self, fruit1, fruit2):
        self.fruit1 = fruit1
        self.fruit2 = fruit2

    def mango(self):
        print(self.fruit1, " is one of the delicious fruits in the world")

    def orange(self):
        print(self.fruit2, " is the packed with vitamin C")


class Health(Fruits):
    def exercise(self):
        print(f"to have a good health one has to exercise regularly and eat a {self.fruit1} and an {self.fruit2} every morning")

    def sleep(self):
        print("a person should also sleep well for better health")


def main():
    awesomeness = Health("Mango", "Orange")
    awesomeness.orange()
    awesomeness.mango()
    awesomeness.exercise()
    print(awesomeness.other_fruits)
    awesomeness.sleep()


if __name__ == "__main__":
    main()
