import unittest
import shopping_cart

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = shopping_cart.ShoppingCart()

    
    def test_add_item(self):
        self.cart.add_item('Notebook', 10, 5)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0]['name'], 'Notebook')
        self.assertEqual(self.cart.items[0]['price'], 10)
        self.assertEqual(self.cart.items[0]['quantity'], 5)

        with self.assertRaises(ValueError) as context:
            self.cart.add_item('Notebook', 10, 0)
        self.assertEqual(str(context.exception), "Quantity must be greater than 0")



    def test_total_price(self):
        self.cart.add_item('Notebook', 10, 5)
        self.cart.add_item('Pen', 5, 5)
        total = self.cart.total_price()
        self.assertEqual(total, 75)

    

    def test_remove_item(self):
        self.cart.add_item('Notebook', 10, 5)
        self.cart.add_item('Pen', 5, 5)
        self.cart.remove_item('Pen')
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0]['name'], 'Notebook')



    def test_is_empty(self):
        self.assertTrue(self.cart.is_empty())
        self.cart.add_item('Notebook', 10, 5)
        self.assertFalse(self.cart.is_empty())



    def test_remove_nonexistent_item(self):
        self.cart.add_item('Notebook', 10, 5)
        self.cart.remove_item('Pen')
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0]['name'], 'Notebook')





if __name__ == '__main__':
    unittest.main()