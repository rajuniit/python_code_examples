from customer import Customer
from discount_rule_interface import IDiscountRule


# Teenage Customer Rule
class TeenageCustomerRule(IDiscountRule):

    def apply_rule(self, customer: Customer):
        if 12 <= customer.age <= 14:
            return 0.25  # 25% discount
        return 0.0
