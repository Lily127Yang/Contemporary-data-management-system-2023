import pytest
from fe.access.new_buyer import register_new_buyer
import uuid
from fe.test.gen_book_data import GenBook
from fe.access import operations
import fe.conf as conf
from be.model import operations as direct_operations

class TestRecommend:
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

    def test_recommend_ok(self):
        gen_book = GenBook(self.seller_id, self.store_id)
        ok, buy_book_id_list = gen_book.gen(
            non_exist_book_id=False, low_stock_level=False
        )
        assert ok
        _ = gen_book.buy_book_info_list
        code, _ = self.buyer.new_order(self.store_id, buy_book_id_list)
        assert code == 200
        code = self.opera.book_recommend(self.buyer_id, self.buyer_password)
        assert code == 200

    def test_recommend_ok_directly(self):
        gen_book = GenBook(self.seller_id, self.store_id)
        ok, buy_book_id_list = gen_book.gen(
            non_exist_book_id=False, low_stock_level=False
        )
        assert ok
        _ = gen_book.buy_book_info_list
        code, _ = self.buyer.new_order(self.store_id, buy_book_id_list)
        assert code == 200
        code, _ = self.d_op.recommend(self.buyer_id, self.buyer_password)
        assert code == 200

    def test_recommend_authorization_fail(self):
        gen_book = GenBook(self.seller_id, self.store_id)
        ok, buy_book_id_list = gen_book.gen(
            non_exist_book_id=False, low_stock_level=False
        )
        assert ok
        _ = gen_book.buy_book_info_list
        code, _ = self.buyer.new_order(self.store_id, buy_book_id_list)
        assert code == 200
        code = self.opera.book_recommend(self.buyer_id, self.buyer_password + "_x")
        assert code == 401
        code = self.opera.book_recommend(self.buyer_id + "_x", self.buyer_password)
        assert code == 401

    def test_recommend_authorization_fail_directly(self):
        gen_book = GenBook(self.seller_id, self.store_id)
        ok, buy_book_id_list = gen_book.gen(
            non_exist_book_id=False, low_stock_level=False
        )
        assert ok
        _ = gen_book.buy_book_info_list
        code, _ = self.buyer.new_order(self.store_id, buy_book_id_list)
        assert code == 200
        code, _ = self.d_op.recommend(self.buyer_id, self.buyer_password + "_x")
        assert code == 401
        code, _ = self.d_op.recommend(self.buyer_id + "_x", self.buyer_password)
        assert code == 401
    
    def test_recommend_no_order_fail(self):
        new_buyer_id = new_buyer_password = "test_operations_buyer_{}".format(str(uuid.uuid1()))
        buyer = register_new_buyer(new_buyer_id, new_buyer_password)
        code = self.opera.book_recommend(new_buyer_id, new_buyer_password)
        assert code == 940
        code = self.opera.book_recommend(new_buyer_id, new_buyer_password)
        assert code == 940

    def test_recommend_no_order_fail_directly(self):
        new_buyer_id = new_buyer_password = "test_operations_buyer_{}".format(str(uuid.uuid1()))
        buyer = register_new_buyer(new_buyer_id, new_buyer_password)
        code, _ = self.d_op.recommend(new_buyer_id, new_buyer_password)
        assert code == 940
        code, _ = self.d_op.recommend(new_buyer_id, new_buyer_password)
        assert code == 940