import pytest
from fe.access.new_buyer import register_new_buyer
from fe.access.new_seller import register_new_seller
import uuid
from fe.test.gen_book_data import GenBook
from fe.access import operations
import fe.conf as conf
from be.model import operations as direct_operations
from fe.access import seller
import json
from fe.access import book


class TestSearchBook:
    @pytest.fixture(autouse=True)
    def pre_run_initialization(self):
        self.opera = operations.Operations(conf.URL)
        self.user_id = "test_operations_store_user_{}".format(str(uuid.uuid1()))
        self.seller_id = "test_operations_seller_{}".format(str(uuid.uuid1()))
        self.buyer_id = "test_operations_buyer_{}".format(str(uuid.uuid1()))
        self.store_id = "test_operations_store_{}".format(str(uuid.uuid1()))
        self.seller_password = self.seller_id
        self.buyer_password = self.buyer_id
        self.user_password = self.user_id
        self.buyer = register_new_buyer(self.buyer_id, self.buyer_password)
        self.d_op = direct_operations.Operations()
        self.seller = register_new_seller(self.user_id, self.user_password)
        self.exist_store_id = "111"
        self.seller.create_store(self.exist_store_id)
        book_db = book.BookDB()
        self.books = book_db.get_book_info(0, 2)
        for b in self.books:
            self.seller.add_book(self.exist_store_id, 0, b)
        yield
        # do after test

    def search_books(self, keyword, how="global_search", store_id=None):
        if how == "local_search" and not store_id:
            return 916
        return self.opera.book_search(keyword, how, store_id if how == "local_search" else None)

    def test_global_search(self):
        """Test for global search functionality."""
        # 全局搜索关键词“三毛”
        keyword = "三毛"
        code = self.search_books(keyword)
        assert code == 200, f"Expected 200, but got {code}"
        code, book_list = self.d_op.global_search(keyword)
        assert code == 200, f"Expected 200, but got {code}"

        # 全局搜索不存在的关键词“**”
        keyword = "**"
        code = self.search_books(keyword)
        assert code == 915, f"Expected 200, but got {code}"
        code, book_list = self.d_op.global_search(keyword)
        assert code == 915, f"Expected 200, but got {code}"

        # 全局搜索但是不输入关键词
        keyword = ""
        code, book_list = self.d_op.global_search(keyword)
        assert code == 914, f"Expected not 200 for empty keyword, but got {code}"
        code = self.search_books(keyword)
        assert code == 914, f"Expected not 200 for empty keyword, but got {code}"

    def test_local_search(self):
        """Test for local search functionality."""
        keyword = "三毛"
        code = self.search_books(keyword, how="local_search", store_id=self.store_id)
        assert code == 200, f"Expected 200, but got {code}"
        code, book_list = self.d_op.local_search(keyword, store_id=self.exist_store_id)
        assert code == 200, f"Expected 200, but got {code}"

        code, book_list = self.d_op.local_search(keyword, store_id=None)
        assert code == 916, f"Expected 200, but got {code}"
        code = self.search_books(keyword, how="local_search", store_id=None)
        assert code == 916, f"Expected 200, but got {code}"

        keyword = "不存在的书籍"
        code, book_list = self.d_op.local_search(keyword, store_id=self.exist_store_id)
        assert code == 915, f"Expected 200, but got {code}"
        code = self.search_books(keyword, how="local_search", store_id=self.exist_store_id)
        assert code == 915, f"Expected 200, but got {code}"

        keyword = ""
        code, book_list = self.d_op.local_search(keyword, store_id=self.exist_store_id)
        assert code == 914, f"Expected 200, but got {code}"
        code = self.search_books(keyword, how="local_search", store_id=self.store_id)
        assert code == 914, f"Expected 200, but got {code}"


