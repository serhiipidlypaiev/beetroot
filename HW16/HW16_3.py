class Product:
    def __init__(self, type, name, price) -> None:
        self.type = type
        self.name = name
        self.price = price


class ProductStore:
    def __init__(self) -> None:
        self.product_list = {}
        self.profit = 0

    def add_product(self, product, amount):
        self.product_list[product] = amount

    def set_discount(self, identifier, percent, identifier_type):
        self.identifier = identifier
        self.percent = percent
        self.identifier_type = identifier_type
        for product in self.product_list.keys():
            if product.name == self.identifier or product.type == self.identifier_type:
                product.price = product.price * ((100 - self.percent) / 100)

    def sell_product(self, product_name, amount):
        self.product_name = product_name
        self.amount = amount
        for product in self.product_list.keys():
            if self.product_name == product.name:
                amount_from_dict = self.product_list.get(product)
                print(amount_from_dict)
                if amount_from_dict < amount:
                    raise ValueError("Not enouth product")
                else:
                    self.product_list[product] = amount_from_dict - amount
                    self.profit += amount * product.price
                    print(self.profit)
            else:
                raise NameError("No product")

    def get_income(self):
        return self.profit

    def get_all_products(self):
        for i, k in self.product_list.items():
            print(f"Produkt: {i.name} amount: {k}")

    def get_product_info(self, product_name):
        for product in self.product_list:
            if product.name == product_name:
                return (product.name, self.product_list.get(product))
