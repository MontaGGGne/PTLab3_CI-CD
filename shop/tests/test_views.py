from datetime import datetime
from django.test import TestCase, Client
from shop.views import PurchaseCreate, Product, Purchase

class PurchaseCreateTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        
        self.product_book = Product.objects.create(name="book", price="1000",
                                                   quantity="100", max_quantity="100")
        self.datetime = datetime.now()
        Purchase.objects.create(product=self.product_book,
                                product_quantity="10",
                                person="Ivanov",
                                address="Svetlaya St.")

    def test_webpage_accessibility(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
    def test_correctness_data(self):
        PurchaseCreate.my_func(self, self.product_book, 10)
        print(f"quantity - {Product.objects.get(name=self.product_book.name).quantity}")
        self.assertTrue(Product.objects.get(name=self.product_book.name).quantity == 90)
        self.assertTrue(Product.objects.get(name=self.product_book.name).price == 1150)