import unittest
from order_verify import check_order_status, check_id_is_integer, delivered_orders


class TestOrder(unittest.TestCase):

    def test_order_status(self):
        self.assertEqual(check_order_status(2), True)
        self.assertFalse(check_order_status(9), False)

     
        # use assertFalse to test for an order still pending


    def test_check_id_is_integer(self):
        with self.assertRaises(TypeError):
            order_id = 'two'
            self.assertIsInstance(order_id, delivered_orders)
            self.assertFalse(check_id_is_integer(order_id), False)
    # test if the input is an integer

    # test for an order id that does not exist in both lists

    # test if there are orders added to the list

    # test for adding of a new order

    # test for marking an order delivered