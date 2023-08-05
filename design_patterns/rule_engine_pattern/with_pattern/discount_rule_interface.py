from customer import Customer


# Discount Rule Interface
class IDiscountRule:
    def apply_rule(self, customer: Customer) -> float:
        pass
