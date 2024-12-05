from django.test import TestCase
from shop.models import Product, Purchase
from datetime import datetime

class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="book", price="740",
                               quantity="100", max_quantity="100")
        Product.objects.create(name="pencil", price="50",
                               quantity="100", max_quantity="100")

    def test_correctness_types(self):                   
        self.assertIsInstance(Product.objects.get(name="book").name, str)
        self.assertIsInstance(Product.objects.get(name="book").price, int)
        self.assertIsInstance(Product.objects.get(name="book").quantity, int)
        self.assertIsInstance(Product.objects.get(name="book").max_quantity, int)

        self.assertIsInstance(Product.objects.get(name="pencil").name, str)
        self.assertIsInstance(Product.objects.get(name="pencil").price, int)
        self.assertIsInstance(Product.objects.get(name="pencil").quantity, int)
        self.assertIsInstance(Product.objects.get(name="pencil").max_quantity, int)     

    def test_correctness_data(self):
        self.assertTrue(Product.objects.get(name="book").price == 740)
        self.assertTrue(Product.objects.get(name="book").quantity == 100)
        self.assertTrue(Product.objects.get(name="book").max_quantity == 100)
        self.assertTrue(Product.objects.get(name="pencil").price == 50)
        self.assertTrue(Product.objects.get(name="pencil").quantity == 100)
        self.assertTrue(Product.objects.get(name="pencil").max_quantity == 100)


class PurchaseTestCase(TestCase):
    def setUp(self):
        self.product_book = Product.objects.create(name="book", price="740",
                                                   quantity="100", max_quantity="100")
        self.datetime = datetime.now()
        Purchase.objects.create(product=self.product_book,
                                product_quantity="5",
                                person="Ivanov",
                                address="Svetlaya St.")

    def test_correctness_types(self):
        self.assertIsInstance(Purchase.objects.get(product=self.product_book).person, str)
        self.assertIsInstance(Purchase.objects.get(product=self.product_book).product_quantity, int)
        self.assertIsInstance(Purchase.objects.get(product=self.product_book).address, str)
        self.assertIsInstance(Purchase.objects.get(product=self.product_book).date, datetime)

    def test_correctness_data(self):
        self.assertTrue(Purchase.objects.get(product=self.product_book).person == "Ivanov")
        self.assertTrue(Purchase.objects.get(product=self.product_book).product_quantity == 5)
        self.assertTrue(Purchase.objects.get(product=self.product_book).address == "Svetlaya St.")
        self.assertTrue(Purchase.objects.get(product=self.product_book).date.replace(microsecond=0) == \
            self.datetime.replace(microsecond=0))