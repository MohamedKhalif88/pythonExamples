class Awesome:

    def __init__(self, name):
        self.name = name

    def the_first(self):
        print(self.name + " this is the first function in the class awesome")

    def the_second(self):
        print(self.name + " and this is my second function in the class awesome")


def main():
    nice = Awesome("mak")
    nice.the_first()
    nice.the_second()


if __name__ == "__main__":
    main()