class SunManager:
    def __init__(self, initial_amount=30):
        self.total = initial_amount

    def add_sun(self, amount):
        self.total += amount

    def spend_sun(self, cost):
        if self.total >= cost:
            self.total -= cost
            return True
        return False
