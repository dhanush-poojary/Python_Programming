class car:
    model = None

    def __init__(self, model):
        self.model = model

    def show(self):
        print(f"The model is: {self.model}")


class sports(car):
    horsePower = None

    def __init__(self, horsePower):
        self.horsePower = horsePower

    def show(self):
        print(f"The horsepower is: {self.horsePower}")


class bmw(sports):
    name = "bmw"


b = car(1997)
b.show()

b = sports(600)
b.show()
