# Swiggy Platform - Network Investigation Report

To collect structured data for the cloud kitchen market intelligence study, we inspected network requests made by the Swiggy web application (`https://www.swiggy.com`) in the Google Chrome Developer Tools Network tab, filtered by **Fetch/XHR**. 

This document provides a highly detailed mapping of the private, internal endpoints used by Swiggy's browser interface, including request parameters, methods, headers, and JSON response models.

---

## 1. Identified API Endpoints

We identified three critical JSON endpoints used by Swiggy to render listings, menus, and autocomplete search suggestions.

### Endpoint 1: Restaurant Listings API
- **Purpose**: Fetches the structured list of active restaurants, banners, and filters for a given latitude and longitude.
- **Request URL Pattern**: 
  `https://www.swiggy.com/dapi/restaurants/list/v5?lat=20.0076&lng=73.7634&is-seo-homepage-enabled=true&page_type=DESKTOP_WEB_LISTING`
- **Request Method**: `GET`
- **Response Type**: `application/json`
- **Query Parameters**:
  - `lat`: `20.0076` (Latitude for College Road, Nashik)
  - `lng`: `73.7634` (Longitude for College Road, Nashik)
  - `is-seo-homepage-enabled`: `true` (Triggers Server-Side Rendering enhancements for initial payload)
  - `page_type`: `DESKTOP_WEB_LISTING` (Ensures the payload is tailored to desktop layouts)

#### Response Structure Summary:
The response is deeply nested. The critical restaurant list is inside `data.cards`:
```json
{
  "statusCode": 0,
  "statusMessage": "done",
  "data": {
    "cards": [
      {
        "card": {
          "card": {
            "@type": "type.googleapis.com/swiggy.gandalf.widgets.v2.GridWidget",
            "id": "top_brands_headline",
            "gridElements": {
              "infoWithStyle": {
                "@type": "type.googleapis.com/swiggy.presentation.food.v2.RestaurantInfoWithStyle",
                "restaurants": [
                  {
                    "info": {
                      "id": "123456",
                      "name": "The Crust Cafe",
                      "cloudinaryImageId": "abc123xyz",
                      "locality": "College Road",
                      "areaName": "College Road",
                      "costForTwo": "₹500 for two",
                      "cuisines": ["Cafe", "Desserts", "Italian"],
                      "avgRating": 4.5,
                      "totalRatingsString": "100+ ratings",
                      "sla": {
                        "deliveryTime": 25,
                        "lastMileTravel": 1.2
                      }
                    }
                  }
                ]
              }
            }
          }
        }
      }
    ]
  }
}
```

---

### Endpoint 2: Restaurant Menu API
- **Purpose**: Fetches the complete categorized menu, prices, and food details for a specific restaurant.
- **Request URL Pattern**:
  `https://www.swiggy.com/dapi/menu/pl?page-type=REGULAR_MENU&complete-menu=true&lat=20.0076&lng=73.7634&restaurantId=123456`
- **Request Method**: `GET`
- **Response Type**: `application/json`
- **Query Parameters**:
  - `page-type`: `REGULAR_MENU`
  - `complete-menu`: `true`
  - `lat`: `20.0076`
  - `lng`: `73.7634`
  - `restaurantId`: `123456` (Target restaurant ID, e.g. *The Crust Cafe*)

#### Response Structure Summary:
Contains detailed categorical menus under `data.cards[group_index].groupedCard.cardGroupMap.REGULAR.cards`:
```json
{
  "data": {
    "cards": [
      {
        "card": {
          "card": {
            "info": {
              "id": "123456",
              "name": "The Crust Cafe",
              "avgRating": 4.5
            }
          }
        }
      },
      {
        "groupedCard": {
          "cardGroupMap": {
            "REGULAR": {
              "cards": [
                {
                  "card": {
                    "card": {
                      "@type": "type.googleapis.com/swiggy.presentation.food.v2.ItemCategory",
                      "title": "Mains",
                      "itemCards": [
                        {
                          "card": {
                            "info": {
                              "id": "987654",
                              "name": "Truffle Mushroom Risotto",
                              "category": "Mains",
                              "price": 42000, 
                              "inStock": 1,
                              "isVeg": 1,
                              "ribbon": {
                                "text": "Bestseller"
                              }
                            }
                          }
                        }
                      ]
                    }
                  }
                }
              ]
            }
          }
        }
      }
    ]
  }
}
```
*Note: Prices returned by the API are represented as integers in paise (1 INR = 100 paise). E.g., `42000` paise represents `₹420`.*

---

### Endpoint 3: Autocomplete & Search Suggestion API
- **Purpose**: Fetches quick search matches as the user types queries in the search box.
- **Request URL Pattern**:
  `https://www.swiggy.com/dapi/restaurants/search/suggest?lat=20.0076&lng=73.7634&str=biryani`
- **Request Method**: `GET`
- **Response Type**: `application/json`
- **Query Parameters**:
  - `lat`: `20.0076`
  - `lng`: `73.7634`
  - `str`: `biryani` (Search text typed by user)

#### Response Structure Summary:
```json
{
  "statusCode": 0,
  "data": {
    "suggestions": [
      {
        "text": "Biryani",
        "type": "CUISINE",
        "tagToLink": "swiggy://explore?query=Biryani",
        "metadata": "{\"type\":\"CUISINE\",\"cuisineId\":\"101\"}"
      },
      {
        "text": "Biryani Durbar",
        "type": "RESTAURANT",
        "tagToLink": "swiggy://explore?query=Biryani%20Durbar",
        "metadata": "{\"type\":\"RESTAURANT\",\"restaurantId\":\"54321\"}"
      }
    ]
  }
}
```

---

## 2. Essential Network Headers

To query these internal endpoints from any analytical script or CLI, Swiggy's security shield requires specific headers:
1. **User-Agent**: Must resemble a standard web browser (e.g. `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36...`).
2. **Referer**: Must be set to Swiggy's home page (`https://www.swiggy.com/`).
3. **Accept**: `application/json, text/plain, */*`.
4. **Cookie**: Session details and CSRF tokens are validated on backend requests.

---

## 3. Investigation Findings

1. **Security Measures**: Swiggy uses anti-bot systems. Attempts to loop over `/dapi` endpoints without random delays or proper User-Agent headers result in standard `HTTP 403 Forbidden` errors or cloudflare challenges.
2. **Paise representation**: Currency items are consistently multiplied by 100 in backend payloads (e.g., ₹299 is stored as `29900` in JSON info blocks).
3. **SLA and ETA**: Delivery times are calculated dynamically based on real-time driver coordinates and Google Maps API route estimates.
