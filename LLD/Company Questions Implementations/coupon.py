Coupons = [
    {"CategoryName": "Comforter Sets", "CouponName": "Comforters Sale", "DateModified": "2020-01-01", "Discount": "10%"},
    {"CategoryName": "Comforter Sets", "CouponName": "Cozy Comforter Coupon", "DateModified": "2020-01-01", "Discount": "$15"},
    {"CategoryName": "Bedding", "CouponName": "Best Bedding Bargains", "DateModified": "2019-01-01", "Discount": "35%"},
    {"CategoryName": "Bedding", "CouponName": "Savings on Bedding", "DateModified": "2019-01-01", "Discount": "25%"},
    {"CategoryName": "Bed & Bath", "CouponName": "Low price for Bed & Bath", "DateModified": "2018-01-01", "Discount": "50%"},
    {"CategoryName": "Bed & Bath", "CouponName": "Bed & Bath extravaganza", "DateModified": "2019-01-01", "Discount": "75%"}
]

categories = [
    {"CategoryName": "Comforter Sets", "CategoryParentName": "Bedding"},
    {"CategoryName": "Bedding", "CategoryParentName": "Bed & Bath"},
    {"CategoryName": "Bed & Bath", "CategoryParentName": "None"},
    {"CategoryName": "Soap Dispensers", "CategoryParentName": "Bathroom Accessories"},
    {"CategoryName": "Bathroom Accessories", "CategoryParentName": "Bed & Bath"},
    {"CategoryName": "Toy Organizers", "CategoryParentName": "Baby And Kids"},
    {"CategoryName": "Baby And Kids", "CategoryParentName": "None"}
]

products = [
    {"ProductName": "Cozy Comforter Sets", "Price": 100.00, "CategoryName": "Comforter Sets"},
    {"ProductName": "All-in-one Bedding Set", "Price": 50.00, "CategoryName": "Bedding"},
    {"ProductName": "Infinite Soap Dispenser", "Price": 500.00, "CategoryName": "Bathroom Accessories"},
    {"ProductName": "Rainbow Toy Box", "Price": 257.00, "CategoryName": "Baby And Kids"}
]


from collections import defaultdict
from enum import Enum
import json

class Discount_types(Enum):
    PERCENTAGE = 1
    ABSOLUTE = 2

category_to_coupon_map = defaultdict(list)
distinct_categories = set()

class Coupon:
    def __init__(self, category_name, coupon_name, date_modified, discount):
        self.category_name = category_name
        self.coupon_name = coupon_name
        self.date_modified = date_modified
        self.discount = discount

class Category:
    def __init__(self, category, parent_category):
        self.category = category
        self.parent_category = parent_category        

for coupon in Coupons:
    category_to_coupon_map[coupon["CategoryName"]].append(coupon)

cached_category_objects = {}

# create graph
for category in categories:
    if category["CategoryParentName"] not in cached_category_objects:
        cached_category_objects[category["CategoryParentName"]] = Category(category["CategoryParentName"], None)
    if category["CategoryName"] not in cached_category_objects:
        cached_category_objects[category["CategoryName"]] = Category(category["CategoryName"], None)
    cached_category_objects[category["CategoryName"]].parent_category = cached_category_objects[category["CategoryParentName"]]
    distinct_categories.add(category["CategoryName"])

def get_closest_parent_coupons(category):
    if category == "None":
        return None
    if category in category_to_coupon_map:
        return category_to_coupon_map[category]
    else:
        current_category_object = cached_category_objects[category]
        parent_object = current_category_object.parent_category
        category_to_coupon_map[category] = get_closest_parent_coupons(parent_object.category)
        return category_to_coupon_map[category]

# pre_process all categories
for category in distinct_categories:
    category_to_coupon_map[category] = get_closest_parent_coupons(category)

print(json.dumps(category_to_coupon_map, indent = 4))
