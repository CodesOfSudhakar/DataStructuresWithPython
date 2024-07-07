# class kettle(object):

class kettle():  # In python 3, there is no need to explicitly use the Object like in the previous line which is done
    # in python 2.x

    def __init__(self, make, price):
        self.make = make
        self.on = False
        self.price = price

    def turn_on(self):
        self.on = True


# __init__ is a constructor

brandOne = kettle("BRandname", 10)
print(brandOne.price)
print(brandOne.make)

brandTwo = kettle("Second brand", 22)
print(brandTwo.price)
print(brandOne.make)

print("The brand and its prices are, {}:{} and {}:{}".format(brandOne.make, brandOne.price, brandTwo.make,
                                                             brandTwo.price))

# An alternative way to print the same content.
# Since brandOne and brandTwo are the objects of the class kettle,
# we can simply mention their attributes in the replacement fields.

print("The brand and its prices are, {0.make}={0.price} and {1.make}:{1.price}".format(brandOne, brandTwo))

print(brandOne.on)  # Returns false, as it access the init method
brandOne.turn_on()  # This calls the newly created method to turn on the indicator
print(brandOne.on)  # As a result of previous line, this will return True
brandOne.turn_on()
