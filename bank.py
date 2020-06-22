class Bank():
    def __init__(self):
        self.balance = 0

    def add_money(self, amount):
        try:
            self.balance += amount
        except TypeError:
            print('(error): Please enter a numeric value')
            raise


region = Bank()

region.add_money(200)
# region.add_money("won't work")

print(region.balance)
