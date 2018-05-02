import unittest2 as unittest
from ipynb.fs.full.index import *

class TestObjectAttributes(unittest.TestCase):

    def test_cash_register_class(self):
        example_cr = CashRegister()
        self.assertEqual(type(example_cr), type(CashRegister()))

    def test_cash_register_initial_values(self):
        example_cr = CashRegister()
        self.assertEqual(example_cr._total, 0)
        self.assertItemsEqual(example_cr._items, [])

    def test_cash_register_initial_values_with_discount(self):
        example_cr = CashRegister(50)
        self.assertEqual(example_cr._total, 0)
        self.assertItemsEqual(example_cr._items, [])
        self.assertEqual(example_cr._employee_discount, 50)

    def test_cash_register_decorator_methods(self):
        example_cr = CashRegister(50)
        self.assertItemsEqual(example_cr.items, [])
        self.assertEqual(example_cr.employee_discount, 50)
        example_cr.total = 40
        example_cr.items = [{"name": "ice cream", "price": 5.00}]
        example_cr.employee_discount = 10
        self.assertEqual(example_cr.total, 40)
        self.assertItemsEqual(example_cr.items, [{"name": "ice cream", "price": 5.00}])
        self.assertEqual(example_cr._employee_discount, 10)

    def test_add_item_method(self):
        example_cr = CashRegister()
        self.assertEqual(example_cr.add_item("ice cream", 5.00), 5.00)
        self.assertItemsEqual(example_cr.items, [{"name": "ice cream", "price": 5.00}])

    def test_apply_discount_method(self):
        example_cr = CashRegister(20)
        example_cr.total = 100
        self.assertEqual(example_cr.apply_discount(), 80)
        self.assertEqual(example_cr.total, 100)

    def test_item_names_method(self):
        example_cr = CashRegister()
        example_cr.add_item("ice cream", 5.00)
        example_cr.add_item("cereal", 10.00)
        example_cr.add_item("OJ", 4.00, 3)
        self.assertItemsEqual(example_cr.item_names(), ["ice cream", "cereal", "OJ", "OJ", "OJ"])

    def test_mean_item_price_method(self):
        example_cr = CashRegister()
        example_cr.add_item("ice cream", 5.00)
        example_cr.add_item("cereal", 10.00)
        example_cr.add_item("OJ", 4.00, 3)
        self.assertEqual(example_cr.mean_item_price(), 5.40)

    def test_median_item_price_odd_count_method(self):
        example_cr = CashRegister()
        example_cr.add_item("ice cream", 5.00)
        example_cr.add_item("cereal", 10.00)
        example_cr.add_item("OJ", 4.00, 3)
        self.assertEqual(example_cr.median_item_price(), 4.00)

    def test_median_item_price_even_count_method(self):
        example_cr_even_item_count = CashRegister()
        example_cr_even_item_count.add_item("ice cream", 5.00)
        example_cr_even_item_count.add_item("cereal", 10.00)
        example_cr_even_item_count.add_item("OJ", 4.00, 2)
        self.assertEqual(example_cr_even_item_count.median_item_price(), 4.50)
