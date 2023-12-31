import pytest


pytestmark = pytest.mark.django_db


class TestCategoryModel:

    def test_string_method(self, category_factory):
        data = category_factory(name='test_cat')
        assert data.__str__() == 'test_cat'


class TestBrandModel:

    def test_string_method(self, brand_factory):
        data = brand_factory(name='test_brand')
        assert data.__str__() == 'test_brand'


class TestProductModel:

    def test_string_method(self, product_factory):
        data = product_factory(name='test_prod')
        assert data.__str__() == 'test_prod'
