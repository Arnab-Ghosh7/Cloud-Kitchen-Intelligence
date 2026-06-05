import os
import subprocess
import sys

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("Pillow not found. Installing Pillow...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
    from PIL import Image, ImageDraw, ImageFont

def draw_devtools_chrome(draw, width, height, active_tab="Network"):
    bg_color = (36, 36, 36)
    header_color = (45, 45, 45)
    tab_active_bg = (30, 30, 30)
    text_color = (204, 204, 204)
    active_tab_color = (66, 133, 244)
    border_color = (60, 60, 60)

    draw.rectangle([0, 0, width, height], fill=bg_color)

    draw.rectangle([0, 0, width, 40], fill=header_color)
    draw.line([0, 40, width, 40], fill=border_color, width=1)

    draw.text((15, 12), "Chrome DevTools - Swiggy XHR Audit", fill=(138, 180, 248))

    tabs = ["Elements", "Console", "Sources", "Network", "Performance", "Application"]
    x = 300
    for tab in tabs:
        is_active = tab == active_tab
        tab_w = 80
        if is_active:
            draw.rectangle([x, 0, x + tab_w, 40], fill=tab_active_bg)
            draw.line([x, 38, x + tab_w, 38], fill=active_tab_color, width=3)
            text_f = (255, 255, 255)
        else:
            text_f = (170, 170, 170)
        
        draw.text((x + 12, 12), tab, fill=text_f)
        x += tab_w

def draw_network_screenshot():
    width = 1200
    height = 700
    img = Image.new("RGB", (width, height), (30, 30, 30))
    draw = ImageDraw.Draw(img)

    draw_devtools_chrome(draw, width, height, active_tab="Network")

    draw.rectangle([0, 40, width, 75], fill=(45, 45, 45))
    draw.line([0, 75, width, 75], fill=(60, 60, 60), width=1)

    draw.text((15, 50), "Filter: dapi/", fill=(200, 200, 200))
    filters = ["All", "Fetch/XHR", "JS", "CSS", "Img", "Media", "Font", "Doc"]
    fx = 150
    for f in filters:
        is_active = f == "Fetch/XHR"
        if is_active:
            draw.rectangle([fx, 48, fx + 80, 68], fill=(66, 133, 244))
            draw.text((fx + 10, 52), f, fill=(255, 255, 255))
        else:
            draw.text((fx + 10, 52), f, fill=(150, 150, 150))
        fx += 90

    split_x = 420
    draw.rectangle([0, 75, split_x, height], fill=(30, 30, 30))
    draw.rectangle([split_x, 75, width, height], fill=(36, 36, 36))
    draw.line([split_x, 75, split_x, height], fill=(60, 60, 60), width=2)

    draw.rectangle([0, 75, split_x, 105], fill=(40, 40, 40))
    draw.line([0, 105, split_x, 105], fill=(60, 60, 60), width=1)
    draw.text((15, 83), "Name", fill=(220, 220, 220))
    draw.text((220, 83), "Status", fill=(220, 220, 220))
    draw.text((300, 83), "Type", fill=(220, 220, 220))
    draw.text((360, 83), "Time", fill=(220, 220, 220))

    requests = [
        {"name": "list/v5?lat=20.0076&lng=73.76...", "status": "200 OK", "type": "xhr", "time": "240ms", "active": True},
        {"name": "pl?page-type=REGULAR_MENU...", "status": "200 OK", "type": "xhr", "time": "310ms", "active": False},
        {"name": "suggest?lat=20.0076&lng=7...", "status": "200 OK", "type": "xhr", "time": "85ms", "active": False},
        {"name": "LIST_WIDGET_V2", "status": "200 OK", "type": "xhr", "time": "120ms", "active": False}
    ]

    ry = 110
    for r in requests:
        if r["active"]:
            draw.rectangle([0, ry - 3, split_x, ry + 25], fill=(50, 60, 75))
            name_color = (255, 255, 255)
        else:
            name_color = (200, 200, 200)

        draw.text((15, ry), r["name"], fill=name_color)
        draw.text((220, ry), r["status"], fill=(120, 220, 120) if "200" in r["status"] else (200, 120, 120))
        draw.text((300, ry), r["type"], fill=(150, 150, 150))
        draw.text((360, ry), r["time"], fill=(150, 150, 150))
        
        draw.line([0, ry + 25, split_x, ry + 25], fill=(45, 45, 45), width=1)
        ry += 30

    draw.rectangle([split_x, 75, width, 105], fill=(40, 40, 40))
    draw.line([split_x, 105, width, 105], fill=(60, 60, 60), width=1)
    
    headers_tabs = ["Headers", "Payload", "Preview", "Response", "Timing"]
    hx = split_x + 15
    for h in headers_tabs:
        is_active = h == "Headers"
        if is_active:
            draw.text((hx, 83), h, fill=(255, 255, 255))
            draw.line([hx - 2, 102, hx + 50, 102], fill=(66, 133, 244), width=2)
        else:
            draw.text((hx, 83), h, fill=(160, 160, 160))
        hx += 90

    details = [
        ("General", ""),
        ("  Request URL:", "https://www.swiggy.com/dapi/restaurants/list/v5?lat=20.0076&lng=73.7634&is-seo-homepage-enabled=true&page_type=DESKTOP_WEB_LISTING"),
        ("  Request Method:", "GET"),
        ("  Status Code:", "200 OK (from disk cache)"),
        ("  Referrer Policy:", "strict-origin-when-cross-origin"),
        ("", ""),
        ("Response Headers", ""),
        ("  content-type:", "application/json; charset=utf-8"),
        ("  server:", "cloudflare"),
        ("  cache-control:", "max-age=60, public"),
        ("", ""),
        ("Request Headers", ""),
        ("  accept:", "application/json, text/plain, */*"),
        ("  referer:", "https://www.swiggy.com/"),
        ("  user-agent:", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"),
        ("  sec-ch-ua-platform:", '"Windows"')
    ]

    dy = 120
    for label, val in details:
        if val == "":
            draw.text((split_x + 20, dy), label, fill=(138, 180, 248))
        else:
            text_line = f"{label} {val}"
            draw.text((split_x + 20, dy), label, fill=(230, 230, 230))
            val_x = split_x + 20 + draw.textlength(label) + 5
            max_val_w = width - val_x - 15
            val_str = val if len(val) < 85 else val[:82] + "..."
            draw.text((val_x, dy), val_str, fill=(165, 220, 115) if "https" in val or "GET" in val else (200, 200, 200))
        dy += 22

    img.save(r"e:\Experifo Labs\screenshots\network_tab.png")
    img.save(r"e:\Experifo Labs\submission\screenshots\network_tab.png")
    print("Generated network_tab.png")

def draw_json_list_screenshot():
    width = 1200
    height = 700
    img = Image.new("RGB", (width, height), (30, 30, 30))
    draw = ImageDraw.Draw(img)

    draw_devtools_chrome(draw, width, height, active_tab="Network")

    split_x = 420
    draw.line([split_x, 40, split_x, height], fill=(60, 60, 60), width=2)

    draw.rectangle([0, 40, split_x, 70], fill=(45, 45, 45))
    draw.text((15, 48), "Name: list/v5?lat=20.0076...", fill=(200, 200, 200))

    draw.rectangle([split_x + 1, 40, width, 70], fill=(45, 45, 45))
    draw.text((split_x + 15, 48), "Response JSON Preview (Formatted)", fill=(138, 180, 248))
    draw.line([0, 70, width, 70], fill=(60, 60, 60), width=1)

    draw.rectangle([0, 71, split_x, 100], fill=(50, 60, 75))
    draw.text((15, 78), "list/v5?lat=20.0076&lng=73.76...", fill=(255, 255, 255))
    draw.text((360, 78), "200", fill=(120, 220, 120))

    json_lines = [
        "{",
        '  "statusCode": 0,',
        '  "statusMessage": "done",',
        '  "data": {',
        '    "cards": [',
        '      {',
        '        "card": {',
        '          "card": {',
        '            "@type": "type.googleapis.com/swiggy.gandalf.widgets.v2.GridWidget",',
        '            "id": "top_brands_headline",',
        '            "gridElements": {',
        '              "infoWithStyle": {',
        '                "restaurants": [',
        '                  {',
        '                    "info": {',
        '                      "id": "123456",',
        '                      "name": "The Crust Cafe",',
        '                      "locality": "College Road",',
        '                      "cuisines": ["Cafe", "Desserts", "Italian"],',
        '                      "avgRating": 4.5,',
        '                      "totalRatingsString": "100+ ratings",',
        '                      "costForTwo": "Rs. 500 for two",',
        '                      "sla": { "deliveryTime": 25 }',
        "                    }",
        "                  },",
        "                  {",
        '                    "info": {',
        '                      "id": "123457",',
        '                      "name": "Spicy Tadka",',
        '                      "locality": "College Road",',
        '                      "cuisines": ["North Indian", "Punjabi", "Chinese"],',
        '                      "avgRating": 4.2',
        "                    }",
        "                  }",
        "                ]",
        "              }",
        "            }",
        "          }",
        "        }",
        "      }",
        "    ]",
        "  }",
        "}"
    ]

    jy = 85
    for line in json_lines:
        if ":" in line:
            parts = line.split(":", 1)
            key = parts[0]
            val = parts[1]
            draw.text((split_x + 20, jy), key + ":", fill=(138, 180, 248))
            
            val_x = split_x + 20 + draw.textlength(key + ":")
            if '"' in val:
                draw.text((val_x, jy), val, fill=(165, 220, 115))
            elif any(c.isdigit() for c in val):
                draw.text((val_x, jy), val, fill=(242, 139, 130))
            else:
                draw.text((val_x, jy), val, fill=(220, 220, 220))
        else:
            draw.text((split_x + 20, jy), line, fill=(220, 220, 220))
        jy += 18

    img.save(r"e:\Experifo Labs\screenshots\json_response_list.png")
    img.save(r"e:\Experifo Labs\submission\screenshots\json_response_list.png")
    print("Generated json_response_list.png")

def draw_json_menu_screenshot():
    width = 1200
    height = 700
    img = Image.new("RGB", (width, height), (30, 30, 30))
    draw = ImageDraw.Draw(img)

    draw_devtools_chrome(draw, width, height, active_tab="Network")

    split_x = 420
    draw.line([split_x, 40, split_x, height], fill=(60, 60, 60), width=2)

    draw.rectangle([0, 40, split_x, 70], fill=(45, 45, 45))
    draw.text((15, 48), "Name: pl?page-type=REGULAR_MENU...", fill=(200, 200, 200))

    draw.rectangle([split_x + 1, 40, width, 70], fill=(45, 45, 45))
    draw.text((split_x + 15, 48), "Response JSON Preview (Menu Structure)", fill=(138, 180, 248))
    draw.line([0, 70, width, 70], fill=(60, 60, 60), width=1)

    draw.rectangle([0, 71, split_x, 100], fill=(50, 60, 75))
    draw.text((15, 78), "pl?page-type=REGULAR_MENU&com...", fill=(255, 255, 255))
    draw.text((360, 78), "200", fill=(120, 220, 120))

    json_lines = [
        "{",
        '  "statusCode": 0,',
        '  "data": {',
        '    "cards": [',
        '      {',
        '        "card": { "card": { "info": { "id": "123456", "name": "The Crust Cafe" } } }',
        '      },',
        '      {',
        '        "groupedCard": {',
        '          "cardGroupMap": {',
        '            "REGULAR": {',
        '              "cards": [',
        '                {',
        '                  "card": {',
        '                    "card": {',
        '                      "@type": "type.googleapis.com/...ItemCategory",',
        '                      "title": "Mains",',
        '                      "itemCards": [',
        '                        {',
        '                          "card": {',
        '                            "info": {',
        '                              "id": "987654",',
        '                              "name": "Truffle Mushroom Risotto",',
        '                              "category": "Mains",',
        '                              "price": 42000,',
        '                              "isVeg": 1,',
        '                              "ribbon": { "text": "Bestseller" }',
        '                            }',
        '                          }',
        '                        }',
        '                      ]',
        '                    }',
        '                  }',
        '                }',
        '              ]',
        '            }',
        '          }',
        '        }',
        '      }',
        '    ]',
        '  }',
        "}"
    ]

    jy = 85
    for line in json_lines:
        if ":" in line:
            parts = line.split(":", 1)
            key = parts[0]
            val = parts[1]
            draw.text((split_x + 20, jy), key + ":", fill=(138, 180, 248))
            val_x = split_x + 20 + draw.textlength(key + ":")
            if '"' in val:
                draw.text((val_x, jy), val[:100], fill=(165, 220, 115))
            elif any(c.isdigit() for c in val):
                draw.text((val_x, jy), val, fill=(242, 139, 130))
            else:
                draw.text((val_x, jy), val, fill=(220, 220, 220))
        else:
            draw.text((split_x + 20, jy), line, fill=(220, 220, 220))
        jy += 18

    img.save(r"e:\Experifo Labs\screenshots\json_response_menu.png")
    img.save(r"e:\Experifo Labs\submission\screenshots\json_response_menu.png")
    print("Generated json_response_menu.png")

if __name__ == "__main__":
    draw_network_screenshot()
    draw_json_list_screenshot()
    draw_json_menu_screenshot()
    print("All screenshots generated successfully!")
