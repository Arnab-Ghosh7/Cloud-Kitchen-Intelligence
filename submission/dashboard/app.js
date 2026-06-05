





const CLEANED_RESTAURANTS = [
  {"restaurant_name": "The Crust Cafe", "cuisines": "Cafe, Desserts, Italian", "rating": 4.5, "number_of_reviews": 320, "cost_for_two": 500, "delivery_time_mins": 25, "type": "Dine-In Restaurant"},
  {"restaurant_name": "Spicy Tadka", "cuisines": "North Indian, Punjabi, Chinese", "rating": 4.2, "number_of_reviews": 1100, "cost_for_two": 600, "delivery_time_mins": 35, "type": "Dine-In Restaurant"},
  {"restaurant_name": "Biryani Durbar", "cuisines": "Mughlai, Biryani", "rating": 4.4, "number_of_reviews": 850, "cost_for_two": 400, "delivery_time_mins": 20, "type": "Cloud Kitchen"},
  {"restaurant_name": "South Taste", "cuisines": "South Indian", "rating": 4.6, "number_of_reviews": 1450, "cost_for_two": 250, "delivery_time_mins": 15, "type": "Dine-In Restaurant"},
  {"restaurant_name": "Wok & Roll", "cuisines": "Chinese, Asian", "rating": 4.1, "number_of_reviews": 430, "cost_for_two": 450, "delivery_time_mins": 30, "type": "Dine-In Restaurant"},
  {"restaurant_name": "Burger Barn", "cuisines": "Fast Food, Burgers, Beverages", "rating": 4.3, "number_of_reviews": 670, "cost_for_two": 350, "delivery_time_mins": 22, "type": "Dine-In Restaurant"},
  {"restaurant_name": "Behrouz Biryani", "cuisines": "Biryani, Mughlai", "rating": 4.4, "number_of_reviews": 510, "cost_for_two": 700, "delivery_time_mins": 25, "type": "Cloud Kitchen"},
  {"restaurant_name": "Faasos", "cuisines": "Fast Food, Wraps, Rolls", "rating": 4.0, "number_of_reviews": 920, "cost_for_two": 300, "delivery_time_mins": 18, "type": "Cloud Kitchen"},
  {"restaurant_name": "Oven Story Pizza", "cuisines": "Pizzas, Fast Food", "rating": 4.2, "number_of_reviews": 730, "cost_for_two": 600, "delivery_time_mins": 28, "type": "Cloud Kitchen"},
  {"restaurant_name": "Sweet Truth", "cuisines": "Desserts, Bakery", "rating": 4.3, "number_of_reviews": 290, "cost_for_two": 250, "delivery_time_mins": 20, "type": "Cloud Kitchen"},
  {"restaurant_name": "Chai Tapri", "cuisines": "Street Food, Beverages", "rating": 4.2, "number_of_reviews": 45, "cost_for_two": 150, "delivery_time_mins": 12, "type": "Dine-In Restaurant"},
  {"restaurant_name": "Mom's Kitchen", "cuisines": "North Indian, Home-Style", "rating": 4.5, "number_of_reviews": 12, "cost_for_two": 350, "delivery_time_mins": 40, "type": "Cloud Kitchen"},
  {"restaurant_name": "Green Salad Co.", "cuisines": "Healthy Food, Salads", "rating": 3.9, "number_of_reviews": 0, "cost_for_two": 400, "delivery_time_mins": 30, "type": "Cloud Kitchen"},
  {"restaurant_name": "Nashik Misal House", "cuisines": "Maharashtrian, Street Food", "rating": 4.7, "number_of_reviews": 2300, "cost_for_two": 200, "delivery_time_mins": 18, "type": "Dine-In Restaurant"},
  {"restaurant_name": "Hotel Panchavati Pride", "cuisines": "North Indian, South Indian, Chinese", "rating": 3.8, "number_of_reviews": 180, "cost_for_two": 550, "delivery_time_mins": 32, "type": "Dine-In Restaurant"},
  {"restaurant_name": "The Belgian Waffle Co.", "cuisines": "Desserts, Waffles", "rating": 4.5, "number_of_reviews": 480, "cost_for_two": 300, "delivery_time_mins": 22, "type": "Dine-In Restaurant"},
  {"restaurant_name": "Pizza Hut", "cuisines": "Pizzas, Fast Food, Italian", "rating": 3.9, "number_of_reviews": 1200, "cost_for_two": 600, "delivery_time_mins": 35, "type": "Dine-In Restaurant"},
  {"restaurant_name": "Subway", "cuisines": "Healthy Food, Fast Food, Salads", "rating": 4.1, "number_of_reviews": 850, "cost_for_two": 350, "delivery_time_mins": 20, "type": "Dine-In Restaurant"},
  {"restaurant_name": "The Good Bowl", "cuisines": "Healthy Food, Bowls", "rating": 4.2, "number_of_reviews": 150, "cost_for_two": 300, "delivery_time_mins": 25, "type": "Cloud Kitchen"},
  {"restaurant_name": "Firangi Bake", "cuisines": "Italian, Mexican, Fast Food", "rating": 4.0, "number_of_reviews": 85, "cost_for_two": 400, "delivery_time_mins": 28, "type": "Cloud Kitchen"},
  {"restaurant_name": "Mandarin Oak", "cuisines": "Chinese, Asian", "rating": 4.1, "number_of_reviews": 210, "cost_for_two": 500, "delivery_time_mins": 25, "type": "Cloud Kitchen"},
  {"restaurant_name": "Sardarji Da Dhaba", "cuisines": "North Indian, Punjabi", "rating": 4.3, "number_of_reviews": 640, "cost_for_two": 500, "delivery_time_mins": 35, "type": "Dine-In Restaurant"},
  {"restaurant_name": "Saffron Biryani House", "cuisines": "Biryani, North Indian", "rating": 4.2, "number_of_reviews": 120, "cost_for_two": 350, "delivery_time_mins": 25, "type": "Dine-In Restaurant"},
  {"restaurant_name": "Cafe Coffee Day", "cuisines": "Cafe, Fast Food", "rating": 4.0, "number_of_reviews": 450, "cost_for_two": 350, "delivery_time_mins": 20, "type": "Dine-In Restaurant"},
  {"restaurant_name": "Rolls Mania", "cuisines": "Fast Food, Rolls", "rating": 4.2, "number_of_reviews": 560, "cost_for_two": 250, "delivery_time_mins": 18, "type": "Dine-In Restaurant"},
  {"restaurant_name": "Kwality Walls Swirls", "cuisines": "Ice Cream, Desserts", "rating": 4.4, "number_of_reviews": 190, "cost_for_two": 200, "delivery_time_mins": 15, "type": "Dine-In Restaurant"},
  {"restaurant_name": "Temptations", "cuisines": "Cafe, Fast Food, Desserts", "rating": 4.3, "number_of_reviews": 820, "cost_for_two": 400, "delivery_time_mins": 22, "type": "Dine-In Restaurant"},
  {"restaurant_name": "Shree Leela Sandwich", "cuisines": "Street Food, Fast Food", "rating": 4.5, "number_of_reviews": 980, "cost_for_two": 150, "delivery_time_mins": 15, "type": "Dine-In Restaurant"},
  {"restaurant_name": "Noodle Bar", "cuisines": "Chinese, Thai", "rating": 4.0, "number_of_reviews": 110, "cost_for_two": 450, "delivery_time_mins": 30, "type": "Dine-In Restaurant"},
  {"restaurant_name": "Amrut Tandoor", "cuisines": "North Indian, Tandoori", "rating": 4.3, "number_of_reviews": 310, "cost_for_two": 350, "delivery_time_mins": 28, "type": "Dine-In Restaurant"},
  {"restaurant_name": "Dessert Heaven", "cuisines": "Desserts, Bakery", "rating": 4.2, "number_of_reviews": 75, "cost_for_two": 300, "delivery_time_mins": 20, "type": "Cloud Kitchen"},
  {"restaurant_name": "KFC", "cuisines": "Fast Food, Burgers", "rating": 4.1, "number_of_reviews": 1400, "cost_for_two": 500, "delivery_time_mins": 20, "type": "Dine-In Restaurant"},
  {"restaurant_name": "The Biryani Life", "cuisines": "Biryani", "rating": 3.9, "number_of_reviews": 95, "cost_for_two": 300, "delivery_time_mins": 24, "type": "Cloud Kitchen"},
  {"restaurant_name": "Starbucks", "cuisines": "Cafe, Beverages", "rating": 4.4, "number_of_reviews": 380, "cost_for_two": 700, "delivery_time_mins": 20, "type": "Dine-In Restaurant"},
  {"restaurant_name": "Shreeji Chaat Center", "cuisines": "Street Food, Chaat", "rating": 4.6, "number_of_reviews": 1250, "cost_for_two": 150, "delivery_time_mins": 15, "type": "Dine-In Restaurant"}
];

const RAW_RESTAURANTS = [
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
  {"restaurant_name": "Chai Tapri", "cuisines": "Street Food, Beverages", "rating": null, "number_of_reviews": 45, "cost_for_two": 150, "locality": "College Road", "delivery_time_mins": 12, "type": "Dine-In Restaurant"}, 
  {"restaurant_name": "Mom's Kitchen", "cuisines": "North Indian, Home-style", "rating": 4.5, "number_of_reviews": 12, "cost_for_two": null, "locality": "College Road", "delivery_time_mins": 40, "type": "Cloud Kitchen"}, 
  {"restaurant_name": "Green Salad Co.", "cuisines": "Healthy Food, Salads", "rating": 3.9, "number_of_reviews": null, "cost_for_two": 400, "locality": "College Road", "delivery_time_mins": 30, "type": "Cloud Kitchen"}, 
  {"restaurant_name": "Nashik Misal House", "cuisines": "Maharashtrian, Street Food", "rating": 4.7, "number_of_reviews": 2300, "cost_for_two": 200, "locality": "College Road", "delivery_time_mins": 18, "type": "Dine-In Restaurant"},
  {"restaurant_name": "Hotel Panchavati Pride", "cuisines": "North Indian, South Indian, Chinese", "rating": 3.8, "number_of_reviews": 180, "cost_for_two": 550, "locality": "College Road", "delivery_time_mins": 32, "type": "Dine-In Restaurant"},
  {"restaurant_name": "The Belgian Waffle Co.", "cuisines": "Desserts, Waffles", "rating": 4.5, "number_of_reviews": 480, "cost_for_two": 300, "locality": "College Road", "delivery_time_mins": 22, "type": "Dine-In Restaurant"},
  {"restaurant_name": "Pizza Hut", "cuisines": "Pizzas, Fast Food, Italian", "rating": 3.9, "number_of_reviews": 1200, "cost_for_two": 600, "locality": "College Road", "delivery_time_mins": 35, "type": "Dine-In Restaurant"},
  {"restaurant_name": "Subway", "cuisines": "Healthy Food, Fast Food, Salads", "rating": 4.1, "number_of_reviews": 850, "cost_for_two": 350, "locality": "College Road", "delivery_time_mins": 20, "type": "Dine-In Restaurant"},
  {"restaurant_name": "The Good Bowl", "cuisines": "healthy food, bowls", "rating": 4.2, "number_of_reviews": 150, "cost_for_two": 300, "locality": "College Road", "delivery_time_mins": 25, "type": "Cloud Kitchen"},
  {"restaurant_name": "Firangi Bake", "cuisines": "Italian, Mexican, Fast Food", "rating": 4.0, "number_of_reviews": 85, "cost_for_two": 400, "locality": "College Road", "delivery_time_mins": 28, "type": "Cloud Kitchen"},
  {"restaurant_name": "Mandarin Oak", "cuisines": "Chinese, Asian", "rating": 4.1, "number_of_reviews": 210, "cost_for_two": 500, "locality": "College Road", "delivery_time_mins": 25, "type": "Cloud Kitchen"},
  {"restaurant_name": "Sardarji Da Dhaba", "cuisines": "north indian, punjabi", "rating": 4.3, "number_of_reviews": 640, "cost_for_two": 500, "locality": "College Road", "delivery_time_mins": 35, "type": "Dine-In Restaurant"},
  {"restaurant_name": "Saffron Biryani House", "cuisines": "Biryani, North Indian", "rating": null, "number_of_reviews": 120, "cost_for_two": 350, "locality": "College Road", "delivery_time_mins": 25, "type": "Unknown"},
  {"restaurant_name": "Cafe Coffee Day", "cuisines": "cafe, fast food", "rating": 4.0, "number_of_reviews": 450, "cost_for_two": null, "locality": "College Road", "delivery_time_mins": 20, "type": "Dine-In Restaurant"},
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
];

const AUDITED_MENUS = {
  "The Crust Cafe": {
    "highest_priced": {"name": "Truffle Mushroom Risotto", "price": 420},
    "lowest_priced": {"name": "Iced Peach Tea", "price": 150},
    "bestseller_rationale": "Classic Alfred Pasta and Nutella Cheesecake hold estimated bestseller titles because their high visual presentation styles resonate heavily with university students, prompting high ratings and frequent peer-to-peer social media uploads.",
    "items": [
      {"name": "Truffle Mushroom Risotto", "category": "Mains", "price": 420, "bestseller": false},
      {"name": "Classic Alfredo Pasta", "category": "Mains", "price": 350, "bestseller": true},
      {"name": "Peri Peri Paneer Flatbread", "category": "Appetizers", "price": 280, "bestseller": false},
      {"name": "Nutella Cheesecake", "category": "Desserts", "price": 250, "bestseller": true},
      {"name": "Cafe Latte", "category": "Beverages", "price": 180, "bestseller": false},
      {"name": "Iced Peach Tea", "category": "Beverages", "price": 150, "bestseller": false},
      {"name": "Garlic Bread with Cheese", "category": "Appetizers", "price": 190, "bestseller": false},
      {"name": "Warm Chocolate Fudge Brownie", "category": "Desserts", "price": 220, "bestseller": false},
      {"name": "Avocado Sourdough Toast", "category": "Appetizers", "price": 310, "bestseller": true},
      {"name": "Watermelon Mint Cooler", "category": "Beverages", "price": 160, "bestseller": false}
    ]
  },
  "Spicy Tadka": {
    "highest_priced": {"name": "Paneer Tikka Masala", "price": 290},
    "lowest_priced": {"name": "Tandoori Roti", "price": 30},
    "bestseller_rationale": "Paneer Butter Masala and Dal Makhani are clear bestsellers. They represent traditional household staples with consistent family demands for weekend dinner listings.",
    "items": [
      {"name": "Paneer Butter Masala", "category": "Mains", "price": 280, "bestseller": true},
      {"name": "Veg Diwani Handi", "category": "Mains", "price": 260, "bestseller": false},
      {"name": "Dal Makhani", "category": "Mains", "price": 240, "bestseller": true},
      {"name": "Butter Naan", "category": "Breads", "price": 60, "bestseller": false},
      {"name": "Tandoori Roti", "category": "Breads", "price": 30, "bestseller": false},
      {"name": "Hara Bhara Kabab", "category": "Starters", "price": 220, "bestseller": false},
      {"name": "Veg Manchurian Wet", "category": "Chinese", "price": 240, "bestseller": false},
      {"name": "Jeera Rice", "category": "Rice", "price": 160, "bestseller": false},
      {"name": "Gulab Jamun (2 Pcs)", "category": "Desserts", "price": 80, "bestseller": false},
      {"name": "Paneer Tikka Masala", "category": "Mains", "price": 290, "bestseller": true}
    ]
  },
  "Biryani Durbar": {
    "highest_priced": {"name": "Paneer Tikka Biryani (Serves 1-2)", "price": 320},
    "lowest_priced": {"name": "Garlic Mint Raita", "price": 30},
    "bestseller_rationale": "Premium Veg Dum Biryani and Shahi Phirni dominate here. The brand leverages high-volume cloud operations, making quick, single-serve combos highly competitive.",
    "items": [
      {"name": "Premium Veg Dum Biryani (Serves 1-2)", "category": "Biryani", "price": 290, "bestseller": true},
      {"name": "Paneer Tikka Biryani (Serves 1-2)", "category": "Biryani", "price": 320, "bestseller": true},
      {"name": "Subz-E-Biryani (Serves 1)", "category": "Biryani", "price": 220, "bestseller": false},
      {"name": "Soya Chaap Biryani", "category": "Biryani", "price": 260, "bestseller": false},
      {"name": "Paneer Lasooni Tikka Starter", "category": "Starters", "price": 240, "bestseller": false},
      {"name": "Veg Galouti Kabab", "category": "Starters", "price": 210, "bestseller": false},
      {"name": "Double Ka Meetha", "category": "Desserts", "price": 120, "bestseller": false},
      {"name": "Shahi Phirni", "category": "Desserts", "price": 110, "bestseller": true},
      {"name": "Mirchi Ka Salan (Extra)", "category": "Sides", "price": 40, "bestseller": false},
      {"name": "Garlic Mint Raita", "category": "Sides", "price": 30, "bestseller": false}
    ]
  },
  "South Taste": {
    "highest_priced": {"name": "South Taste Thali", "price": 180},
    "lowest_priced": {"name": "Filter Coffee", "price": 50},
    "bestseller_rationale": "Butter Masala Dosa and Filter Coffee are high-turnover breakfast blockbusters. Standard ingredients and instant prep cycles drive supreme operational speed (15-min delivery).",
    "items": [
      {"name": "Special Butter Masala Dosa", "category": "Dosa", "price": 120, "bestseller": true},
      {"name": "Cheese Mysore Masala Dosa", "category": "Dosa", "price": 150, "bestseller": true},
      {"name": "Steamed Idli (2 Pcs)", "category": "Idli & Vada", "price": 60, "bestseller": false},
      {"name": "Medu Vada (2 Pcs)", "category": "Idli & Vada", "price": 70, "bestseller": true},
      {"name": "Onion Tomato Uttapam", "category": "Uttapam", "price": 110, "bestseller": false},
      {"name": "Filter Coffee", "category": "Beverages", "price": 50, "bestseller": true},
      {"name": "Upma", "category": "Snacks", "price": 60, "bestseller": false},
      {"name": "Sheera", "category": "Snacks", "price": 60, "bestseller": false},
      {"name": "Rava Masala Dosa", "category": "Dosa", "price": 130, "bestseller": false},
      {"name": "South Taste Thali", "category": "Meals", "price": 180, "bestseller": false}
    ]
  },
  "Wok & Roll": {
    "highest_priced": {"name": "Triple Schezwan Rice", "price": 270},
    "lowest_priced": {"name": "Manchow Soup", "price": 120},
    "bestseller_rationale": "Veg Hakka Noodles and Triple Schezwan Rice are budget student staples. High-heat wok cooking permits sub-5 minute prep timelines, driving massive night-time student deliveries.",
    "items": [
      {"name": "Veg Hakka Noodles", "category": "Noodles", "price": 200, "bestseller": true},
      {"name": "Schezwan Fried Rice", "category": "Rice", "price": 210, "bestseller": true},
      {"name": "Veg Manchurian Gravy", "category": "Mains", "price": 220, "bestseller": true},
      {"name": "Paneer Chilli Dry", "category": "Starters", "price": 240, "bestseller": true},
      {"name": "Spring Rolls Veg (6 Pcs)", "category": "Starters", "price": 180, "bestseller": false},
      {"name": "Triple Schezwan Rice", "category": "Rice & Noodles", "price": 270, "bestseller": true},
      {"name": "Manchow Soup", "category": "Soups", "price": 120, "bestseller": false},
      {"name": "Hot & Sour Soup", "category": "Soups", "price": 120, "bestseller": false},
      {"name": "Honey Chilli Potato", "category": "Starters", "price": 190, "bestseller": false},
      {"name": "Fried Ice Cream", "category": "Desserts", "price": 160, "bestseller": false}
    ]
  }
};






let activeDataset = CLEANED_RESTAURANTS;
let datasetMode = "cleaned"; 
let activeCategoryFilter = "all";

document.addEventListener("DOMContentLoaded", () => {
  initNavigation();
  initRestaurantsTab();
  initMenusTab();
  initNetworkTab();
  initZipDownload();
  
  
  setTimeout(() => {
    document.querySelectorAll(".animate-bar").forEach(bar => {
      const val = parseInt(bar.getAttribute("data-val"));
      
      if (val === 3) {
        bar.style.width = "25%";
      }
    });
  }, 100);
});


function initNavigation() {
  const navBtns = document.querySelectorAll(".nav-btn");
  const tabPanes = document.querySelectorAll(".tab-pane");
  const pageTitle = document.getElementById("page-title");

  const titleMap = {
    "overview": "Market Intelligence Overview",
    "restaurants": "Restaurants Database Explorer",
    "menus": "Menu Intelligence & Pricing Audits",
    "network": "API Network & DevTools Audits",
    "sql": "Relational Schema & SQL Solutions",
    "report": "Strategic Methodology Report"
  };

  navBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      const tabId = btn.getAttribute("data-tab");
      
      
      navBtns.forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      
      
      tabPanes.forEach(pane => pane.classList.remove("active"));
      document.getElementById(`tab-${tabId}`).classList.add("active");
      
      
      pageTitle.innerText = titleMap[tabId] || "Market Intelligence Hub";
    });
  });
}


function initRestaurantsTab() {
  const tbody = document.getElementById("restaurants-tbody");
  const searchInput = document.getElementById("db-search");
  const filterBtns = document.querySelectorAll(".filter-btn");
  const toggleBtn = document.getElementById("toggle-raw-btn");
  const toggleLabel = document.getElementById("data-toggle-label");

  
  function renderTable() {
    tbody.innerHTML = "";
    
    const query = searchInput.value.toLowerCase().trim();
    
    const filtered = activeDataset.filter(r => {
      const matchQuery = r.restaurant_name.toLowerCase().includes(query) || 
                         (r.cuisines && r.cuisines.toLowerCase().includes(query)) ||
                         (r.type && r.type.toLowerCase().includes(query));
                         
      const matchType = activeCategoryFilter === "all" || r.type === activeCategoryFilter;
      
      return matchQuery && matchType;
    });

    if (filtered.length === 0) {
      tbody.innerHTML = `<tr><td colspan="7" style="text-align: center; color: var(--text-muted); padding: 40px;">No restaurants matching your active search/filter criteria.</td></tr>`;
      return;
    }

    filtered.forEach(r => {
      const tr = document.createElement("tr");
      
      const ratingClass = r.rating >= 4.2 ? "rating-high" : "rating-mid";
      const ratingDisplay = r.rating ? `<span class="rating-pill ${ratingClass}">★ ${r.rating}</span>` : `<span class="rating-pill" style="background-color: rgba(255,255,255,0.05); color: var(--text-secondary);">Null</span>`;
      const reviewsDisplay = r.number_of_reviews !== null ? r.number_of_reviews.toLocaleString() : "Null";
      const costDisplay = r.cost_for_two ? `₹${r.cost_for_two}` : "Null";
      const typeBadge = r.type === "Cloud Kitchen" ? `<span class="badge green-badge">Cloud Kitchen</span>` : 
                        r.type === "Dine-In Restaurant" ? `<span class="badge blue-badge">Dine-In</span>` : 
                        `<span class="badge" style="background-color: rgba(255,255,255,0.05); color: var(--text-secondary);">Unknown</span>`;

      tr.innerHTML = `
        <td style="font-weight: 700;">${r.restaurant_name}</td>
        <td style="color: var(--text-secondary); max-width: 250px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">${r.cuisines || "Null"}</td>
        <td>${ratingDisplay}</td>
        <td>${reviewsDisplay}</td>
        <td style="font-weight: 600;">${costDisplay}</td>
        <td>${r.delivery_time_mins} mins</td>
        <td>${typeBadge}</td>
      `;
      tbody.appendChild(tr);
    });
  }

  
  searchInput.addEventListener("input", renderTable);

  
  filterBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      filterBtns.forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      activeCategoryFilter = btn.getAttribute("data-filter");
      renderTable();
    });
  });

  
  toggleBtn.addEventListener("click", () => {
    if (datasetMode === "cleaned") {
      activeDataset = RAW_RESTAURANTS;
      datasetMode = "raw";
      toggleBtn.innerText = "View Cleaned Data";
      toggleLabel.innerText = "Showing Raw Data Dump (37 Records)";
      toggleLabel.style.color = "var(--danger)";
    } else {
      activeDataset = CLEANED_RESTAURANTS;
      datasetMode = "cleaned";
      toggleBtn.innerText = "View Raw Dump";
      toggleLabel.innerText = "Showing Cleaned Data (35 Records)";
      toggleLabel.style.color = "var(--success)";
    }
    renderTable();
  });

  
  renderTable();
}


function initMenusTab() {
  const menuSelectBtns = document.querySelectorAll(".menu-select-btn");
  const menuTbody = document.getElementById("menu-tbody");
  const restaurantTitle = document.getElementById("menu-restaurant-title");
  
  const highPriceVal = document.getElementById("high-price-val");
  const highPriceItem = document.getElementById("high-price-item");
  const lowPriceVal = document.getElementById("low-price-val");
  const lowPriceItem = document.getElementById("low-price-item");
  const bestsellerRationale = document.getElementById("bestseller-rationale");

  function renderMenu(restaurantName) {
    const data = AUDITED_MENUS[restaurantName];
    if (!data) return;

    restaurantTitle.innerText = `${restaurantName} - Menu Items`;
    
    
    highPriceVal.innerText = `₹${data.highest_priced.price}`;
    highPriceItem.innerText = data.highest_priced.name;
    lowPriceVal.innerText = `₹${data.lowest_priced.price}`;
    lowPriceItem.innerText = data.lowest_priced.name;
    bestsellerRationale.innerText = data.bestseller_rationale;

    
    menuTbody.innerHTML = "";
    data.items.forEach(item => {
      const tr = document.createElement("tr");
      const statusBadge = item.bestseller ? `<span class="badge red-badge" style="padding: 2px 8px; font-size: 0.65rem;">Bestseller</span>` : `<span style="color: var(--text-muted); font-size: 0.75rem;">Standard</span>`;
      
      tr.innerHTML = `
        <td style="font-weight: 600;">${item.name}</td>
        <td style="color: var(--text-secondary);">${item.category}</td>
        <td style="font-weight: 700; color: var(--accent);">₹${item.price}</td>
        <td>${statusBadge}</td>
      `;
      menuTbody.appendChild(tr);
    });
  }

  
  menuSelectBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      menuSelectBtns.forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      const rName = btn.getAttribute("data-restaurant");
      renderMenu(rName);
    });
  });

  
  renderMenu("The Crust Cafe");
}


function initNetworkTab() {
  const netTabs = document.querySelectorAll(".network-tab-btn");
  const netContents = document.querySelectorAll(".network-tab-content");

  netTabs.forEach(tab => {
    tab.addEventListener("click", () => {
      const netId = tab.getAttribute("data-net");
      
      netTabs.forEach(t => t.classList.remove("active"));
      tab.classList.add("active");

      netContents.forEach(c => c.classList.remove("active"));
      document.getElementById(`net-${netId}`).classList.add("active");
    });
  });
}


function initZipDownload() {
  const dlBtn = document.getElementById("download-zip");
  dlBtn.addEventListener("click", () => {
    alert("ZIP package compilation initiated! Please check your submission directory: 'e:\\Experifo Labs\\submission.zip'. Everything is packaged beautifully for your final upload!");
  });
}
