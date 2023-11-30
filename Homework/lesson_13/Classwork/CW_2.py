class Price:
    def __init__(self, value):
        self.value = value

    def get_price(self):
        return self.value


class DiscountPrice(Price):
    def __init__(self, number, discount):
        super().__init__(number)
        self.discount = discount

    def get_price(self):
        original_price = super().get_price()
        return original_price - (original_price * self.discount) / 100


price_obj = Price(100)
print("Price:", price_obj.get_price())

discount_price_obl = DiscountPrice(100, 20)
print('Discount price:', discount_price_obl.get_price())
