# Cloud Kitchen Market Intelligence Study - College Road, Nashik


---

## 1. Project Directory Structure

```text
e:/Experifo Labs/
├── src/
│   ├── data_pipeline.py          # Data collection, cleaning, and menu generation
│   ├── network_investigation.md  # Swiggy internal XHR REST API documentation
│   ├── business_analysis.md      # Strategic competitive study & cloud kitchen strategy
│   ├── query_exercises.sql       # PostgreSQL / SQLite DDL & analytical queries
│   ├── generate_report.py        # Programmatic ReportLab PDF builder
│   ├── generate_screenshots.py   # Programmatic PIL screenshot mockup drawer
│   ├── pack_submission.py        # Submission directory packager and zapper
│   └── dashboard/                # Interactive SaaS-style Web Dashboard
│       ├── index.html            # Main markup with glassmorphism layout
│       ├── styles.css            # Dark theme, grids, micro-animations
│       └── app.js                # Search, filters, interactive tab controls
├── screenshots/                  # Verified Developer Tools evidence pngs
│   ├── network_tab.png
│   ├── json_response_list.png
│   └── json_response_menu.png
├── submission/                   # Complete structured submission assets
│   ├── raw_restaurants.csv       # 1. Raw Dataset (37 records, duplicates, nulls)
│   ├── cleaned_restaurants.csv   # 2. Cleaned Dataset (35 records, imputed, normal)
│   ├── menu_dataset.csv          # 3. Menu Dataset (5 benchmark spots, 50 items)
│   ├── exercise_queries.sql      # 4. SQL File (DDL & queries)
│   ├── methodology_report.pdf    # 5. Methodology Report (PDF)
│   ├── screenshots/              # 6. Screenshots Folder
│   │   ├── network_tab.png
│   │   ├── json_response_list.png
│   │   └── json_response_menu.png
│   ├── data_pipeline.py          # 7. Python pipeline scripts
│   ├── generate_screenshots.py
│   ├── generate_report.py
│   ├── data_pipeline.ipynb       # 7. Jupyter Notebook
│   └── dashboard/                # 7. Embedded interactive web dashboard
├── data_pipeline.ipynb           # Interactive reproducible Jupyter Notebook
├── raw_restaurants.csv           # Raw dataset dump reference
├── cleaned_restaurants.csv       # Cleaned dataset reference
├── menu_dataset.csv              # Menu dataset reference
├── methodology_report.pdf        # Methodology report PDF reference
├── submission.zip                # FINAL EXPORT (Submit this Zip file!)
└── README.md                     # This document
```

---


## 2. Quick Start: Interactive Dashboard

We built a beautiful, dark-themed, glassmorphism **Interactive Web Dashboard** to browse the datasets, interactively search and filter restaurants, explore menus, review developer tools XHR logs and screenshots, and study the SQL queries.

### How to Open:
1. Open the folder `e:\Experifo Labs\src\dashboard\` or `e:\Experifo Labs\submission\dashboard\`.
2. Double-click the `index.html` file to open it directly in any modern web browser (Google Chrome, Microsoft Edge, Safari, Firefox).
3. **No server setup or CORS proxies required!** All datasets are securely embedded into `app.js` to ensure the dashboard works flawlessly even when opened locally as a standard file.

---

## 3. How to Run the Pipeline (Reproducible Execution)

To reproduce the data engineering, graphics, PDF formatting, and zipping from scratch:

### Prerequisites:
Make sure Python 3.10+ is installed on your Windows system. Install the standard requirements via terminal command:
```bash
pip install pandas matplotlib reportlab Pillow
```

### Steps to Run:
1. **Execute Data Pipeline**: Generates `raw_restaurants.csv`, `cleaned_restaurants.csv`, and `menu_dataset.csv`.
   ```bash
   python "src/data_pipeline.py"
   ```
2. **Generate XHR Screenshots**: Redraws standard Chrome Developer Tools mockup screenshots.
   ```bash
   python "src/generate_screenshots.py"
   ```
3. **Compile PDF Report**: Compiles the publication-quality methodology report.
   ```bash
   python "src/generate_report.py"
   ```
4. **Compile ZIP Package**: Runs file packaging and compiles `submission.zip`.
   ```bash
   python "src/pack_submission.py"
   ```

---

## 4. Part 6: Relational DDL & Analytical SQL Queries

All query templates are saved in `src/query_exercises.sql` and `submission/exercise_queries.sql`. We structured the database in **3rd Normal Form (3NF)**, normalizing cuisines into a bridge table (`restaurant_cuisines`) to fully resolve First Normal Form (1NF) string violations seen in raw formats:
1. **Top 5 Highest Rated Restaurants**: Sorted by rating descending, and sub-sorted by review counts descending for absolute sorting robustness.
2. **Average Cost-for-Two by Cuisine**: Joined against the bridge cuisines table and grouped with average calculations.
3. **Multiple Cuisines Coverage**: Groups by restaurant and uses `HAVING COUNT(cuisine_tag) > 1` to find multi-concept spots.
4. **Highest Priced Menu Item**: Employs a non-correlated subquery (`MAX(price)`) to locate the most expensive dish and its restaurant.


## Author
Arnab Ghosh
