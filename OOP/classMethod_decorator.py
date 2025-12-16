# @classMethod is used to call the class within the class. (calling the __init__)

class Chai:

    def __init__(self, type, price):
        self.type = type
        self.price = price


    @classmethod
    def from_dict(cls, data):
        # Calling the Chai class using cls, calling the constructor.
        return cls(data['type'], data['price'])



chaiOne = Chai('Black', 50)
print(chaiOne.type, chaiOne.price)

chaiTwo = Chai.from_dict({'type': 'Ginger', 'price': 80})
print(chaiTwo.type, chaiTwo.price)