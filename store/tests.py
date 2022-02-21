from django.test import TestCase
from store.models.customer import Customer
from store.models.category import Category

# Create your tests here.

class BasicTest(TestCase):
    def test_fields(self):
        customer = Customer()
        customer.first_name = "Rastra"
        customer.last_name = "Karki"
        customer.phone = "9860009091"
        customer.email = "rastradhoj@gmail.com"
        customer.password = "12345678"
        customer.save()
        
        check = Customer.objects.get(id=1)
        self.assertEqual(check, customer)
        
    def test_category(self):
        category = Category()
        category.name = "Clothing - Men"
        category.save()
        
        record = Category.objects.get(id=1)
        self.assertEqual(record, category)
