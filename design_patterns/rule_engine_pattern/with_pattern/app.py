import os
import sys

from customer import Customer
from rules.regular_customer_rule import RegularCustomerRule
from rules.premium_customer_rule import PremiumCustomerRule
from rules.teenage_customer_rule import TeenageCustomerRule

from rule_engine import DiscountRuleEngine


parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)

if __name__ == '__main__':
    customer1 = Customer("Meena", "regular", 15)
    customer2 = Customer("Raju", "premium", 12)
    customer3 = Customer("Mithu", "regular", 12)

    teenage_customer_rule = TeenageCustomerRule()
    regular_customer_rule = RegularCustomerRule()
    premium_customer_rule = PremiumCustomerRule()

    discount_rule_engine = DiscountRuleEngine()
    discount_rule_engine.add_rule(teenage_customer_rule)
    discount_rule_engine.add_rule(regular_customer_rule)
    discount_rule_engine.add_rule(premium_customer_rule)

    print(f"{customer1.name}'s Discount: {discount_rule_engine.get_discount_percentage(customer1) * 100:.1f}%")
    print(f"{customer2.name}'s Discount: {discount_rule_engine.get_discount_percentage(customer2) * 100:.1f}%")
    print(f"{customer3.name}'s Discount: {discount_rule_engine.get_discount_percentage(customer3) * 100:.1f}%")
