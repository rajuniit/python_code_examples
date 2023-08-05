import classes

Customer = classes.Customer


class DiscountPercentageCalculator:

    @staticmethod
    def calculate(customer: Customer) -> float:
        max_discount = 0.0
        if customer.membership_level == "regular":
            max_discount = max(max_discount, 0.10)
        elif customer.membership_level == "premium":
            max_discount = max(max_discount, 0.20)
        elif 12 <= customer.age <= 14:
            max_discount = max(max_discount, 0.25)
        return max_discount


if __name__ == '__main__':
    customer1 = Customer("Meena", "regular", 15)
    customer2 = Customer("Raju", "premium", 12)
    customer3 = Customer("Mithu", "regular", 12)

    print(DiscountPercentageCalculator.calculate(customer1) * 100)
    print(DiscountPercentageCalculator.calculate(customer2) * 100)
    print(DiscountPercentageCalculator.calculate(customer3) * 100)
