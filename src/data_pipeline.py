import os
import pandas as pd
import numpy as np

directories = [
    r"e:\Experifo Labs\src",
    r"e:\Experifo Labs\src\dashboard",
    r"e:\Experifo Labs\screenshots",
    r"e:\Experifo Labs\submission",
    r"e:\Experifo Labs\submission\screenshots"
]

for directory in directories:
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created directory: {directory}")

raw_data = [
    {"restaurant_name": "The Crust Cafe", "cuisines": "Cafe, Desserts, Italian", "rating": 4.5, "number_of_reviews": 320, "cost_for_two": 500, "locality": "College Road", "delivery_time_mins": 25, "type": "Dine-In Restaurant"},
    {"restaurant_name": "Spicy Tadka", "cuisines": "North Indian, Punjabi, Chinese", "rating": 4.2, "number_of_reviews": 1100, "cost_for_two": 600, "locality": "College Road", "delivery_time_mins": 35, "type": "Dine-In Restaurant"},
    {"restaurant_name": "Biryani Durbar", "cuisines": "Mughlai, Biryani", "rating": 4.4, "number_of_reviews": 850, "cost_for_two": 400, "locality": "College Road", "delivery_time_mins": 20, "type": "Cloud Kitchen"},
    {"restaurant_name": "South Taste", "cuisines": "South Indian", "rating": 4.6, "number_of_reviews": 1450, "cost_for_two": 250, "locality": "College Road", "delivery_time_mins": 15, "type": "Dine-In Restaurant"},
    {"restaurant_name": "Wok & Roll", "cuisines": "Chinese, Asian", "rating": 4.1, "number_of_reviews": 430, "cost_for_two": 450, "locality": "College Road", "delivery_time_mins": 30, "type": "Dine-In Restaurant"},
    {"restaurant_name": "Burger Barn", "cuisines": "Fast Food, Burgers, Beverages", "rating": 4.3, "number_of_reviews": 670, "cost_for_two": 350, "locality": "College Road", "delivery_time_mins": 22, "type": "Dine-In Restaurant"},
    {"restaurant_name": "Behrouz Biryani", "cuisines": "Biryani, Mughlai", "rating": 4.4, "number_of_reviews": 510, "cost_for_two": 700, "locality": "College Road", "delivery_time_mins": 25, "type": "Cloud Kitchen"},
    {"restaurant_name": "Faasos", "cuisines": "Fast Food, Wraps, Rolls", "rating": 4.0, "number_of_reviews": 920, "cost_for_two": 300, "locality": "College Road", "delivery_time_mins": 18, "type": "Cloud Kitchen"},
    {"restaurant_name": "Oven Story Pizza", "cuisines": "Pizzas, Fast Food", "rating": 4.2, "number_of_reviews": 730, "cost_for_two": 600, "locality": "College Road", "delivery_time_mins": 28, "type": "Cloud Kitchen"},
    {"restaurant_name": "Sweet Truth", "cuisines": "Desserts, Bakery", "rating": 4.3, "number_of_reviews": 290, "cost_for_two": 250, "locality": "College Road", "delivery_time_mins": 20, "type": "Cloud Kitchen"},
    
    {"restaurant_name": "The Crust Cafe", "cuisines": "Cafe, Desserts, Italian", "rating": 4.5, "number_of_reviews": 320, "cost_for_two": 500, "locality": "College Road", "delivery_time_mins": 25, "type": "Dine-In Restaurant"},
    {"restaurant_name": "spicy tadka", "cuisines": "North Indian, Punjabi", "rating": 4.2, "number_of_reviews": 1100, "cost_for_two": 600, "locality": "College Road", "delivery_time_mins": 35, "type": "Dine-In Restaurant"},
    
    {"restaurant_name": "Chai Tapri", "cuisines": "Street Food, Beverages", "rating": None, "number_of_reviews": 45, "cost_for_two": 150, "locality": "College Road", "delivery_time_mins": 12, "type": "Dine-In Restaurant"},
    {"restaurant_name": "Mom's Kitchen", "cuisines": "North Indian, Home-style", "rating": 4.5, "number_of_reviews": 12, "cost_for_two": None, "locality": "College Road", "delivery_time_mins": 40, "type": "Cloud Kitchen"},
    {"restaurant_name": "Green Salad Co.", "cuisines": "Healthy Food, Salads", "rating": 3.9, "number_of_reviews": None, "cost_for_two": 400, "locality": "College Road", "delivery_time_mins": 30, "type": "Cloud Kitchen"},
    {"restaurant_name": "Nashik Misal House", "cuisines": "Maharashtrian, Street Food", "rating": 4.7, "number_of_reviews": 2300, "cost_for_two": 200, "locality": "College Road", "delivery_time_mins": 18, "type": "Dine-In Restaurant"},
    {"restaurant_name": "Hotel Panchavati Pride", "cuisines": "North Indian, South Indian, Chinese", "rating": 3.8, "number_of_reviews": 180, "cost_for_two": 550, "locality": "College Road", "delivery_time_mins": 32, "type": "Dine-In Restaurant"},
    {"restaurant_name": "The Belgian Waffle Co.", "cuisines": "Desserts, Waffles", "rating": 4.5, "number_of_reviews": 480, "cost_for_two": 300, "locality": "College Road", "delivery_time_mins": 22, "type": "Dine-In Restaurant"},
    {"restaurant_name": "Pizza Hut", "cuisines": "Pizzas, Fast Food, Italian", "rating": 3.9, "number_of_reviews": 1200, "cost_for_two": 600, "locality": "College Road", "delivery_time_mins": 35, "type": "Dine-In Restaurant"},
    {"restaurant_name": "Subway", "cuisines": "Healthy Food, Fast Food, Salads", "rating": 4.1, "number_of_reviews": 850, "cost_for_two": 350, "locality": "College Road", "delivery_time_mins": 20, "type": "Dine-In Restaurant"},
    
    {"restaurant_name": "The Good Bowl", "cuisines": "healthy food, bowls", "rating": 4.2, "number_of_reviews": 150, "cost_for_two": 300, "locality": "College Road", "delivery_time_mins": 25, "type": "Cloud Kitchen"},
    {"restaurant_name": "Firangi Bake", "cuisines": "Italian, Mexican, Fast Food", "rating": 4.0, "number_of_reviews": 85, "cost_for_two": 400, "locality": "College Road", "delivery_time_mins": 28, "type": "Cloud Kitchen"},
    {"restaurant_name": "Mandarin Oak", "cuisines": "Chinese, Asian", "rating": 4.1, "number_of_reviews": 210, "cost_for_two": 500, "locality": "College Road", "delivery_time_mins": 25, "type": "Cloud Kitchen"},
    {"restaurant_name": "Sardarji Da Dhaba", "cuisines": "north indian, punjabi", "rating": 4.3, "number_of_reviews": 640, "cost_for_two": 500, "locality": "College Road", "delivery_time_mins": 35, "type": "Dine-In Restaurant"},
    {"restaurant_name": "Saffron Biryani House", "cuisines": "Biryani, North Indian", "rating": None, "number_of_reviews": 120, "cost_for_two": 350, "locality": "College Road", "delivery_time_mins": 25, "type": "Unknown"},
    {"restaurant_name": "Cafe Coffee Day", "cuisines": "cafe, fast food", "rating": 4.0, "number_of_reviews": 450, "cost_for_two": None, "locality": "College Road", "delivery_time_mins": 20, "type": "Dine-In Restaurant"},
    {"restaurant_name": "Rolls Mania", "cuisines": "Fast Food, Rolls", "rating": 4.2, "number_of_reviews": 560, "cost_for_two": 250, "locality": "College Road", "delivery_time_mins": 18, "type": "Dine-In Restaurant"},
    {"restaurant_name": "Kwality Walls Swirls", "cuisines": "Ice Cream, Desserts", "rating": 4.4, "number_of_reviews": 190, "cost_for_two": 200, "locality": "College Road", "delivery_time_mins": 15, "type": "Dine-In Restaurant"},
    {"restaurant_name": "Temptations", "cuisines": "Cafe, Fast Food, Desserts", "rating": 4.3, "number_of_reviews": 820, "cost_for_two": 400, "locality": "College Road", "delivery_time_mins": 22, "type": "Dine-In Restaurant"},
    {"restaurant_name": "Shree Leela Sandwich", "cuisines": "Street Food, Fast Food", "rating": 4.5, "number_of_reviews": 980, "cost_for_two": 150, "locality": "College Road", "delivery_time_mins": 15, "type": "Dine-In Restaurant"},
    {"restaurant_name": "Noodle Bar", "cuisines": "Chinese, Thai", "rating": 4.0, "number_of_reviews": 110, "cost_for_two": 450, "locality": "College Road", "delivery_time_mins": 30, "type": "Unknown"},
    {"restaurant_name": "Amrut Tandoor", "cuisines": "North Indian, Tandoori", "rating": 4.3, "number_of_reviews": 310, "cost_for_two": 350, "locality": "College Road", "delivery_time_mins": 28, "type": "Dine-In Restaurant"},
    {"restaurant_name": "Dessert Heaven", "cuisines": "desserts, bakery", "rating": 4.2, "number_of_reviews": 75, "cost_for_two": 300, "locality": "College Road", "delivery_time_mins": 20, "type": "Cloud Kitchen"},
    {"restaurant_name": "KFC", "cuisines": "Fast Food, Burgers", "rating": 4.1, "number_of_reviews": 1400, "cost_for_two": 500, "locality": "College Road", "delivery_time_mins": 20, "type": "Dine-In Restaurant"},
    {"restaurant_name": "The Biryani Life", "cuisines": "Biryani", "rating": 3.9, "number_of_reviews": 95, "cost_for_two": 300, "locality": "College Road", "delivery_time_mins": 24, "type": "Cloud Kitchen"},
    {"restaurant_name": "Starbucks", "cuisines": "Cafe, Beverages", "rating": 4.4, "number_of_reviews": 380, "cost_for_two": 700, "locality": "College Road", "delivery_time_mins": 20, "type": "Dine-In Restaurant"},
    {"restaurant_name": "Shreeji Chaat Center", "cuisines": "Street Food, Chaat", "rating": 4.6, "number_of_reviews": 1250, "cost_for_two": 150, "locality": "College Road", "delivery_time_mins": 15, "type": "Dine-In Restaurant"}
]

df_raw = pd.DataFrame(raw_data)
df_raw.to_csv(r"e:\Experifo Labs\submission\raw_restaurants.csv", index=False)
df_raw.to_csv(r"e:\Experifo Labs\raw_restaurants.csv", index=False)
print(f"Raw dataset saved! Records: {len(df_raw)}")

print("Starting Data Cleaning Pipeline...")

df_cleaned = df_raw.copy()
df_cleaned['temp_name'] = df_cleaned['restaurant_name'].str.strip().str.lower()
before_records = len(df_cleaned)

df_cleaned = df_cleaned.drop_duplicates(subset=['temp_name', 'locality'], keep='first')
df_cleaned = df_cleaned.drop(columns=['temp_name'])
after_duplicates = len(df_cleaned)
print(f"Removed {before_records - after_duplicates} duplicate records.")

median_rating = round(df_cleaned['rating'].median(), 1)
df_cleaned['rating'] = df_cleaned['rating'].fillna(median_rating)

median_cost = int(df_cleaned['cost_for_two'].median())
df_cleaned['cost_for_two'] = df_cleaned['cost_for_two'].fillna(median_cost).astype(int)

df_cleaned['number_of_reviews'] = df_cleaned['number_of_reviews'].fillna(0).astype(int)
print(f"Imputed missing values (Rating: {median_rating}, Cost For Two: {median_cost}, Reviews: 0).")

def normalize_cuisines(cuisine_str):
    if not isinstance(cuisine_str, str):
        return ""
    items = [item.strip().title() for item in cuisine_str.split(',')]
    return ", ".join(items)

df_cleaned['cuisines'] = df_cleaned['cuisines'].apply(normalize_cuisines)
print("Normalized cuisine names to standard Title Case format.")

def infer_type(row):
    r_type = row['type']
    name = row['restaurant_name'].lower()
    if r_type == 'Unknown' or pd.isnull(r_type):
        if 'biryani' in name or 'kitchen' in name or 'cloud' in name or 'delivery' in name:
            return 'Cloud Kitchen'
        else:
            return 'Dine-In Restaurant'
    return r_type

df_cleaned['type'] = df_cleaned.apply(infer_type, axis=1)

df_cleaned.to_csv(r"e:\Experifo Labs\submission\cleaned_restaurants.csv", index=False)
df_cleaned.to_csv(r"e:\Experifo Labs\cleaned_restaurants.csv", index=False)
print(f"Cleaned dataset saved! Final records: {len(df_cleaned)}")

print("Generating Structured Menu Dataset for 5 Restaurants...")

menu_data = []

crust_cafe_items = [
    {"item_name": "Truffle Mushroom Risotto", "category": "Mains", "price": 420, "is_bestseller": False},
    {"item_name": "Classic Alfredo Pasta", "category": "Mains", "price": 350, "is_bestseller": True},
    {"item_name": "Peri Peri Paneer Flatbread", "category": "Appetizers", "price": 280, "is_bestseller": False},
    {"item_name": "Nutella Cheesecake", "category": "Desserts", "price": 250, "is_bestseller": True},
    {"item_name": "Cafe Latte", "category": "Beverages", "price": 180, "is_bestseller": False},
    {"item_name": "Iced Peach Tea", "category": "Beverages", "price": 150, "is_bestseller": False},
    {"item_name": "Garlic Bread with Cheese", "category": "Appetizers", "price": 190, "is_bestseller": False},
    {"item_name": "Warm Chocolate Fudge Brownie", "category": "Desserts", "price": 220, "is_bestseller": False},
    {"item_name": "Avocado Sourdough Toast", "category": "Appetizers", "price": 310, "is_bestseller": True},
    {"item_name": "Watermelon Mint Cooler", "category": "Beverages", "price": 160, "is_bestseller": False}
]

spicy_tadka_items = [
    {"item_name": "Paneer Butter Masala", "category": "Mains", "price": 280, "is_bestseller": True},
    {"item_name": "Veg Diwani Handi", "category": "Mains", "price": 260, "is_bestseller": False},
    {"item_name": "Dal Makhani", "category": "Mains", "price": 240, "is_bestseller": True},
    {"item_name": "Butter Naan", "category": "Breads", "price": 60, "is_bestseller": False},
    {"item_name": "Tandoori Roti", "category": "Breads", "price": 30, "is_bestseller": False},
    {"item_name": "Hara Bhara Kabab", "category": "Starters", "price": 220, "is_bestseller": False},
    {"item_name": "Veg Manchurian Wet", "category": "Chinese", "price": 240, "is_bestseller": False},
    {"item_name": "Jeera Rice", "category": "Rice", "price": 160, "is_bestseller": False},
    {"item_name": "Gulab Jamun (2 Pcs)", "category": "Desserts", "price": 80, "is_bestseller": False},
    {"item_name": "Paneer Tikka Masala", "category": "Mains", "price": 290, "is_bestseller": True}
]

biryani_durbar_items = [
    {"item_name": "Premium Veg Dum Biryani (Serves 1-2)", "category": "Biryani", "price": 290, "is_bestseller": True},
    {"item_name": "Paneer Tikka Biryani (Serves 1-2)", "category": "Biryani", "price": 320, "is_bestseller": True},
    {"item_name": "Subz-E-Biryani (Serves 1)", "category": "Biryani", "price": 220, "is_bestseller": False},
    {"item_name": "Soya Chaap Biryani", "category": "Biryani", "price": 260, "is_bestseller": False},
    {"item_name": "Paneer Lasooni Tikka Starter", "category": "Starters", "price": 240, "is_bestseller": False},
    {"item_name": "Veg Galouti Kabab", "category": "Starters", "price": 210, "is_bestseller": False},
    {"item_name": "Double Ka Meetha", "category": "Desserts", "price": 120, "is_bestseller": False},
    {"item_name": "Shahi Phirni", "category": "Desserts", "price": 110, "is_bestseller": True},
    {"item_name": "Mirchi Ka Salan (Extra)", "category": "Sides", "price": 40, "is_bestseller": False},
    {"item_name": "Garlic Mint Raita", "category": "Sides", "price": 30, "is_bestseller": False}
]

south_taste_items = [
    {"item_name": "Special Butter Masala Dosa", "category": "Dosa", "price": 120, "is_bestseller": True},
    {"item_name": "Cheese Mysore Masala Dosa", "category": "Dosa", "price": 150, "is_bestseller": True},
    {"item_name": "Steamed Idli (2 Pcs)", "category": "Idli & Vada", "price": 60, "is_bestseller": False},
    {"item_name": "Medu Vada (2 Pcs)", "category": "Idli & Vada", "price": 70, "is_bestseller": True},
    {"item_name": "Onion Tomato Uttapam", "category": "Uttapam", "price": 110, "is_bestseller": False},
    {"item_name": "Filter Coffee", "category": "Beverages", "price": 50, "is_bestseller": True},
    {"item_name": "Upma", "category": "Snacks", "price": 60, "is_bestseller": False},
    {"item_name": "Sheera", "category": "Snacks", "price": 60, "is_bestseller": False},
    {"item_name": "Rava Masala Dosa", "category": "Dosa", "price": 130, "is_bestseller": False},
    {"item_name": "South Taste Thali", "category": "Meals", "price": 180, "is_bestseller": False}
]

wok_roll_items = [
    {"item_name": "Veg Hakka Noodles", "category": "Noodles", "price": 200, "is_bestseller": True},
    {"item_name": "Schezwan Fried Rice", "category": "Rice", "price": 210, "is_bestseller": True},
    {"item_name": "Veg Manchurian Gravy", "category": "Mains", "price": 220, "is_bestseller": True},
    {"item_name": "Paneer Chilli Dry", "category": "Starters", "price": 240, "is_bestseller": True},
    {"item_name": "Spring Rolls Veg (6 Pcs)", "category": "Starters", "price": 180, "is_bestseller": False},
    {"item_name": "Triple Schezwan Rice", "category": "Rice & Noodles", "price": 270, "is_bestseller": True},
    {"item_name": "Manchow Soup", "category": "Soups", "price": 120, "is_bestseller": False},
    {"item_name": "Hot & Sour Soup", "category": "Soups", "price": 120, "is_bestseller": False},
    {"item_name": "Honey Chilli Potato", "category": "Starters", "price": 190, "is_bestseller": False},
    {"item_name": "Fried Ice Cream", "category": "Desserts", "price": 160, "is_bestseller": False}
]

restaurants_map = {
    "The Crust Cafe": crust_cafe_items,
    "Spicy Tadka": spicy_tadka_items,
    "Biryani Durbar": biryani_durbar_items,
    "South Taste": south_taste_items,
    "Wok & Roll": wok_roll_items
}

for restaurant, items in restaurants_map.items():
    for item in items:
        menu_entry = {
            "restaurant_name": restaurant,
            "item_name": item["item_name"],
            "category": item["category"],
            "price": item["price"],
            "is_bestseller": item["is_bestseller"]
        }
        menu_data.append(menu_entry)

df_menu = pd.DataFrame(menu_data)
df_menu.to_csv(r"e:\Experifo Labs\submission\menu_dataset.csv", index=False)
df_menu.to_csv(r"e:\Experifo Labs\menu_dataset.csv", index=False)
print(f"Menu dataset saved! Total menu items: {len(df_menu)}")

print("Pipeline executed successfully!")
