from customer import Customer
from discount_rule_interface import IDiscountRule


# Regular Customer Rule
class RegularCustomerRule(IDiscountRule):

    def apply_rule(self, customer: Customer):
        if customer.membership_level == 'regular':
            return 0.10  # 10% discount
        return 0
