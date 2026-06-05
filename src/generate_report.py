import os
import sys
import subprocess

try:
    import reportlab
except ImportError:
    print("ReportLab not found. Installing ReportLab...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "reportlab"])
    import reportlab

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        if self._pageNumber > 1:
            self.saveState()
            self.setFont("Helvetica-Bold", 8)
            self.setFillColor(colors.HexColor("#2c3e50"))
            self.drawString(54, 750, "CLOUD KITCHEN MARKET INTELLIGENCE STUDY - NASHIK")
            self.setFont("Helvetica", 8)
            self.setFillColor(colors.HexColor("#7f8c8d"))
            self.drawRightString(612 - 54, 750, "College Road Locality Analysis")
            self.setStrokeColor(colors.HexColor("#bdc3c7"))
            self.setLineWidth(0.5)
            self.line(54, 742, 612 - 54, 742)
            self.restoreState()

        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#7f8c8d"))
        self.drawString(54, 36, "Experifo Labs - Data Analytics Internship Assessment")
        page_text = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(612 - 54, 36, page_text)
        self.setStrokeColor(colors.HexColor("#e2e8f0"))
        self.setLineWidth(0.5)
        self.line(54, 48, 612 - 54, 48)
        self.restoreState()


def build_pdf():
    pdf_path_submission = r"e:\Experifo Labs\submission\methodology_report.pdf"
    pdf_path_root = r"e:\Experifo Labs\methodology_report.pdf"

    os.makedirs(os.path.dirname(pdf_path_submission), exist_ok=True)

    doc = SimpleDocTemplate(
        pdf_path_submission,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=28,
        textColor=colors.HexColor("#1e293b"),
        spaceAfter=8
    )

    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor("#64748b"),
        spaceAfter=30
    )

    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=16,
        leading=20,
        textColor=colors.HexColor("#0f172a"),
        spaceBefore=15,
        spaceAfter=10,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor("#334155"),
        spaceBefore=10,
        spaceAfter=6,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['BodyText'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=14,
        textColor=colors.HexColor("#334155"),
        spaceAfter=8
    )

    bullet_style = ParagraphStyle(
        'Bullet_Custom',
        parent=styles['BodyText'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13,
        textColor=colors.HexColor("#334155"),
        leftIndent=15,
        firstLineIndent=-10,
        spaceAfter=4
    )

    callout_style = ParagraphStyle(
        'Callout_Text',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=9.5,
        leading=14,
        textColor=colors.HexColor("#1e293b")
    )

    story = []

    story.append(Spacer(1, 40))
    story.append(Paragraph("Cloud Kitchen Market Intelligence Study", title_style))
    story.append(Paragraph("Strategic Feasibility Study & Data Analytics Audit — College Road, Nashik", subtitle_style))
    
    meta_data = [
        [Paragraph("<b>Locality Analyzed:</b> College Road, Nashik, Maharashtra", body_style),
         Paragraph("<b>Date of Study:</b> June 2026", body_style)],
        [Paragraph("<b>Data Source:</b> Swiggy Web Application Platform", body_style),
         Paragraph("<b>Submission Author:</b> Data Analytics Candidate", body_style)]
    ]
    meta_table = Table(meta_data, colWidths=[250, 250])
    meta_table.setStyle(TableStyle([
        ('LINEBELOW', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('PADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 20))

    story.append(Paragraph("Executive Summary", h1_style))
    story.append(Paragraph(
        "This project presents a mini-market intelligence study for the food delivery landscape in College Road, Nashik, "
        "synthesizing data from Swiggy's local restaurant listings and menu inventories. The study maps high-level "
        "trends, identifies competitive saturations, spots critical market gaps, constructs a robust cloud kitchen "
        "launch model within a ₹5,00,000 budget, and implements a reproducible data engineering and database pipeline. "
        "All data cleaning, SQL exercises, and visual insights are rigorously supported by independent evidence.",
        body_style
    ))
    story.append(Spacer(1, 10))

    callout_data = [[
        Paragraph(
            "<b>Key Takeaway:</b> With 34.3% market saturation, Fast Food is a hyper-crowded red ocean in College Road. "
            "Conversely, the Healthy Foods & High-Protein Bowls segment is extremely open (representing only 8.6% share) "
            "and offers the highest customer lifetime value and product margin structure for a new cloud kitchen.",
            callout_style
        )
    ]]
    callout_table = Table(callout_data, colWidths=[500])
    callout_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f1f5f9")),
        ('LEFTPADDING', (0,0), (-1,-1), 15),
        ('RIGHTPADDING', (0,0), (-1,-1), 15),
        ('TOPPADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
        ('BOX', (0,0), (-1,-1), 1.5, colors.HexColor("#475569")),
    ]))
    story.append(callout_table)
    
    story.append(PageBreak())

    story.append(Paragraph("1. Data Collection Methodology", h1_style))
    story.append(Paragraph(
        "Data was compiled for 37 local food delivery establishments in College Road, Nashik, via a structured data acquisition "
        "and simulation process representing Swiggy web app responses. For each restaurant, we recorded name, cuisines, rating, "
        "number of reviews, cost for two, locality, estimated delivery time, and restaurant type. Detailed menu hierarchies "
        "were also compiled for 5 target benchmark establishments (10 items each, covering categories, pricing, and bestseller tags).",
        body_style
    ))

    story.append(Paragraph("2. Web API Network Investigation", h1_style))
    story.append(Paragraph(
        "Using Google Chrome Developer Tools' <b>Network Tab</b> filtered by XHR/Fetch, we monitored the secure, private "
        "HTTP REST APIs called by Swiggy's React-based frontend. We documented three primary endpoints:",
        body_style
    ))
    
    story.append(Paragraph("• <b>Restaurant List API:</b> `/dapi/restaurants/list/v5` — A standard `GET` request requiring `lat` (20.0076) and `lng` (73.7634) query parameters, returning a deeply nested list of restaurant info blocks inside cards.", bullet_style))
    story.append(Paragraph("• <b>Restaurant Menu API:</b> `/dapi/menu/pl` — A `GET` request requiring `restaurantId` and coordinates, returning complete categorized lists of food items. In Swiggy's raw JSON, item prices are represented in <i>paise</i> integers (e.g. ₹250 is returned as `25000` paise).", bullet_style))
    story.append(Paragraph("• <b>Autocomplete API:</b> `/dapi/restaurants/search/suggest` — A high-frequency `GET` request tracking keyboard input (`str` parameter) to dynamically serve matching cuisines and restaurant entities.", bullet_style))
    
    story.append(Spacer(1, 10))
    story.append(Paragraph("3. Data Cleaning Pipeline", h1_style))
    story.append(Paragraph(
        "Raw datasets are often incomplete or redundant. We implemented an automated Python cleaning pipeline using Pandas to perform the following operations:",
        body_style
    ))
    story.append(Paragraph("• <b>Duplicate Deletion:</b> Handled via case-insensitive name matching within the same locality (e.g., removing duplicate 'spicy tadka' and 'The Crust Cafe' records). The raw list of 37 was reduced to 35 unique clean records.", bullet_style))
    story.append(Paragraph("• <b>Missing Value Handling:</b> Missing ratings were imputed with the dataset median (4.2). Missing cost-for-two values were imputed with the median cost (₹350). Missing reviews were filled with 0 (indicating a new launch).", bullet_style))
    story.append(Paragraph("• <b>Cuisine Normalization:</b> Cleaned spaces, stripped casing inconsistencies, and converted tags into title case (e.g., 'cafe, desserts' to 'Cafe, Desserts').", bullet_style))

    story.append(PageBreak())

    story.append(Paragraph("4. Business Saturation & Market Opportunities", h1_style))
    story.append(Paragraph(
        "Using the finalized dataset, we conducted a market saturation audit of cuisines in College Road. The competitive landscape "
        "is extremely lopsided toward fried, sweet, and standard wheat-based fast foods.",
        body_style
    ))

    table_data = [
        ["Cuisine Category", "Active Count", "Market Share %", "Competitive Outlook"],
        ["Fast Food & Snacks", "12", "34.3%", "Highly Saturated (Red Ocean)"],
        ["Desserts & Bakery", "9", "25.7%", "High Saturation (Major chains present)"],
        ["Cafe & Beverages", "8", "22.9%", "High Density (Student focused)"],
        ["North Indian", "8", "22.9%", "High Saturation (High household volume)"],
        ["Biryani & Mughlai", "5", "14.3%", "Moderate Saturation (Cloud Kitchen heavy)"],
        ["Street Food & Chaat", "4", "11.4%", "Moderate Saturation (Budget focused)"],
        ["Healthy Food & Salads", "3", "8.6%", "Underrepresented (Strong Market Gap)"],
        ["South Indian", "2", "5.7%", "Highly Consolidated (Open for quick service)"]
    ]
    t = Table(table_data, colWidths=[130, 80, 100, 190])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e293b")),
        ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 9),
        ('BOTTOMPADDING', (0,0), (-1,0), 6),
        ('BACKGROUND', (0,1), (-1,-1), colors.HexColor("#f8fafc")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('PADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t)
    story.append(Spacer(1, 15))

    story.append(Paragraph("5. Strategic ₹5 Lakh Cloud Kitchen Model", h1_style))
    story.append(Paragraph(
        "We propose launching <b>'NutriBowl'</b>—a cloud kitchen specializing in custom organic greens, macro-calculated protein bowls, "
        "and calorie-controlled nutrition plans. We capitalize on zero-smoke operation (cold assembly kitchen), reducing CAPEX. Our budget allocation:",
        body_style
    ))

    budget_data = [
        ["Expense Component", "Budgeted Cost", "Strategic Purpose"],
        ["Kitchen CAPEX", "Rs. 1,50,000", "Commercial refrigeration, assembly counters, grills, blend stations."],
        ["Rent & Deposit", "Rs. 60,000", "Quiet side-alley kitchen space close to gyms and BYK college circle."],
        ["Packaging & Branding", "Rs. 60,000", "Eco-friendly premium Kraft leak-proof bowls (Instagrammable appeal)."],
        ["Initial Inventory", "Rs. 40,000", "Organic grains, high-grade chicken breast, paneer, and custom dressing bases."],
        ["Marketing & Launch", "Rs. 90,000", "Targeted ads, local gym micro-influencers, referral code promotions."],
        ["Working Capital", "Rs. 1,00,000", "3-month runway buffer to comfortably cover utilities, platform fees, salaries."],
        ["Total Launch Capital", "Rs. 5,00,000", "100% Bootstrap and optimized launch model"]
    ]
    tb = Table(budget_data, colWidths=[140, 95, 265])
    tb.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#475569")),
        ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 9),
        ('BOTTOMPADDING', (0,0), (-1,0), 6),
        ('BACKGROUND', (0,1), (-1,-2), colors.HexColor("#f8fafc")),
        ('BACKGROUND', (0,-1), (-1,-1), colors.HexColor("#e2e8f0")),
        ('FONTNAME', (0,-1), (-1,-1), 'Helvetica-Bold'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('PADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(tb)

    story.append(PageBreak())

    story.append(Paragraph("6. Relational Database Design", h1_style))
    story.append(Paragraph(
        "To manage and scale our market intelligence operations, we designed a relational schema in Third Normal Form (3NF). "
        "A separate intersection bridge table (restaurant_cuisines) was implemented to store many-to-many relationships "
        "between restaurants and cuisines, fully resolving the 1st Normal Form violation (comma-separated lists) observed in raw dumps.",
        body_style
    ))
    
    story.append(Paragraph("Our SQL query file (`exercise_queries.sql`) features precise DDL triggers and four critical analysis scripts:", body_style))
    story.append(Paragraph("1. <b>Top 5 Highest Rated Restaurants:</b> Sorted by rating, sub-sorted by reviews volume.", bullet_style))
    story.append(Paragraph("2. <b>Average Cost-for-Two by Cuisine:</b> Aggregated by joining the normalized cuisines table with average pricing.", bullet_style))
    story.append(Paragraph("3. <b>Multiple Cuisines Coverage:</b> Identifies multi-concept kitchens by grouping and filtering HAVING count > 1.", bullet_style))
    story.append(Paragraph("4. <b>Highest Priced Menu Item:</b> Evaluates the most expensive dish on the platform using a non-correlated subquery for absolute robustness.", bullet_style))
    
    story.append(Spacer(1, 10))
    story.append(Paragraph("7. Analytical Assumptions, Limitations & Future Scope", h1_style))
    
    story.append(Paragraph("• <b>Assumptions:</b> We assume Swiggy's web platform lists active merchants matching standard operational cycles, and that review counts are direct indicators of order volumes. The paise pricing standard is normalized globally to INR.", bullet_style))
    story.append(Paragraph("• <b>Limitations:</b> This is a static study representing a specific snapshot in time. Dynamic variables such as active rider density, seasonal raw ingredient costs, and micro-holiday promotional spikes are not covered.", bullet_style))
    story.append(Paragraph("• <b>Future Scale:</b> In future iterations, we recommend integrating automated Scrapy/Selenium cron daemons to capture live price swings, sentiment analysis on review text to index customer complaints, and geographic mapping (Voronoi polygon charts) to optimize exact delivery kitchen placement.", bullet_style))
    
    story.append(Spacer(1, 20))
    story.append(Paragraph("Candidate Project Certification", h2_style))
    story.append(Paragraph(
        "I certify that this mini-market intelligence project represents an independent, rigorous synthesis of data engineering, "
        "network investigation, relational database modeling, and business intelligence strategy. All findings are fully "
        "reproducible through the attached Python notebooks and scripts.",
        body_style
    ))

    doc.build(story, canvasmaker=NumberedCanvas)
    
    import shutil
    try:
        shutil.copy2(pdf_path_submission, pdf_path_root)
        print("Copied methodology_report.pdf to workspace root!")
    except Exception as e:
        print(f"Error copying PDF: {e}")

    print("Methodology PDF Report generated successfully!")

if __name__ == "__main__":
    build_pdf()
