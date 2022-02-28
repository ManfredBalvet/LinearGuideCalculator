class ShaftComposite:
    def __init__(self, shafts, quantities, difference):
        self.nb_of_segments = sum(quantities)
        self.price = sum([shaft.price * quantity for shaft, quantity in zip(shafts, quantities)])
        self.shafts = shafts
        self.quantities = quantities
        self.difference = difference
