from customer import Customer
from discount_rule_interface import IDiscountRule


class PremiumCustomerRule(IDiscountRule):

    def apply_rule(self, customer: Customer):
        if customer.membership_level == 'premium':
            return 0.20  # 20% discount
        return 0.0
