pending_orders = [3, 4, 5, 6, 9]
delivered_orders = [1, 2, '32', 100, ]


def check_order_status(order_id):
    if order_id in delivered_orders:
        return True
    else:
        return False
    if order_id in pending_orders:
        return True
    else:
        return False


def check_id_is_integer(order_id):
    if not isinstance(order_id, int):
            raise TypeError('order_id has to be an integer')
    if order_id in delivered_orders:
        return True
    else:
        return False
    