class Awesome:

    def __init__(self):
        print("this is a constructor method")

    def the_first(self):
        print("this is the first function in the class awesome")

    def the_second(self):
        print("and this is my second function in the class awesome")


def main():
    nice = Awesome()
    nice.the_first()
    nice.the_second()


if __name__ == "__main__":
    main()