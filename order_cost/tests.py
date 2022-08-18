from urllib import response
from django.test import TestCase 
from django.urls import reverse
from .order_handler import OrderHandler
import json
# A test suite in Django is 
# a collection of all the test cases in all the apps in your project
# Create your tests here.

class YourTestClass(TestCase):
    
    def setUp(self):
        self.handler = OrderHandler()
        self.data = {
            "order_items": [
                {
                "name": "bread",
                "quantity": 2,
                "price": 2200
                },
                {
                "name": "butter",
                "quantity": 1,
                "price": 5900
                }
                
            ],
            "offer": {
                "offer_type": "FLAT",
                "offer_val": 1000
            },
            "distance": 1200
        }
    def test_get_delivery_cost(self):
        self.assertEquals(5000, self.handler.get_delivery_cost(10))
        self.assertEquals(10000, self.handler.get_delivery_cost(20))
        self.assertEquals(50000, self.handler.get_delivery_cost(30)) 
    
    def test_get_items_value(self):
        cost = 10300
        self.assertEquals(cost, self.handler.get_items_value(self.data["order_items"]))
        
    def test_get_discount_value(self):
        
        delivery_cost = 100
        offer1 = {
           "offer_type": "FLAT",
            "offer_val": 1000
            }
        
        offer2 = {
           "offer_type": "DELIVERY"
            }

        self.assertEquals(offer1["offer_val"], self.handler.get_discount_value(offer1, delivery_cost))
        
        self.assertEquals(delivery_cost, self.handler.get_discount_value(offer2, delivery_cost))

    def test_calculate_order_value(self):
        
        offer1 = {
           "offer_type": "FLAT",
            "offer_val": 1000
            }
        offer2 = {
           "offer_type": "DELIVERY"
            }
        distance = 1200
        
        value1= 14300
        value2= 10300
        self.assertEquals(value1, self.handler.calculate_order_value(self.data["order_items"],distance,offer1))
        self.assertEquals(value2, self.handler.calculate_order_value(self.data["order_items"],distance,offer2))
            
            
    def test_get_order_value(self): 
         order_value = {
            'order_total' : 14300
         }
         self.assertEquals(order_value, self.handler.get_order_value(self.data))