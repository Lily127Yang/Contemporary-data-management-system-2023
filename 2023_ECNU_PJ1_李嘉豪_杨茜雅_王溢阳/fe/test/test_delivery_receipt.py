import pytest
from fe.access.new_buyer import register_new_buyer
import uuid
from fe.test.gen_book_data import GenBook
from fe.access import operations
import fe.conf as conf
from be.model import operations as direct_operations

class TestDeliveryReceipt:
    @pytest.fixture(autouse=True)
    def pre_run_initialization(self):
        self.opera = operations.Operations(conf.URL)
        self.seller_id = "test_operations_seller_{}".format(str(uuid.uuid1()))
        self.buyer_id = "test_operations_buyer_{}".format(str(uuid.uuid1()))
        self.store_id = "test_operations_store_{}".format(str(uuid.uuid1()))
        self.seller_password = self.seller_id
        self.buyer_password = self.buyer_id
        self.buyer = register_new_buyer(self.buyer_id, self.buyer_password)
        self.d_op = direct_operations.Operations()
        yield

    def test_set_delivery_ok(self):
        gen_book = GenBook(self.seller_id, self.store_id)
        ok, buy_book_id_list = gen_book.gen(
            non_exist_book_id=False, low_stock_level=False
        )
        assert ok
        buy_book_info_list = gen_book.buy_book_info_list
        code, order_id = self.buyer.new_order(self.store_id, buy_book_id_list)
        assert code == 200
        # 至此应该已经完成了下单操作
        total_price = 0
        for item in buy_book_info_list:
            book = item[0]
            num = item[1]
            total_price = total_price + book.price * num
        code = self.buyer.add_funds(total_price)
        assert code == 200
        code = self.buyer.payment(order_id)
        assert code == 200
        # 至此完成了购买操作
        code = self.opera.set_delivery(order_id, self.store_id, self.seller_id, self.seller_password)
        assert code == 200

    def test_set_delivery_directly_ok(self):
        gen_book = GenBook(self.seller_id, self.store_id)
        ok, buy_book_id_list = gen_book.gen(
            non_exist_book_id=False, low_stock_level=False
        )
        assert ok
        buy_book_info_list = gen_book.buy_book_info_list
        code, order_id = self.buyer.new_order(self.store_id, buy_book_id_list)
        assert code == 200
        # 至此应该已经完成了下单操作
        total_price = 0
        for item in buy_book_info_list:
            book = item[0]
            num = item[1]
            total_price = total_price + book.price * num
        code = self.buyer.add_funds(total_price)
        assert code == 200
        code = self.buyer.payment(order_id)
        assert code == 200
        # 至此完成了购买操作
        code, _ = self.d_op.delivery(order_id, self.store_id, self.seller_id, self.seller_password)
        assert code == 200

    def test_set_receipt_ok(self):
        gen_book = GenBook(self.seller_id, self.store_id)
        ok, buy_book_id_list = gen_book.gen(
            non_exist_book_id=False, low_stock_level=False
        )
        assert ok
        buy_book_info_list = gen_book.buy_book_info_list
        code, order_id = self.buyer.new_order(self.store_id, buy_book_id_list)
        assert code == 200
        # 至此应该已经完成了下单操作
        total_price = 0
        for item in buy_book_info_list:
            book = item[0]
            num = item[1]
            total_price = total_price + book.price * num
        code = self.buyer.add_funds(total_price)
        assert code == 200
        code = self.buyer.payment(order_id)
        assert code == 200
        # 至此完成了购买操作
        code = self.opera.set_delivery(order_id, self.store_id, self.seller_id, self.seller_password)
        assert code == 200
        code = self.opera.set_receipt(order_id, self.buyer_id, self.buyer_password)
        assert code == 200
    
    def test_set_receipt_directly_ok(self):
        gen_book = GenBook(self.seller_id, self.store_id)
        ok, buy_book_id_list = gen_book.gen(
            non_exist_book_id=False, low_stock_level=False
        )
        assert ok
        buy_book_info_list = gen_book.buy_book_info_list
        code, order_id = self.buyer.new_order(self.store_id, buy_book_id_list)
        assert code == 200
        # 至此应该已经完成了下单操作
        total_price = 0
        for item in buy_book_info_list:
            book = item[0]
            num = item[1]
            total_price = total_price + book.price * num
        code = self.buyer.add_funds(total_price)
        assert code == 200
        code = self.buyer.payment(order_id)
        assert code == 200
        # 至此完成了购买操作
        code, _ = self.d_op.delivery(order_id, self.store_id, self.seller_id, self.seller_password)
        assert code == 200
        code, _ = self.d_op.receipt(order_id, self.buyer_id, self.buyer_password)
        assert code == 200


    def test_set_delivery_before_payment(self):
        gen_book = GenBook(self.seller_id, self.store_id)
        ok, buy_book_id_list = gen_book.gen(
            non_exist_book_id=False, low_stock_level=False
        )
        assert ok
        code, order_id = self.buyer.new_order(self.store_id, buy_book_id_list)
        assert code == 200
        # 至此应该已经完成了下单操作
        code = self.opera.set_delivery(order_id, self.store_id, self.seller_id, self.seller_password)
        assert code != 200

    def test_set_delivery_before_payment_directly(self):
        gen_book = GenBook(self.seller_id, self.store_id)
        ok, buy_book_id_list = gen_book.gen(
            non_exist_book_id=False, low_stock_level=False
        )
        assert ok
        code, order_id = self.buyer.new_order(self.store_id, buy_book_id_list)
        assert code == 200
        # 至此应该已经完成了下单操作
        code, _ = self.d_op.delivery(order_id, self.store_id, self.seller_id, self.seller_password)
        assert code != 200

    def test_set_receipt_before_payment(self):
        gen_book = GenBook(self.seller_id, self.store_id)
        ok, buy_book_id_list = gen_book.gen(
            non_exist_book_id=False, low_stock_level=False
        )
        assert ok
        code, order_id = self.buyer.new_order(self.store_id, buy_book_id_list)
        assert code == 200
        # 至此应该已经完成了下单操作
        code = self.opera.set_receipt(order_id, self.buyer_id, self.buyer_password)
        assert code != 200
    
    def test_set_receipt_before_payment_directly(self):
        gen_book = GenBook(self.seller_id, self.store_id)
        ok, buy_book_id_list = gen_book.gen(
            non_exist_book_id=False, low_stock_level=False
        )
        assert ok
        code, order_id = self.buyer.new_order(self.store_id, buy_book_id_list)
        assert code == 200
        # 至此应该已经完成了下单操作
        code, _ = self.d_op.receipt(order_id, self.buyer_id, self.buyer_password)
        assert code != 200