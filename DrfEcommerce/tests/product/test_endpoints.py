import pytest


pytestmark = pytest.mark.django_db


class TestCategoryEndpoints:

    endpoint = '/api/category/'

    def test_category_get(self, category_factory, client):
        category_factory.create_batch(4)
        response = client.get(self.endpoint)
        assert response.status_code == 200
        assert len(response.data) == 4


class TestBrandEndpoints:
    endpoint = '/api/brand/'

    def test_brand_get(self, brand_factory, client):
        brand_factory.create_batch(4)
        response = client.get(self.endpoint)
        assert response.status_code == 200
        assert len(response.data) == 4


class TestProductEndpoints:
    endpoint = '/api/product/'

    def test_product_get(self, product_factory, client):
        product_factory()
        response = client.get(self.endpoint)
        assert response.status_code == 200
