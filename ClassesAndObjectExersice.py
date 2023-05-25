# We have a class defined for vehicles. Create two new vehicles called car1 and car2.
# Set car1 to be a red convertible worth $60,000.00 with a name of Fer, and car2 to be a blue van named Jump worth $10,000.00.
# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here
car1 = Vehicle()
car1.name = "Jump"
car1.kind = "Van"
car1.value = 10000.00
car1.color = "Blue"

car2 = Vehicle()
car2.name = "Fer"
car2kind = "conveertible"
car2.value = 600000.00
car2.color = "red"

# test code
print(car1.description())
print(car2.description())