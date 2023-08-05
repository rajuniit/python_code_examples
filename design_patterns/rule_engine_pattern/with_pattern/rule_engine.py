from customer import Customer
from discount_rule_interface import IDiscountRule


class DiscountRuleEngine:
    def __init__(self):
        self.rules = []

    def add_rule(self, rule: IDiscountRule):
        self.rules.append(rule)

    def get_discount_percentage(self, customer: Customer):
        max_discount = 0.0
        for rule in self.rules:
            discount = rule.apply_rule(customer)
            max_discount = max(max_discount, discount)
        return max_discount
