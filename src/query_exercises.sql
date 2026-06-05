CREATE TABLE restaurants (
    restaurant_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    restaurant_name VARCHAR(150) NOT NULL,
    locality VARCHAR(100) NOT NULL DEFAULT 'College Road',
    rating DECIMAL(2,1) CHECK (rating >= 1.0 AND rating <= 5.0),
    number_of_reviews INTEGER DEFAULT 0,
    cost_for_two INTEGER CHECK (cost_for_two > 0),
    delivery_time_mins INTEGER CHECK (delivery_time_mins > 0),
    restaurant_type VARCHAR(50) CHECK (restaurant_type IN ('Cloud Kitchen', 'Dine-In Restaurant', 'Unknown'))
);

CREATE TABLE restaurant_cuisines (
    restaurant_id INTEGER,
    cuisine_tag VARCHAR(50) NOT NULL,
    PRIMARY KEY (restaurant_id, cuisine_tag),
    FOREIGN KEY (restaurant_id) REFERENCES restaurants(restaurant_id) ON DELETE CASCADE
);


CREATE TABLE menu_items (
    item_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    restaurant_id INTEGER NOT NULL,
    item_name VARCHAR(200) NOT NULL,
    category VARCHAR(100),
    price DECIMAL(10,2) CHECK (price >= 0.0),
    is_bestseller BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (restaurant_id) REFERENCES restaurants(restaurant_id) ON DELETE CASCADE
);

-- Indexing for Query Optimization
CREATE INDEX idx_restaurants_rating ON restaurants(rating DESC);
CREATE INDEX idx_menu_items_price ON menu_items(price DESC);
CREATE INDEX idx_cuisines_tag ON restaurant_cuisines(cuisine_tag);



SELECT 
    restaurant_name, 
    rating, 
    cost_for_two, 
    restaurant_type
FROM 
    restaurants
ORDER BY 
    rating DESC, 
    number_of_reviews DESC
LIMIT 5;


SELECT 
    c.cuisine_tag,
    ROUND(AVG(r.cost_for_two), 2) AS average_cost_for_two,
    COUNT(r.restaurant_id) AS restaurant_count
FROM 
    restaurants r
JOIN 
    restaurant_cuisines c ON r.restaurant_id = c.restaurant_id
GROUP BY 
    c.cuisine_tag
ORDER BY 
    average_cost_for_two DESC;


SELECT 
    r.restaurant_name,
    COUNT(c.cuisine_tag) AS cuisine_count,
    GROUP_CONCAT(c.cuisine_tag, ', ') AS cuisine_tags 
FROM 
    restaurants r
JOIN 
    restaurant_cuisines c ON r.restaurant_id = c.restaurant_id
GROUP BY 
    r.restaurant_id, r.restaurant_name
HAVING 
    COUNT(c.cuisine_tag) > 1
ORDER BY 
    cuisine_count DESC;


SELECT 
    r.restaurant_name,
    m.item_name,
    m.category,
    m.price
FROM 
    menu_items m
JOIN 
    restaurants r ON m.restaurant_id = r.restaurant_id
WHERE 
    m.price = (SELECT MAX(price) FROM menu_items);
